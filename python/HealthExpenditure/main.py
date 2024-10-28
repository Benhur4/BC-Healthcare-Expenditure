
import pandas as pd

# Load the entire sheet
sheet = pd.read_excel('path_to_excel_file.xlsx', sheet_name='Sheet1')

# Assuming you know the row ranges for each table
table1 = sheet.iloc[1:20]  # Example range for Table 1
table2 = sheet.iloc[21:40] # Example range for Table 2

# Save each table to a new CSV for easier SQL import
table1.to_csv('table1.csv', index=False)
table2.to_csv('table2.csv', index=False)