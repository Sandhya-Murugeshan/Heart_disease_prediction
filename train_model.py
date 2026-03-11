import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
data = pd.read_csv("heart.csv")

# Rename columns to match your app
data.rename(columns={
    "chest_pain_type":"cp",
    "resting_blood_pressure":"trestbps",
    "cholestoral":"chol",
    "fasting_blood_sugar":"fbs",
    "rest_ecg":"restecg",
    "Max_heart_rate":"thalach",
    "exercise_induced_angina":"exang",
    "vessels_colored_by_flourosopy":"ca",
    "thalassemia":"thal"
}, inplace=True)

# -------- Encode categorical columns using LabelEncoder --------
categorical_cols = ["sex","cp","fbs","restecg","exang","slope","ca","thal"]
encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le  # save encoder for app

# Split features and target
X = data.drop("target", axis=1)
y = data["target"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("heart_model.pkl","wb"))

# Save encoders
pickle.dump(encoders, open("encoders.pkl","wb"))

print("✅ Model and encoders saved successfully!")