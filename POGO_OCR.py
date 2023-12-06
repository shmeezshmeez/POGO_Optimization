
# Import MySQL Connector
import mysql.connector

# Establish a MySQL Connection
mydb = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object
mycursor = mydb.cursor()


import os
import re
import logging
import json
import pandas as pd
from google.cloud import vision_v1
from typing import List, Tuple
from PIL import Image
import pytesseract
from PIL import ImageEnhance
import cv2
import numpy as np

# Your Google Cloud credentials path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/samuelfriedman/Downloads/axial-entity-398308-0e004580c5e8.json"

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Load the Pokémon names from a file named pokemon_names.txt
pokemon_names = []
with open('pokemon_names.txt', 'r') as file:
    pokemon_names = [line.strip() for line in file]

# List of Pokémon that can Mega Evolve
# List of Pokémon that can Mega Evolve
MEGA_EVOLUTION_LIST = [
    "VENUSAUR", "CHARIZARD", "BLASTOISE", "BEEDRILL", "PIDGEOT", "ALAKAZAM", "SLOWBRO",
    "GENGAR", "KANGASKHAN", "PINSIR", "GYARADOS", "AERODACTYL", "MEWTWO", "AMPHAROS",
    "STEELIX", "SCIZOR", "HERACROSS", "HOUNDOOM", "TYRANITAR", "SCEPTILE", "BLAZIKEN",
    "SWAMPERT", "GARDEVOIR", "SABLEYE", "MAWILE", "AGGRON", "MEDICHAM", "MANECTRIC",
    "SHARPEDO", "CAMERUPT", "ALTARIA", "BANETTE", "ABSOL", "GLALIE", "SALAMENCE",
    "METAGROSS", "LATIAS", "LATIOS", "RAYQUAZA", "LOPUNNY", "GARCHOMP", "LUCARIO",
    "ABOMASNOW", "GALLADE", "AUDINO", "DIANCIE"]
# Functions (they remain the same as before)

def extract_text_from_image(image_path):
    client = vision_v1.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description if texts else ""
def can_mega_evolve(pokemon_name):
    return pokemon_name in MEGA_EVOLUTION_LIST
import cv2
import numpy as np

def extract_filled_bar_percentage(image_path):
    # Read the image and convert to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binary threshold
    _, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Define the regions for Attack, Defense, and HP bars
    attack_region = threshed[1620:1650, 100:1100]
    defense_region = threshed[1720:1750, 100:1100]
    hp_region = threshed[1820:1850, 100:1100]

    return {
        "Attack": np.sum(attack_region) / 255 / (attack_region.shape[0] * attack_region.shape[1]),
        "Defense": np.sum(defense_region) / 255 / (defense_region.shape[0] * defense_region.shape[1]),
        "HP": np.sum(hp_region) / 255 / (hp_region.shape[0] * hp_region.shape[1])
    }

def calculate_iv(percentage):
    return round(percentage * 15)
def extract_pokemon_names_from_tesseract(image_path: str, reference_names: List[str] = pokemon_names) -> str:
    """
    Extracts Pokémon name from a given image using Tesseract OCR.

    Parameters:
    - image_path (str): Path to the image from which the name needs to be extracted.
    - reference_names (List[str]): List of Pokémon names for reference. Default is the global pokemon_names list.

    Returns:
    - str: Recognized Pokémon name from the image.
    """
    image = Image.open(image_path)
    
    # Convert image to grayscale
    image = image.convert('L')
    
    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # The enhancement factor (e.g., 2 means doubling the contrast)

    extracted_text = pytesseract.image_to_string(image, config='--psm 6').lower()
    for name in reference_names:
        if name in extracted_text:
            return name
    return ""


def extract_pokemon_names_from_vision(image_path: str, reference_names: List[str] = pokemon_names) -> List[str]:
    """
    Extracts Pokémon names from a given image using OCR.
    """
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image, config='--psm 6').lower()
    logging.info(f"Raw text extracted by Tesseract: {extracted_text}")
    recognized_names = [name for name in reference_names if name in extracted_text]
    
    return recognized_names
