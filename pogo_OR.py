# Standard Library Imports
import math
import json
import random
from typing import List, Dict

# Third-Party Imports
import mysql.connector as mysql
import pandas as pd
import numpy as np
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value
from pulp import PULP_CBC_CMD

# Database Connection Settings
DB_CONFIG = {
    'host': "localhost",
    'user': "root",
    'password': "Shmeezshmeez2001!",
    'database': "POGOR"
}

# Global Constants
MY_STARDUST = 10000
# Create the DataFrame
# Given data
# Level range from 1 to 50 with 0.5 increments
levels = [i + 0.5 * j for i in range(1, 51) for j in range(2)]

# Stardust and Candy costs based on the provided data (truncated to match the length of levels list)
stardust_costs = [200]*4 + [400]*4 + [600]*4 + [800]*4 + [1000]*4 + [1300]*4 + [1600]*4 + [1900]*4 + \
                 [2200]*4 + [2500]*4 + [3000]*4 + [3500]*4 + [4000]*4 + [4500]*4 + [5000]*4 + \
                 [6000]*4 + [7000]*4 + [8000]*4 + [9000]*4 + [10000]*4 + [11000]*4 + [12000]*4 + \
                 [13000]*4 + [14000]*4 + [15000]*4

candy_costs = [1]*20 + [2]*20 + [3]*20 + [4]*8 + [6]*4 + [8]*4 + [10]*4 + [12]*4 + [15]*4 + [17]*4 + [20]*4

# After level 40, Candy XL is required. 1 Candy XL = 100 regular Candy
candy_xl = [10]*4 + [12]*4 + [15]*4 + [17]*4 + [20]*4

# Convert Candy XL to regular Candy and append to candy_costs list
candy_costs += [xl * 100 for xl in candy_xl]

# Make sure all lists are of the same length
min_length = min(len(levels), len(stardust_costs), len(candy_costs))
levels = levels[:min_length]
stardust_costs = stardust_costs[:min_length]
candy_costs = candy_costs[:min_length]
print(f"Level Length: {len(levels)}")
print(f"Stardust Length: {len(stardust_costs)}")
print(f"Candy Length: {len(candy_costs)}")

# Create the DataFrame
POWER_UP_COSTS = pd.DataFrame({
    'Level': levels,
    'Stardust': stardust_costs,
    'Candy': candy_costs,
})


# Utility Functions
def connect_to_database(config):
    try:
        conn = mysql.connect(**config)
        return conn, conn.cursor()
        
    except mysql.Error as err:
        print(f"Error: {err}")
        exit(1)

def move_type_matches_pokemon_type(cursor, move_name, pokemon_id, move_type):
    valid_move_types = ['fast', 'charge']
    
    if move_type.lower() not in valid_move_types:
        raise ValueError(f"move_type must be either {', '.join(valid_move_types)}")
        
    table = f"{move_type.lower()}_moves_stats"
    cursor.execute(f"SELECT type FROM {table} WHERE move_name = %s", (move_name,))
    fetched_move_type = cursor.fetchone()[0]
    
    cursor.execute("SELECT type1, type2 FROM species_stats WHERE species_id = %s", (pokemon_id,))
    pokemon_types = cursor.fetchone()
    
    return fetched_move_type in pokemon_types

# CP Multiplier Calculation
def get_cp_multiplier(level):
    return 0.095 * math.pow(level, 2) - 0.854 * level + 10 if level > 1 else 0.095

# Type Effectiveness Calculation
def calculate_effectiveness(cursor, attacking_type, defending_type):
    cursor.execute("""
        SELECT effectiveness_multiplier
        FROM type_effectiveness
        WHERE attacking_type = %s AND defending_type = %s
    """, (attacking_type, defending_type))
    
    result = cursor.fetchone()
    return result[0] if result else 1
#
# Power-up Costs Calculation
def get_power_up_costs(level, pokemon_type):
    row = POWER_UP_COSTS[POWER_UP_COSTS['Level'] == level]
    stardust, candy = row['Stardust'].values[0], row['Candy'].values[0]
    
    if pokemon_type == 'Lucky':
        stardust *= 0.5
    elif pokemon_type == 'Purified':
        stardust *= 0.9
        candy *= 0.9
    elif pokemon_type == 'Shadow':
        stardust *= 1.2
        candy *= 1.2
    
    return stardust, candy

