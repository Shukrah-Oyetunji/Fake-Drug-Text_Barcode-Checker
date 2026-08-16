
# Fake Drug Text/ Barcode Checker

### 3MTT Capstone Project — Artificial Intelligence/Machine Learning NextGen

## Project Overview

The Fake Drug Text/ Barcode Checker is a machine learning and Streamlit-based application designed to assist in the verification of pharmaceutical products using their barcode.

The system allows a user to enter a 13-digit drug barcode, retrieve the corresponding drug information from a database, and obtain an AI-based prediction indicating whether the drug is classified as **Fake** or **Not Fake**.

The machine learning uses XGBoost as the final classification model.

> **Note:** The original pharmaceutical dataset used in this project was obtained from an NDC (National Drug Code) data source. However, the available dataset did not contain all the fields required for this project, particularly barcode information and drug verification status (Fake/Not Fake). Synthetic data was introduced for these attributes to enable development of the verification workflow. This approach was adopted because access to comprehensive real-world pharmaceutical authentication datasets is restricted by security, regulatory, privacy, and ethical considerations.

--- 
## Project Objectives

The objectives of this project are to:

- Develop a barcode-based drug checker system.
- Build a machine learning model for Fake/Not Fake classification.
- Explore and preprocess pharmaceutical product data.
- Compare different machine learning models.
- Develop a user-friendly Streamlit interface.

## Program

This project was developed as a **Capstone Project for the 3 Million Technical Talent (3MTT) Programme**, as part of the practical application of Artificial Intelligence and Machine Learning skills acquired during the program.

---

##  Technologies Used

- **Python**
- **Pandas & NumPy** — Data processing
- **Matplotlib** — Data visualization
- **Scikit-learn** — Machine learning and evaluation
- **XGBoost** — Final classification model
- **Imbalanced-learn (SMOTE)** — Class imbalance handling
- **Streamlit** — Web application
- **Joblib** — Save Model
- **Jupyter Notebook & VS Code** — Development
- **Python Virtual Environment**

## Dataset

The dataset contains **137,469 records and 15 features**, including:

- Barcode
- Product NDC
- Generic Name
- Manufacturer
- Brand Name
- Dosage Form
- Product Type
- Route
- Marketing Start Date
- Product ID
- Batch Number
- Manufacture Date
- Expiry Date
- Verification Status

The target variable contains:

```text
Not Fake — 80%
Fake     — 20%
```

---

## Machine Learning workflow
```text
Data Collection
      ↓
Data Preparation
      ↓
Exploratory Data Analysis
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Encoding
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Prediction Pipeline
      ↓
Streamlit Application

```
---
## Model Comparison
Several Models were evaluated

| Model                   |   Accuracy |  Precision |     Recall |   F1 Score |
| ----------------------- | ---------: | ---------: | ---------: | ---------: |
| Baseline Random Forest  |     74.77% |     19.94% |      8.67% |     12.09% |
| Random Forest – Model 2 |     63.12% |     19.68% |     27.39% |     22.90% |
| Random Forest + SMOTE   |     67.08% |     19.34% |     20.39% |     19.85% |
| XGBoost                 |     53.27% |     20.04% |     44.68% |     27.67% |
| **Tuned XGBoost**       | **51.59%** | **20.15%** | **47.94%** | **28.37%** |

### Final Model
**Tuned XGBoost** was selected because the project places greater emphasis on identifying the Fake class.
Although its overall accuracy was lower, it achieved the highest Fake-class recall (47.94%) and F1-score (28.37%) among the evaluated models.
---

## Application
The Streamlit application allows users to:
- Enter a 13-digit barcode.
- Validate the barcode.
- Search the drug database.
- View drug information.
- Generate an AI prediction.
- View prediction confidence.

Run the application with:
streamlit run app.py

---
## Project Structure

```text
Fake Drug Barcode Checker/
│
├── data/
│   ├── drugs.csv
│   ├── drugs_with_barcodes.csv
│   └── processed_barcode_data.csv
│
├── models/
│   ├── drug_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── fake_drug_text.ipynb
│   ├── model_training.ipynb
│   └── xgboost_training.ipynb
|
├── app.py
├── predict.py
├── convert_json_to_csv.py
├── Updated_dataset.py
├── requirements.txt
└── .gitignore
```

## Installation

cd Fake-Drug-Barcode-Checker

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

## Limitations
The Fake/Not Fake labels were synthetically generated because verified counterfeit-drug datasets containing barcode information are difficult to obtain due to security, regulatory, and ethical considerations.

Therefore, the model should not be used as the sole method for determining whether a real pharmaceutical product is genuine or counterfeit.

### Future improvements could include:

- Verified real-world counterfeit-drug datasets
- Real barcode
- Improved model calibration and validation
- Image-based packaging analysis

**StreamLit Web Application:**  https://shukrah-oyetunji-fake-drug-text-barcode-checker-app-q5bgz2.streamlit.app/