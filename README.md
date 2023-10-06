# Pokémon GO Collection Optimizer

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The Pokémon GO Collection Optimizer is a comprehensive tool designed to help Pokémon GO players optimize their Pokémon collections. Utilizing Optical Character Recognition (OCR), MySQL databases, and linear programming techniques, the project aims to find the optimal set of Pokémon to power up based on a custom "coolness" metric, while also considering constraints such as stardust budget and candy limits.

---

## Features

### OCR (POGO_OCR.py)

- Captures key Pokémon metrics like Combat Power (CP), Current HP, Total HP, and Stardust using Google Vision API.
- Stores OCR results in a pandas DataFrame for subsequent analysis and optimization.

### Database Management (POGOR.sql)

- Defines the schema for various tables that store Pokémon attributes, moves, and types.
- Populates initial data to kickstart the optimization process.

### Optimization (pogo_OR.py)

- Fetches Pokémon data from a MySQL database.
- Uses linear programming to optimize the Pokémon collection based on a "coolness" metric.
- Considers various constraints like stardust budget and candy limits.

---

## Technology Stack

- **Programming Language**: Python
- **OCR**: Google Vision API
- **Database**: MySQL
- **Linear Programming Library**: PuLP

---

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Google Vision API credentials

### Steps

1. Clone the repository:

```
git clone https://github.com/your-username/pokemon-go-optimizer.git
```

2. Navigate to the project directory:

```
cd pokemon-go-optimizer
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Set up the MySQL database using the provided SQL file (`POGOR.sql`):

```
mysql -u root -p < POGOR.sql
```

5. Add your Google Vision API credentials to `POGO_OCR.py`.

---

## Usage

1. Run the OCR script to capture and store Pokémon metrics:

```
python POGO_OCR.py
```

2. Run the optimization script to find the optimal set of Pokémon to power up:

```
python pogo_OR.py
```

---

## Future Enhancements

- Integration with Tableau for interactive visualization and constraint adjustments.
- Real-time OCR and database updates.
- Additional optimization constraints and objectives.

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
