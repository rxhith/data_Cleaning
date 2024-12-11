import pandas as pd

# Load the CSV file
file_name = "E:\\data cleaning\\filtered_second.csv"  # Ensure this file exists in the same directory as the script
data = pd.read_csv(file_name)

# Drop the 'id' column
data = data.drop(columns=['id'])

# Save the cleaned data to an Excel file
output_file_name = "cleaned_data_final.xlsx"
data.to_excel(output_file_name, index=False)

print(f"File saved as '{output_file_name}'.")
