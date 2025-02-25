# Transaction Value Analysis

This project analyzes transaction data from two databases (WCOB_SAMS_INTEGRATED and WCOB_DILLARDS) to compare sales trends and identify potential market opportunities. This analysis was conducted as an experiment to determine if valuable insights could be extracted from combining data across these two databases. While a data warehouse would be a more practical solution for regular analysis, this project demonstrates the potential for cross-database analysis when a common key (state abbreviation) is available.

## Data Retrieval

The data is retrieved using a SQL query that spans both databases and performs various statistical calculations. The query takes approximately 3-4 minutes to execute.

## Data Export

The results of the SQL query are exported to a CSV file named `results.csv`.

## Python Analysis

The `run.py` script performs the following steps:

1. **Data Loading:** Loads the data from `results.csv` into a pandas DataFrame.
2. **Data Cleaning:** Handles missing values and converts relevant columns to numeric format.
3. **Data Aggregation:** Groups the data by state and category to calculate average transaction values and price deltas.
4. **Visualization:** Creates three bar plots to visualize:
   - Average Sams Transaction Value by State and Category
   - Average Dillards Transaction Value by State and Category
   - Price Delta (Sams - Dillards) by State and Category
5. **Output:** Saves the plots to a PNG file named `transaction_analysis.png` and displays them.

## Requirements

- Python 3.6 or higher
- pandas
- matplotlib
- numpy

## Usage

1. Ensure the `results.csv` file is in the same directory as `run.py`.
2. Run the `run.py` script: `python run.py`


This will generate a file named `transaction_analysis.png`.
