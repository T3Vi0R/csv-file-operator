# Code Generator and CSV Splitter

## Overview
This Python application provides two main functionalities:
1. **Generate Promotion Codes**: Creates a .csv file with random promotion codes based on the length and quantity provided by the user.
2. **Split CSV Files**: Splits a larger .csv file into smaller ones, each with a maximum size of 2MB.

The application features a simple graphical user interface built using `tkinter` and leverages the `pandas` library for efficient CSV processing.

## Features
- **Generate Random Codes**: Enter the desired length and quantity of codes to generate a .csv file with unique codes, excluding confusing characters like `0`, `O`, `o`, `i`, `l`, `L`, `I`.
- **Split Large CSV Files**: Select a large .csv file and automatically split it into multiple smaller files, each no larger than 2MB.
- **Progress Bar**: Visual indication of the progress during the CSV splitting operation.
- **User-Friendly Interface**: Easy-to-use GUI with a fixed window size and enhanced styling.

## Requirements
- Python 3.x
- `tkinter` (usually included with Python)
- `pandas`

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/T3Vi0R/csv-file-operator.git
   cd csv-file-operator
   ```
2. **Install the required libraries**:
   ```sh
   pip install pandas
   ```

## Usage
1. **Run the application**:
   ```sh
   python main.py
   ```
2. **Generate Codes**:
   - Enter the desired length and quantity of codes.
   - Click "Generate Codes" and choose where to save the .csv file.
3. **Split CSV Files**:
   - Click "Split CSV" and select the large .csv file to split.
   - The split files will be saved in the same directory with `_part_x` suffixes.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact
For more information, please visit [CODEFLOAT](https://www.codefloat.pl).