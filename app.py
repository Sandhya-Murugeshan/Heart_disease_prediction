import streamlit as st
import numpy as np
import pickle

# --- Set background image ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://wallpapercave.com/wp/wp11622738.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        filter: brightness(0.85);  /* makes the background slightly faded */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Load trained model and encoders
model = pickle.load(open("heart_model.pkl","rb"))
encoders = pickle.load(open("encoders.pkl","rb"))

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient medical details")

# -------- INPUT FIELDS --------
age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", ["Male","Female"])
cp = st.selectbox(
    "Chest Pain Type",
    ["Typical angina","Atypical angina","Non-anginal pain","Asymptomatic"]
)
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol Level")
fbs = st.selectbox("Fasting Blood Sugar", ["Lower than 120 mg/ml", "Higher than 120 mg/ml"])
restecg = st.selectbox(
    "Rest ECG Result",
    ["Normal","ST-T wave abnormality","Left ventricular hypertrophy"]
)
thalach = st.number_input("Maximum Heart Rate")
exang = st.selectbox("Exercise Induced Angina", ["No","Yes"])
oldpeak = st.number_input("ST Depression")
slope = st.selectbox("Slope", ["Upsloping","Flat","Downsloping"])
ca = st.selectbox("Number of Major Vessels", ["Zero","One","Two","Three"])
thal = st.selectbox("Thalassemia", ["Normal","Fixed defect","Reversable Defect"])

# -------- Encode inputs using saved LabelEncoders --------
sex = encoders["sex"].transform([sex])[0]
cp = encoders["cp"].transform([cp])[0]
fbs = encoders["fbs"].transform([fbs])[0]
restecg = encoders["restecg"].transform([restecg])[0]
thalach = int(thalach)
exang = encoders["exang"].transform([exang])[0]
oldpeak = float(oldpeak)
slope = encoders["slope"].transform([slope])[0]
ca = encoders["ca"].transform([ca])[0]
thal = encoders["thal"].transform([thal])[0]

# -------- PREDICTION --------
if st.button("Predict Heart Disease"):
    user_data = np.array([[age,sex,cp,trestbps,chol,fbs,
                           restecg,thalach,exang,oldpeak,
                           slope,ca,thal]])
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease. Please consult a doctor.")
    else:
        st.success("✅ Low Risk of Heart Disease. Stay healthy!")