# Fetch Pokemon and Species Stats
def fetch_pokemon_species_stats(cursor):
    print("Testing database connection...")
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    print(f"Test query result: {result}")

    cursor.execute("""
        SELECT 
            my_pokemon.pokemon_id,
            my_pokemon.Shadow,
            my_pokemon.Lucky,
            species_stats.base_attack,
            species_stats.base_defense,
            species_stats.base_stamina,
            my_pokemon.attack_iv,
            my_pokemon.defense_iv,
            my_pokemon.stamina_iv,
            my_pokemon.level,
            my_pokemon.fast_move,
            my_pokemon.charge_move
        FROM 
            my_pokemon
        INNER JOIN 
            species_stats ON my_pokemon.Pokemon = species_stats.`order`
    """)
    
    return cursor.fetchall()



# Fetch Fast Move Stats
def fetch_fast_move_stats(cursor):
    cursor.execute("""
        SELECT 
            my_pokemon.pokemon_id,
            my_pokemon.fast_move,
            fast_move_stats.power AS fast_move_power,
            fast_move_stats.duration AS fast_move_duration,
            fast_move_stats.energy AS fast_move_energy,
            fast_move_stats.type AS fast_move_type
        FROM 
            my_pokemon
        INNER JOIN
            fast_move_stats ON LOWER(my_pokemon.fast_move) = LOWER(fast_move_stats.Move)
    """)
    
    return cursor.fetchall()

# Fetch Charge Move Stats
def fetch_charge_move_stats(cursor):
    cursor.execute("""
        SELECT 
            my_pokemon.pokemon_id,
            my_pokemon.charge_move,
            charge_move_stats.power AS charge_move_power,
            charge_move_stats.CD AS charge_move_duration,
            charge_move_stats.EPS AS charge_move_energy,
            charge_move_stats.type AS charge_move_type
        FROM 
            my_pokemon
        INNER JOIN
            charge_move_stats ON LOWER(my_pokemon.charge_move) = LOWER(charge_move_stats.Move)
    """)
    
    return cursor.fetchall()
# Fetch All Required Data later include my_pokemon.Shadow,
def fetch_all_data(cursor) -> list:
    cursor.execute("""
        SELECT 
            my_pokemon.level,
            my_pokemon.id,
            
            my_pokemon.Lucky,
            species_stats.base_attack,
            species_stats.base_defense,
            species_stats.base_stamina,
            my_pokemon.attack_iv,
            my_pokemon.defense_iv,
            my_pokemon.stamina_iv,
            my_pokemon.fast_move,
            my_pokemon.charge_move,
            fast_move_stats.power AS fast_move_power,
            fast_move_stats.duration AS fast_move_duration,
            fast_move_stats.energy AS fast_move_energy,
            fast_move_stats.type AS fast_move_type,
            charge_move_stats.power AS charge_move_power,
            charge_move_stats.CD AS charge_move_duration,
            charge_move_stats.EPS AS charge_move_energy,
            charge_move_stats.type AS charge_move_type
        FROM 
            my_pokemon
        INNER JOIN 
            species_stats ON my_pokemon.`id` = species_stats.`species_id`
        INNER JOIN
            fast_move_stats ON LOWER(my_pokemon.fast_move) = LOWER(fast_move_stats.Move)
        INNER JOIN
            charge_move_stats ON LOWER(my_pokemon.charge_move) = LOWER(charge_move_stats.Move)
    """)
    print("Fetching all data...")
    results = cursor.fetchall()
    print(f"Number of rows fetched: {len(results)}")
    print(f"First few rows: {results[:3]}")

    return results  # Return the fetched results instead of calling fetchall() again

# Close database connection
def close_database_connection(conn):
    
    conn.close()

from typing import List, Dict

