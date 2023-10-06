# Pokémon GO Collection Optimizer: A Comprehensive Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
    1. [Optical Character Recognition (OCR)](#optical-character-recognition-ocr)
    2. [Database Management](#database-management)
    3. [Optimization Engine](#optimization-engine)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
    1. [Prerequisites](#prerequisites)
    2. [Installation Steps](#installation-steps)
5. [Usage](#usage)
    1. [Data Collection](#data-collection)
    2. [Optimization](#optimization)
6. [Code Structure](#code-structure)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

The Pokémon GO Collection Optimizer is designed to assist Pokémon GO enthusiasts in maximizing the effectiveness of their collections. The tool integrates Optical Character Recognition (OCR), SQL databases, and linear programming algorithms to find the optimal collection of Pokémon to power up, all the while considering real-world constraints such as stardust budgets and candy limits.

---

## Features

### Optical Character Recognition (OCR)

**File**: `POGO_OCR.py`

- **What it Does**: 
  - Captures Pokémon metrics such as Combat Power (CP), Current HP, Total HP, and Stardust from screenshots of the Pokémon GO app.
- **Technology**: 
  - Utilizes Google Vision API for OCR capabilities.
- **Data Storage**: 
  - Stores the captured metrics in a pandas DataFrame for future analysis and optimization.

### Database Management

**File**: `POGOR.sql`

- **What it Does**: 
  - Manages the database schema and initial data to support the optimization process.
- **Tables**: 
  - Includes tables for Pokémon attributes, moves, and types.
- **Technology**: 
  - MySQL is used for database management.

### Optimization Engine

**File**: `pogo_OR.py`

- **What it Does**: 
  - Optimizes the Pokémon collection based on a customizable "coolness" metric.
- **Technology**: 
  - Utilizes PuLP library for the linear programming algorithm.
- **Constraints**: 
  - Considers limitations like stardust budget and candy limits.

---

## Technology Stack

- **Python**: Main programming language for scripting and data manipulation.
- **Google Vision API**: For OCR capabilities.
- **MySQL**: For database management.
- **PuLP**: Linear programming library for optimization.

---

## Installation

### Prerequisites

- Python 3.x installed.
- MySQL server up and running.
- Google Vision API credentials.

### Installation Steps

1. **Clone the Repository**
    ```
    git clone https://github.com/your-username/pokemon-go-optimizer.git
    ```
  
2. **Navigate to Project Directory**
    ```
    cd pokemon-go-optimizer
    ```

3. **Install Required Packages**
    ```
    pip install -r requirements.txt
    ```

4. **Database Setup**
    ```
    mysql -u root -p < POGOR.sql
    ```

5. **Google Vision API Credentials**
    - Add your API credentials to `POGO_OCR.py`.

---

## Usage

### Data Collection

- Run the OCR script to collect Pokémon metrics.

    ```
    python POGO_OCR.py
    ```

### Optimization

- Execute the optimization script to obtain the optimal set of Pokémon to power up.

    ```
    python pogo_OR.py
    ```

---

## Code Structure

- `POGO_OCR.py`: Contains functions for OCR and data storage.
- `POGOR.sql`: SQL file for database schema and initial data.
- `pogo_OR.py`: Includes the optimization algorithm.
- `requirements.txt`: Lists all the Python dependencies.

---

## Future Enhancements

- **Tableau Integration**: For enhanced visualization and interactive constraint adjustments.
- **Real-time OCR**: To continuously update the database.
- **Advanced Optimization Criteria**: For more complex constraints and objective functions.

---

## Contributing

- Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

## License

- This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for more details.

---

This README aims to provide a complete understanding of the project and its functionalities. It's an excellent way to introduce others to the complexities and features of the Pokémon GO Collection Optimizer.
