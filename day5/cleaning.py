import pandas as pd

# Define valid values for capabilities and consequences
valid_capabilities = [
    "user training",
    "supply chain risk management",
    "role clarity",
    "bc/dr plan",
    "metrics and measurement",
    "edr/xdr"
]

valid_consequences = [
    "data loss",
    "ip theft",
    "low quality product",
    "ot-iot failure",
    "pervasive visibility",
    "physically exposed",
    "privacy breach",
    "ransom",
    "reputation hit",
    "resource theft",
    "service degradation",
    "third-party failure"
]

# Load the CSV file
input_file = "E:\\Optim\\optim\\modified_cleaning_code\\day5 raw - Sheet1.csv"  # Replace with your input file name
output_file = "filtered_output.csv"

data = pd.read_csv(input_file)

# Normalize columns by stripping whitespace and converting to lowercase
data["capability"] = data["capability"].str.strip().str.lower()
data["consequence"] = data["consequence"].str.strip().str.lower()

# Filter rows based on valid capabilities and consequences
valid_data = data[
    (data["capability"].isin(valid_capabilities)) &
    (data["consequence"].isin(valid_consequences))
]

# Drop rows where the same control_name has multiple capabilities or consequences
duplicated_controls = valid_data.groupby("control_name").filter(
    lambda x: x["capability"].nunique() > 1 or x["consequence"].nunique() > 1
)

# Remove invalid rows from the dataset
valid_data = valid_data.drop(duplicated_controls.index)

# Drop duplicate rows
unique_data = valid_data.drop_duplicates()

# Save the filtered data to a new CSV file
unique_data.to_csv(output_file, index=False)

# Print statistics
print("Original rows:", len(data))
print("Rows after filtering valid capabilities and consequences:", len(valid_data))
print("Rows after removing duplicates:", len(unique_data))
print("Rows dropped:", len(data) - len(unique_data))

print(f"Filtered data saved to '{output_file}'")

# Generate statistics for the number of controls per capability
capability_counts = unique_data["capability"].value_counts()
print("\nNumber of controls generated for each capability:")
print(capability_counts)

# Generate statistics for the number of controls per consequence
consequence_counts = unique_data["consequence"].value_counts()
print("\nNumber of controls generated for each consequence:")
print(consequence_counts)

print(f"Filtered data saved to '{output_file}'")