MEGA_POKEMON_IDS = [3, 6, 9, 65, 94, 115, 127, 130, 142, 150, 181, 212, 214, 229, 248, 257, 282, 303, 306, 308, 310, 354, 359, 380, 381, 445, 448, 460]
SHINY_WEIGHT = 1.5
MEGA_WEIGHT = 1.2
NUNDO_WEIGHT = 1.2

def calculate_adjusted_stats(base_stat_value: int, iv: int, cp_multiplier: float, is_shadow: bool = False) -> float:
    if iv is None:
        iv = 0
    return (base_stat_value + iv) * cp_multiplier * (1.2 if is_shadow else 1)

def calculate_dmg(adjusted_attack: float, adjusted_defense: float, move_power: int, stab_bonus: float) -> int:
    return math.floor(0.5 * move_power * (adjusted_attack / adjusted_defense) * stab_bonus ) + 1

def calculate_dps_parameters(dmg: int, duration: int, energy: int) -> float:
    return dmg / duration, energy / duration

def get_coolness_rating(pokemon_id: int, attack_iv: int, defense_iv: int, stamina_iv: int, adjusted_attack: float, fast_dps: float, charge_dps: float) -> float:
    coolness = 0.0
    
    # Prioritize Mega Pokémon
    if pokemon_id in MEGA_POKEMON_IDS:
        coolness += MEGA_WEIGHT
    
    # Prioritize perfect IV Pokémon
    if attack_iv == 15 and defense_iv == 15 and stamina_iv == 15:
        coolness += 1.1
    
    # Prioritize Nundo Pokémon (all IVs are zero)
    if attack_iv == 0 and defense_iv == 0 and stamina_iv == 0:
        coolness += NUNDO_WEIGHT
    
    # Prioritize high CP Pokémon (using adjusted_attack as a proxy)
    coolness += adjusted_attack * 1.1
    
    # Prioritize high DPS Pokémon
    total_dps = fast_dps + charge_dps
    coolness += total_dps * 1.1
    
    return coolness


def process_pokemon_data(results: List[Dict]) -> List[Dict]:
    print("Starting process_pokemon_data function...")
    
    # Debug: Check the type and content of 'results'
    print(f"Type of results: {type(results)}")
    
    # Initialize an empty list to store processed Pokémon data
    pokemon_data_list = []
    
    for idx, row in enumerate(results):
        # Debug: Check the enumeration
        
        # This assumes that your SQL query returns 19 values
        [
            level, pokemon_id, is_lucky, base_attack,
            base_defense, base_stamina, attack_iv, defense_iv, stamina_iv,
            fast_move, charge_move, fast_move_power, fast_move_duration,
            fast_move_energy, fast_move_type, charge_move_power, charge_move_duration,
            charge_move_energy, charge_move_type
        ] = row

        # Calculate stats
        cp_multiplier = get_cp_multiplier(level)
        adjusted_attack = calculate_adjusted_stats(int(base_attack), attack_iv, cp_multiplier)
        adjusted_defense = calculate_adjusted_stats(int(base_defense), defense_iv, cp_multiplier)
        adjusted_stamina = calculate_adjusted_stats(int(base_stamina), stamina_iv, cp_multiplier)

        # Calculate damage and DPS parameters
        fast_dmg = calculate_dmg(adjusted_attack, adjusted_defense, fast_move_power, 1.2)
        charge_dmg = calculate_dmg(adjusted_attack, adjusted_defense, charge_move_power, 1.2)
        fast_dps, fast_eps = calculate_dps_parameters(fast_dmg, fast_move_duration, fast_move_energy)
        charge_dps, charge_eps = calculate_dps_parameters(charge_dmg, charge_move_duration, charge_move_energy)

        # Calculate coolness rating
        coolness_rating = get_coolness_rating(pokemon_id, attack_iv, defense_iv, stamina_iv, adjusted_attack, fast_dps, charge_dps)

        # Create a dictionary for each Pokémon
        pokemon_data = {
            'pokemon_id': pokemon_id,
            # 'is_shadow': is_shadow,
            # 'Pokemon': Pokemon,
            'is_lucky': is_lucky,
            'adjusted_attack': adjusted_attack,
            'adjusted_defense': adjusted_defense,
            'adjusted_stamina': adjusted_stamina,
            'coolness_rating': coolness_rating,
            'fast_dps': fast_dps,
            'charge_dps': charge_dps
        }

        # Append each Pokémon's data to the list
        pokemon_data_list.append(pokemon_data)

    print(f"Processed {len(pokemon_data_list)} Pokémon records.")
    return pokemon_data_list


