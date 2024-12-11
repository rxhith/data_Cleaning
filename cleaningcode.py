import pandas as pd

# Load data from the CSV file
input_file = "task 3 + verbose - Sheet1.csv"  # Replace with your input CSV file path
output_file = "cleaned_total.csv"  # Replace with your desired output file path

# Define allowed capabilities and consequences (case-insensitive)
allowed_capabilities = [
    "Identity and Access Management",
    "Secure Edge Access",
    "Resilience Exercises",
    "Security Operations Oversight",
    "Data Sensitivity Scheme",
]
allowed_consequences = [
    "Low-Quality Product",
    "Reputation Hit",
    "Ransom",
    "Pervasive Visibility",
    "Third-Party Failure",
]

# Read the CSV file
df = pd.read_csv(input_file)

# Ensure case-insensitivity by converting to lowercase for comparison
df["capability_lower"] = df["capability"].str.lower()
df["consequence_lower"] = df["consequence"].str.lower()

allowed_capabilities_lower = [cap.lower() for cap in allowed_capabilities]
allowed_consequences_lower = [cons.lower() for cons in allowed_consequences]

# Filter out invalid capabilities and consequences
invalid_rows = df[
    ~df["capability_lower"].isin(allowed_capabilities_lower) | 
    ~df["consequence_lower"].isin(allowed_consequences_lower)
]
valid_df = df[
    df["capability_lower"].isin(allowed_capabilities_lower) & 
    df["consequence_lower"].isin(allowed_consequences_lower)
]

# Remove rows where the same control_name has multiple capabilities or consequences
duplicates = valid_df.groupby('control_name').filter(lambda x: x[['capability', 'consequence']].nunique().sum() > 2)
cleaned_df = valid_df[~valid_df['control_name'].isin(duplicates['control_name'])]

# Drop the temporary lowercase columns
cleaned_df = cleaned_df.drop(columns=["capability_lower", "consequence_lower"])
invalid_rows = invalid_rows.drop(columns=["capability_lower", "consequence_lower"])

# Save the cleaned data to a new CSV file
cleaned_df.to_csv(output_file, index=False)

# Generate statistics
stats = {
    "Total Rows in Original Data": len(df),
    "Rows with Invalid Capabilities or Consequences": len(invalid_rows),
    "Rows Removed Due to Duplicate Control Names": len(valid_df) - len(cleaned_df),
    "Total Rows in Cleaned Data": len(cleaned_df),
}

# Print statistics
print("Statistics:")
for key, value in stats.items():
    print(f"- {key}: {value}")

print(f"Cleaned data saved to {output_file}")
