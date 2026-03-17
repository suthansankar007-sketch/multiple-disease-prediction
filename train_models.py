import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


# ===============================
# Create models folder
# ===============================
os.makedirs("models", exist_ok=True)

# ===============================
# Diabetes Model
# ===============================


print("Training Diabetes Model...")


diabetes = pd.read_csv("dataset/diabetes.csv.csv")
# Encode 'Gender' column: Female=0, Male=1
if 'Gender' in diabetes.columns:
    diabetes['Gender'] = diabetes['Gender'].map({'Female': 0, 'Male': 1})
# Drop rows where Outcome is NaN
diabetes = diabetes.dropna(subset=["Outcome"]) 

X = diabetes.drop("Outcome", axis=1)
y = diabetes["Outcome"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

diabetes_model = RandomForestClassifier(n_estimators=200)

diabetes_model.fit(X_train,y_train)

pred = diabetes_model.predict(X_test)

print("Diabetes Accuracy:",accuracy_score(y_test,pred))

pickle.dump(diabetes_model,open("models/diabetes_model.pkl","wb"))


# ===============================
# Heart Disease Model
# ===============================


print("Training Heart Model...")

heart = pd.read_csv("dataset/heart.csv.csv")
# If there are any non-numeric columns, encode or drop them
for col in heart.columns:
    if heart[col].dtype == 'object':
        heart[col] = heart[col].astype('category').cat.codes
# Drop rows with any NaN values
heart = heart.dropna()
X = heart.drop("target", axis=1)
y = heart["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
heart_model = LogisticRegression(max_iter=1000)
heart_model.fit(X_train, y_train)
pred = heart_model.predict(X_test)
print("Heart Accuracy:", accuracy_score(y_test, pred))
pickle.dump(heart_model, open("models/heart_model.pkl", "wb"))


# ===============================
# Kidney Disease Model
# ===============================


print("Training Kidney Model...")



kidney = pd.read_csv("dataset/kidney.csv.csv")
# Drop columns with >80% missing values, but always keep 'classification'
missing_percent = kidney.isnull().sum() / len(kidney) * 100
cols_to_drop = [col for col in missing_percent.index if missing_percent[col] > 80 and col != 'classification']
kidney = kidney.drop(columns=cols_to_drop)
# Encode non-numeric columns if any
for col in kidney.columns:
    if kidney[col].dtype == 'object':
        kidney[col] = kidney[col].astype('category').cat.codes
# Drop remaining rows with any NaN values
kidney = kidney.dropna()
# Remove rows where classification == -1
kidney = kidney[kidney['classification'] != -1]
X = kidney.drop("classification", axis=1)
y = kidney["classification"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
kidney_model = XGBClassifier()
kidney_model.fit(X_train, y_train)
pred = kidney_model.predict(X_test)
print("Kidney Accuracy:", accuracy_score(y_test, pred))
pickle.dump(kidney_model, open("models/kidney_model.pkl", "wb"))


# ===============================
# Hypertension Model
# ===============================


print("Training Hypertension Model...")



hyper = pd.read_csv("dataset/hypertension.csv.csv")
# Drop columns with >80% missing values, but always keep 'Hypertension'
missing_percent = hyper.isnull().sum() / len(hyper) * 100
cols_to_drop = [col for col in missing_percent.index if missing_percent[col] > 80 and col != 'Hypertension']
hyper = hyper.drop(columns=cols_to_drop)
# Encode non-numeric columns if any
for col in hyper.columns:
    if hyper[col].dtype == 'object':
        hyper[col] = hyper[col].astype('category').cat.codes
# Drop rows with any NaN values
hyper = hyper.dropna()
X = hyper.drop("Hypertension", axis=1)
y = hyper["Hypertension"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
hyper_model = RandomForestClassifier(n_estimators=150)
hyper_model.fit(X_train, y_train)
pred = hyper_model.predict(X_test)
print("Hypertension Accuracy:", accuracy_score(y_test, pred))
pickle.dump(hyper_model, open("models/hypertension_model.pkl", "wb"))


print("\n✅ All models trained and saved successfully")