def extract_details_from_vision(texts: List[str]):
    combined_text = " ".join(texts)
    ...

    details = {}

    # Extracting CP
    cp_match = re.search(r'CP(\d+)', combined_text)
    if cp_match:
        details['cp'] = int(cp_match.group(1))

    # Extracting HP
    hp_match = re.search(r'(\d+)/(\d+) HP', combined_text)
    if hp_match:
        details['current_hp'] = int(hp_match.group(1))
        details['total_hp'] = int(hp_match.group(2))

    # Extract total Stardust
    stardust_match = re.search(r'(\d+) stardust', combined_text, re.IGNORECASE)
    if stardust_match:
        details['stardust'] = int(stardust_match.group(1))

    logging.info(f"Extracted details: {details}")
        # Extract date caught
    date_match = re.search(r'caught on (\d{1,2}/\d{1,2}/\d{4})', combined_text)
    if date_match:
        details['date_caught'] = date_match.group(1)

    # Extract location
    location_match = re.search(r'around (.+), (.+), (.+)', combined_text)
    if location_match:
        details['city'] = location_match.group(1).strip()
        details['state'] = location_match.group(2).strip()
        details['country'] = location_match.group(3).strip()
    return details
def process_image(image_path: str) -> dict[str, any]:
    """Process the image to extract Pokémon details."""
    # Extract details using Tesseract (assuming Google Vision parts are skipped as per environment constraints)
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image, config='--psm 6')
    details = extract_details_from_vision([extracted_text])
    texts = extract_text_from_image(image_path)
    print("Raw texts from Google Vision:", texts)  # Debug line

    return details

def extract_details_from_text(text):
    details = {}

    cp_match = re.search(r'CP(\d+)', text)
    if cp_match:
        details['cp'] = int(cp_match.group(1))

    hp_match = re.search(r'(\d+)/(\d+) HP', text)
    if hp_match:
        details['current_hp'] = int(hp_match.group(1))
        details['total_hp'] = int(hp_match.group(2))

    stardust_match = re.search(r'(\d+) STARDUST', text)
    if stardust_match:
        details['power_up_stardust'] = int(stardust_match.group(1))

    candy_match = re.search(r'(\d+) .*? CANDY', text)
    if candy_match:
        details['candy_count'] = int(candy_match.group(1))

    name = None
    for pokemon in MEGA_EVOLUTION_LIST:
        if pokemon in text.upper():
            name = pokemon
            break

    if name:
        details['name'] = name
        details['can_mega_evolve'] = True
    else:
        # If name is not in the Mega Evolution list, try to identify it from the list of all Pokémon
        for pokemon in pokemon_names:  # pokemon_names should contain all Pokémon names
            if pokemon in text.upper():
                details['name'] = pokemon
                break

    return details
def process_video(video_path: str, output_folder: str):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        extracted_details = process_image(frame_path)

        # Print or store the extracted details
        print(f"Frame {frame_count} details:", extracted_details)

        frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_path = "/path/to/your/video.mp4"  # Change this to your video path
    output_folder = "/path/to/output/folder"  # Change this to your desired output folder
    process_video(video_path, output_folder)


# Create a table to store OCR data, if it doesn't already exist
create_table_query = 'CREATE TABLE IF NOT EXISTS pokemon_data (id INT AUTO_INCREMENT PRIMARY KEY, pokemon_name VARCHAR(255), dps FLOAT, ivs FLOAT, special_status VARCHAR(255), moves VARCHAR(255), recommended_for_powerup BOOLEAN)'
mycursor.execute(create_table_query)


# Insert OCR data into the table
insert_data_query = 'INSERT INTO pokemon_data (pokemon_name, dps, ivs, special_status, moves, recommended_for_powerup) VALUES (%s, %s, %s, %s, %s, %s)'
mycursor.execute(insert_data_query, (your_pokemon_name, your_dps, your_ivs, your_special_status, your_moves, your_recommendation))


# Commit changes and close the connection
mydb.commit()
mycursor.close()
mydb.close()
