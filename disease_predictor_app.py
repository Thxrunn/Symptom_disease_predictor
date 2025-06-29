
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("dataset.csv")
desc_df = pd.read_csv("symptom_Description.csv")
precaution_df = pd.read_csv("symptom_precaution.csv")

# Clean and prepare symptom list
df = df.fillna("")
symptom_cols = df.columns[:-1]
all_symptoms = set()

for col in symptom_cols:
    all_symptoms.update(df[col].unique())

all_symptoms = sorted([s.lower().strip().replace(" ", "_") for s in all_symptoms if s != ""])

# One-hot encode function
def encode_input(symptoms_selected):
    return [1 if s in symptoms_selected else 0 for s in all_symptoms]

# Load and train model
@st.cache(allow_output_mutation=True)
def load_model():
    X = df.apply(lambda row: encode_input([str(s).lower().strip().replace(" ", "_") for s in row[:-1] if s]), axis=1, result_type="expand")
    X.columns = all_symptoms
    y = df['Disease']
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = load_model()

# Prediction logic
def predict_disease(symptoms_input):
    input_vector = encode_input(symptoms_input)
    prediction = model.predict([input_vector])[0]
    return prediction

def get_disease_info(disease_name):
    try:
        description = desc_df[desc_df['Disease'].str.lower() == disease_name.lower()]['Description'].values[0]
    except:
        description = "Description not available."
    try:
        row = precaution_df[precaution_df['Disease'].str.lower() == disease_name.lower()].iloc[0]
        precautions = [row[f'Precaution_{i}'] for i in range(1, 5) if pd.notna(row[f'Precaution_{i}'])]
    except:
        precautions = ["Precautions not available."]
    return description, precautions

# Streamlit app UI
st.title("🩺 Symptom-Based Disease Prediction App")
st.markdown("Enter your symptoms below to predict possible disease:")

selected_symptoms = st.multiselect("Select Symptoms", all_symptoms)

if st.button("Predict"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        prediction = predict_disease(selected_symptoms)
        description, precautions = get_disease_info(prediction)

        st.success(f"🩺 Predicted Disease: {prediction}")
        st.markdown(f"📖 **Description**: {description}")
        st.markdown("✅ **Precautions:**")
        for i, item in enumerate(precautions, 1):
            st.markdown(f"{i}. {item}")
