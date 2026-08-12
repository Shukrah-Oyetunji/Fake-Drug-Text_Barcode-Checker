# Prediction Pipeline
#------------------------------------------
import pandas as pd
import joblib

# Load Model and Feature Columns
# --------------------------------------------------

MODEL_PATH = "models/drug_model.pkl"
FEATURES_PATH = "models/feature_columns.pkl"
DATA_PATH = "data/drugs_with_barcodes.csv"

# Read data, Model and Feature Columns
# --------------------------------------------------

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)

df = pd.read_csv(DATA_PATH)

# Prediction Function
# --------------------------------------------------

def predict_drug(barcode):

    # Convert barcode to string and remove unnecessary space from the begining and end
    barcode = str(barcode).strip()

    # Search for barcode
    drug = df[df["barcode"].astype(str) == barcode]

    # Check if barcode exists
    if drug.empty:
        return {
            "found": False,
            "message": "Barcode not found in the database."
        }

    # Get the first matching record
    drug_record = drug.iloc[0]

    # Prepare data for ML prediction
    # --------------------------------------------------

    X_new = drug.drop(
        columns=["verification_status"],
        errors="ignore"
    ).copy()

    # Remove identifier columns
    identifier_columns = [
        "barcode",
        "product_id",
        "batch_number"
    ]

    X_new = X_new.drop(
        columns=identifier_columns,
        errors="ignore"
    )

    # One-Hot Encoding
    # --------------------------------------------------

    categorical_columns = [
        "generic_name",
        "manufacturer",
        "brand_name",
        "dosage_form",
        "product_type",
        "route"
    ]

    X_new = pd.get_dummies(
        X_new,
        columns=[
            col for col in categorical_columns
            if col in X_new.columns
        ],
        drop_first=True,
        dtype=int
    )
    # Make columns match training data
    # --------------------------------------------------

    X_new = X_new.reindex(
        columns=feature_columns,
        fill_value=0
    )
    
    # Make Prediction
    # --------------------------------------------------

    prediction = model.predict(X_new)[0]

    # Get probability
    probabilities = model.predict_proba(X_new)[0]

    confidence = probabilities[int(prediction)] * 100

    # Convert prediction to label
    if prediction == 1:
        status = "Fake"
    else:
        status = "Not Fake"

    # Return Results
    # --------------------------------------------------

    return {
        "found": True,
        "barcode": drug_record["barcode"],
        "generic_name": drug_record["generic_name"],
        "manufacturer": drug_record["manufacturer"],
        "brand_name": drug_record["brand_name"],
        "dosage_form": drug_record["dosage_form"],
        "product_type": drug_record["product_type"],
        "route": drug_record["route"],
        "batch_number": drug_record["batch_number"],
        "manufacture_date": drug_record["manufacture_date"],
        "expiry_date": drug_record["expiry_date"],
        "prediction": status,
        "confidence": round(confidence, 2)
    }

# Test 

if __name__ == "__main__":

    test_barcode = "8901234567000"

    result = predict_drug(test_barcode)

    print(result)