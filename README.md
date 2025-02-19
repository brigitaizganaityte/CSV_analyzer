# CSV Data Analyzer

## Description
This program analyzes CSV files and provides various insights, such as column details, statistics, correlation, and missing values. Additionally, it allows exporting results and visualizing product amounts.

## Features
- Load and analyze CSV files.
- Display general file information, including statistics and missing values.
- Show column names and correlation matrix.
- Export selected data insights into a CSV file.
- Visualize product amounts using a bar chart.

## Requirements
- Python 3.x
- Required libraries:
  - `pandas`
  - `matplotlib`

To install dependencies, run:
```sh
pip install pandas matplotlib
```

## How to Use
1. Run the script and provide the CSV file name.
2. Choose from additional analysis options:
   - `1`: Show column names
   - `2`: Show correlation matrix
   - `3`: Show missing values
   - `4`: Export selected results to a CSV file
   - `5`: Visualize products vs. amount
   - `6`: Exit the program
3. Follow on-screen prompts to analyze or export data.
4. If exporting, select the type of data to include and specify a filename.

## Example Run
```
Please provide file name that should be analyzed: data.csv
ANALYSIS OF THE FILE
Main information:
<class 'pandas.core.frame.DataFrame'>
...
Additional analysis options:
1: Show columns
2: Correlation
3: Show missing values
4: Export results to csv
5: Visualization of products vs amount
6: End
Please select option: 1
Columns in data:
Index(['Product', 'Amount'], dtype='object')
```

## Error Handling
- If the file is not found, the program will notify the user.
- If the file is empty, an error message is displayed.
- If the file format is incorrect, a parsing error message is shown.

## Notes
- Ensure the CSV file is in the same directory as the script.
- The visualization option assumes the CSV file contains `Product` and `Amount` columns.


