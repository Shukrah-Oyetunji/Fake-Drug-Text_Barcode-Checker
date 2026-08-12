import json
import pandas as pd

# JSON File Path

json_path = "data/drug-ndc-0001-of-0001.json"

#Laod JSON Data

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("JSON loaded successfully!")

# Check JSON contains a "results" section
df = pd.DataFrame(data["results"])

columns_to_keep = [
    "product_ndc",
    "generic_name",
    "labeler_name",
    "brand_name",
    "listing_expiration_date",
    "dosage_form",
    "product_type",
    "route",
    "marketing_start_date",
    "product_id"   
]

# Keeping only columns that exist
available_columns = [col for col in columns_to_keep if col in df.columns]
df = df[available_columns]

# Save data to CSV

df.to_csv("data/drugs.csv", index=False)

print(f"\nCSV file created successfully!")
print(f"Saved as: {"data/drugs.csv"}")
print(f"Number of records: {len(df)}")
print("\nFirst 5 records:")
print(df.head())