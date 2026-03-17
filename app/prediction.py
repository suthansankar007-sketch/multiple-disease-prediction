import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier

os.makedirs("models", exist_ok=True)

data = pd.read_csv("dataset/diabetes.csv")

# BMI create
data['BMI'] = data['Weight'] / ((data['Height']/100) ** 2)

# ---------------- Diabetes ----------------
X = data[['Age','BMI','BP','Sugar','Cholesterol']]
y = data['Diabetes']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/diabetes_model.pkl", "wb"))

# ---------------- Heart ----------------
X = data[['Age','Cholesterol','BP']]
y = data['Heart']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/heart_model.pkl", "wb"))

# ---------------- Kidney ----------------
X = data[['Age','BP','Sugar']]
y = data['Kidney']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/kidney_model.pkl", "wb"))

# ---------------- Hypertension ----------------
X = data[['Age','BMI','BP']]
y = data['Hyper']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("models/hyper_model.pkl", "wb"))

print("All models trained successfully!")
