# ❤️ Heart Disease Prediction Web App

A Machine Learning based web application that predicts the likelihood of heart disease using patient health parameters. The application is built using **Python**, **Scikit-learn**, and **Streamlit** to provide an interactive interface for users to input medical data and receive predictions instantly.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in taking preventive measures.  
This project uses a **Random Forest Classifier** trained on heart disease data to predict whether a person is at risk.

Users can enter medical details such as age, cholesterol level, blood pressure, and other health indicators. The model then analyzes the input and predicts the presence or absence of heart disease.

---

## 🚀 Features

- Interactive **Streamlit web interface**
- Real-time heart disease prediction
- Machine learning model using **Random Forest**
- Encoders for handling categorical features
- Model and encoders saved using **Pickle**
- Simple and user-friendly UI

---

## 🛠 Technologies Used

- **Python** – Model training and application logic  
- **Scikit-learn** – Machine learning algorithms and preprocessing  
  - RandomForestClassifier  
  - LabelEncoder  
- **Streamlit** – Web application interface  
- **Pandas** – Data manipulation and analysis  
- **NumPy** – Numerical computations  
- **Pickle** – Saving and loading trained models and encoders  

---

## 📂 Project Structure

```
heart-disease-prediction/
│
├── app.py                # Streamlit web application
├── model.pkl             # Trained machine learning model
├── encoder.pkl           # Saved label encoders
├── heart.csv             # Dataset
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation
```
---

## 🖥️ Application Screenshots

### Home Page
<img width="1920" height="1080" alt="Output1" src="https://github.com/user-attachments/assets/88616228-3861-4bda-83d6-43cc85c7374a" />

### Input Form
<img width="1920" height="1080" alt="Output2" src="https://github.com/user-attachments/assets/6a402bba-d82f-4c62-833a-dc620d0e7e54" />

### Prediction Result
<img width="1920" height="1080" alt="Output3" src="https://github.com/user-attachments/assets/3ff83ef2-2c1c-434b-a6eb-e1e25c4f59f5" />

### Additional Output
<img width="1920" height="1080" alt="Output4" src="https://github.com/user-attachments/assets/c0b84b18-3c46-44b7-83f1-1e4dd2de82f7" />

---

## 📊 Machine Learning Model

The prediction model is built using **Random Forest Classifier**, which combines multiple decision trees to improve prediction accuracy and reduce overfitting.

**Steps involved:**
1. Data preprocessing
2. Encoding categorical variables
3. Training the Random Forest model
4. Saving the trained model using Pickle
5. Integrating the model with the Streamlit application

---

## 🎯 Future Improvements

- Deploy the application using **Streamlit Cloud / Heroku / AWS**
- Add more medical datasets for better accuracy
- Include data visualization for health metrics
- Improve UI/UX design

---
