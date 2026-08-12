import pandas as pd
from datetime import datetime, timedelta
import random

# Load the original CSV
df = pd.read_csv("data/drugs.csv")

# Rename labeler_name to manufacturer
df.rename(columns={"labeler_name": "manufacturer"}, inplace=True)

# -----------------------------
# Randomly Generate 13 digits Barcode
# -----------------------------
start_barcode = 8901234567000
df.insert(
    0,
    "barcode",
    [str(start_barcode + i) for i in range(len(df))]
)

# -----------------------------
# Generate Batch Number
# -----------------------------
df["batch_number"] = [
    f"BN{str(i + 1).zfill(6)}"
    for i in range(len(df))
]

# -----------------------------
# Generate Manufacture Date
# (Random date between 2023 and 2025)
# -----------------------------
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)

manufacture_dates = []

for _ in range(len(df)):
    random_days = random.randint(0, (end_date - start_date).days)
    mfg_date = start_date + timedelta(days=random_days)
    manufacture_dates.append(mfg_date)

df["manufacture_date"] = manufacture_dates

# -----------------------------
# Generate Expiry Date
# (3 years after manufacture)
# -----------------------------
df["expiry_date"] = [
    date + timedelta(days=365 * 3)
    for date in manufacture_dates
]

# Format dates as YYYY-MM-DD
df["manufacture_date"] = df["manufacture_date"].dt.strftime("%Y-%m-%d")
df["expiry_date"] = df["expiry_date"].dt.strftime("%Y-%m-%d")

# -----------------------------
# Verification Status
# -----------------------------
# Initially mark every record as Not Fake
df["verification_status"] = "Not Fake"

# Randomly select 20% of the dataset
fake_percentage = 0.20
fake_indices = df.sample(frac=fake_percentage, random_state=42).index

# Mark them as Fake
df.loc[fake_indices, "verification_status"] = "Fake"

# Save the Updated dataset
df.to_csv("data/drugs_with_barcodes.csv", index=False)

print("Dataset enhanced successfully!")
print(f"Total records: {len(df)}")
print(df.head())