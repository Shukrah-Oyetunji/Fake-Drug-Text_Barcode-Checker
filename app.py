import streamlit as st
from predict import predict_drug

# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Fake Drug Barcode Checker",
    page_icon=":material/pill:",
    layout="centered"
)

# Application Title
# --------------------------------------------------

st.title(":material/pill: Fake Drug Barcode Checker")

st.write(
    "Enter a drug barcode number to verify the drug information "
    "and obtain an AI-based prediction."
)
# Barcode Input
# --------------------------------------------------

barcode = st.text_input(
    "Enter 13-Digit Barcode",
    placeholder= "e.g. 8901234567000"
)

# Verify Button
# --------------------------------------------------

if st.button(":material/search: Verify Drug"):


    if not barcode:
        st.warning("Please enter a barcode.")

    elif not barcode.isdigit():
        st.error("Please enter numbers only.")

    elif len(barcode) != 13:
        st.error("Barcode must contain exactly 13 digits.")

    else:

        with st.spinner("Checking drug..."):

            result = predict_drug(barcode)

        # Barcode Not Found
        # --------------------------------------------------

        if not result["found"]:

            st.error(":material/cancel: Barcode not found in the database.")

            st.info(
                "The drug could not be found in the current database."
            )


        # --------------------------------------------------
        # Drug Found
        # --------------------------------------------------

        else:

            st.success(":material/verified: Drug found in database.")

            st.subheader("Drug Information")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Barcode:**", result["barcode"])
                st.write("**Generic Name:**", result["generic_name"])
                st.write("**Brand Name:**", result["brand_name"])
                st.write("**Manufacturer:**", result["manufacturer"])
                st.write("**Dosage Form:**", result["dosage_form"])

            with col2:

                st.write("**Product Type:**", result["product_type"])
                st.write("**Route:**", result["route"])
                st.write("**Batch Number:**", result["batch_number"])
                st.write(
                    "**Manufacture Date:**",
                    result["manufacture_date"]
                )
                st.write(
                    "**Expiry Date:**",
                    result["expiry_date"]
                )


            # Prediction
            # --------------------------------------------------

            st.subheader("AI Verification Result")

            if result["prediction"] == "Fake":

                st.error(":material/warning: Prediction: FAKE")

            else:

                st.success(":material/verified: Prediction: NOT FAKE")


            st.write(
                f"**Model Confidence:** {result['confidence']:.2f}%"
            )