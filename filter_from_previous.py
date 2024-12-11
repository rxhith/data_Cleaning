import pandas as pd

# Load the two CSV files

first_csv = pd.read_csv("E:\Optim\data cleaning pipeline\day1_2 - Sheet1.csv")
second_csv = pd.read_csv("cleaned_total.csv")
# Specify the columns for comparison (shared between both CSVs)
comparison_columns = ["control_name", "capability", "consequence"]

# Ensure column names are consistent (strip spaces)
first_csv.rename(columns=lambda x: x.strip(), inplace=True)
second_csv.rename(columns=lambda x: x.strip(), inplace=True)

# Check if the necessary columns exist in both files
if not all(col in first_csv.columns for col in comparison_columns):
    raise KeyError(f"Missing columns in first CSV: {set(comparison_columns) - set(first_csv.columns)}")
if not all(col in second_csv.columns for col in comparison_columns):
    raise KeyError(f"Missing columns in second CSV: {set(comparison_columns) - set(second_csv.columns)}")

# Remove rows in second_csv that match rows in first_csv based on the shared columns
filtered_second_csv = second_csv[~second_csv[comparison_columns].apply(tuple, axis=1).isin(first_csv[comparison_columns].apply(tuple, axis=1))]

# Save the filtered second CSV to a new file
filtered_second_csv.to_csv(r"filtered_second.csv", index=False)

print("Rows removed based on specified columns and new file 'filtered_second.csv' created.")


