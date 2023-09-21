
---

# Pokémon Operations Research Optimizer

## Overview

This project aims to use operations research techniques to optimize the selection of Pokémon based on various constraints and objective functions, such as maximizing "coolness" while adhering to a limited "stardust" budget. The project is a blend of data analytics, operations research, and software development.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Database Schema](#database-schema)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

## Getting Started

Clone this repo to your local machine to get started with the project.

```bash
git clone https://github.com/yourusername/Pokemon-OR-Optimizer.git
```

## Prerequisites

- Python 3.x
- MySQL
- PuLP library for Python
- Other libraries and dependencies are listed in the `requirements.txt` file.

## Installation

1. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up your MySQL database and note down your credentials.

3. Update the `DB_CONFIG` variable in the script to match your database credentials.

## Usage

Run the main Python script to start the optimization process.

```bash
python pogo_OR.py
```

This will generate an optimal selection of Pokémon based on the constraints specified in the script.

## Technologies Used

- Python
- MySQL
- PuLP (Python library for linear programming)
- SQL queries for data manipulation and retrieval

## Database Schema

The database schema is available as a SQL dump in the `schema.sql` file.

To import the schema into your MySQL database:

```bash
mysql -u [username] -p [database_name] < schema.sql
```

## Contributing

If you would like to contribute or have any suggestions, please fork the repository and create a new pull request, or open an issue.

## License

This project is licensed under the MIT License. See `LICENSE.md` for more details.

## Acknowledgments

- Credits to the Pokémon database sources.

