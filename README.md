# 🩺 Symptom-Based Disease Prediction App

A machine learning-powered web app that predicts possible diseases based on user-reported symptoms. Built using **Random Forest**, **scikit-learn**, and **Streamlit**, this application helps with early and accessible disease identification.

---

## 🚀 Live Demo

👉 [Launch the App](https://thxrunn-symptom-disease-predictor-disease-predictor-app-qpk6mi.streamlit.app/)  


---

## 📌 Features

- 🔍 Predicts disease based on selected symptoms
- 🧠 Trained using Random Forest Classifier with high accuracy
- 💡 Supports 100+ symptoms and 40+ medical conditions
- 📊 Shows model performance using classification metrics
- 🌐 Interactive Streamlit-based UI for real-time predictions

---

## 📂 Dataset Overview

The project uses the following files:
- `dataset.csv`: Symptom-to-disease training data  
- `symptom_description.csv`: Description of each symptom  
- `symptom_precaution.csv`: Preventive steps for each disease  


---

## ⚙️ Tech Stack

- **Python**  
- **scikit-learn**  
- **pandas**, **numpy**  
- **Streamlit**

---

## 📈 Model Performance

- **Model**: Random Forest Classifier  
- **Accuracy**: 100% on test data (due to clean synthetic dataset)  
- **Metrics**:  
  - Precision: 1.00  
  - Recall: 1.00  
  - F1 Score: 1.00  

---

## 🧪 How to Use

1. Select your symptom from the dropdown
2. Click **Predict**
3. The model suggests the most probable disease

---

## 💻 Run Locally

```bash
# Clone the repository
git clone https://github.com/Thxrunn/Symptom_disease_predictor.git
cd Symptom_disease_predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run disease_predictor_app.py

🌱 Future Enhancements
🔄 Allow multiple symptom input

📉 Add severity-based risk scoring

🌡️ Visualize symptom intensity trends

📡 Integrate with real-world healthcare datasets (WHO, CDC, etc.)

👤 Author
Tharun Kumar Malla Dinakaran
📧 [tharundina@gmail.com]