def create_decision_variables(pokemon_data_list: List[Dict]) -> Dict:
        return {pokemon['pokemon_id']: LpVariable(cat='Binary', name=f"Pokemon_{pokemon['pokemon_id']}") for pokemon in pokemon_data_list}


def add_objective_function(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict) -> None:
        prob += lpSum(
            [decision_vars[pokemon['pokemon_id']] * pokemon['coolness_rating'] for pokemon in pokemon_data_list]
        ), "Total_Coolness"


def add_stardust_constraint(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict, stardust_budget: int) -> None:
        prob += lpSum(
            [decision_vars[pokemon['pokemon_id']] * 1000 for pokemon in pokemon_data_list]
        ) <= stardust_budget, "Stardust_Constraint"

#need to add candy constraint
def add_candy_constraint(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict) -> None:
        for pokemon in pokemon_data_list:
            prob += decision_vars[pokemon['pokemon_id']] * 50 <= 500, f"Candy_Constraint_{pokemon['pokemon_id']}"


def add_mega_evolution_constraint(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict) -> None:
        prob += lpSum(
            [decision_vars[pokemon['pokemon_id']] for pokemon in pokemon_data_list if pokemon['pokemon_id'] in MEGA_POKEMON_IDS]
        ) <= 1, "Total_Mega_Evolution_Constraint"


def solve_problem(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict) -> None:
        prob.solve(PULP_CBC_CMD(msg=0))
        for pokemon in pokemon_data_list:
            if decision_vars[pokemon['pokemon_id']].value() == 1:
                if 'Pokemon' in pokemon:
                    print(f"Power up {pokemon['Pokemon']} with the following stats:")


def display_results(prob: LpProblem, pokemon_data_list: List[Dict], decision_vars: Dict) -> None:
        print(f"Status: {LpStatus[prob.status]}")
        print(f"Total Coolness: {value(prob.objective)}")


def main():
        conn, cursor = connect_to_database(DB_CONFIG)

        try:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()

            results = fetch_all_data(cursor)
            pokemon_data_list = process_pokemon_data(results)

            prob = LpProblem("Pokemon_Power_Up", LpMaximize)
            decision_vars = create_decision_variables(pokemon_data_list)
            print(f"Number of decision variables created: {len(decision_vars)}")

            add_objective_function(prob, pokemon_data_list, decision_vars)
            add_stardust_constraint(prob, pokemon_data_list, decision_vars, MY_STARDUST)
            add_candy_constraint(prob, pokemon_data_list, decision_vars)
            add_mega_evolution_constraint(prob, pokemon_data_list, decision_vars)
            print(f"Objective set: {bool(prob.objective)}, Number of constraints: {len(prob.constraints)}")

            solve_problem(prob, pokemon_data_list, decision_vars)
            display_results(prob, pokemon_data_list, decision_vars)
            prob.writeLP("PokemonProblem.lp")
           
        finally:
            print(f"Number of Pokemon processed: {len(pokemon_data_list)}")
            print(f"Number of decision variables: {len(decision_vars)}")
            print(f"Objective set: {prob.objective is not None}, Number of constraints: {len(prob.constraints)}")
            print(f"Status: {LpStatus[prob.status]}")
            print(f"Total Coolness: {value(prob.objective)}")
            print(f"Number of Pokemon processed: {len(pokemon_data_list)}")
            print(f"Number of decision variables: {len(decision_vars)}")
            print(f"Objective set: {'Yes' if prob.objective else 'No'}, Number of constraints: {len(prob.constraints)}")
            selected_pokemon = [pokemon for pokemon in pokemon_data_list if decision_vars[pokemon['pokemon_id']].value() == 1]
            print(f"Number of selected Pokemon: {len(selected_pokemon)}")

            close_database_connection(conn)


if __name__ == '__main__':
        main()
