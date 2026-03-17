import streamlit as st
from prediction import predict_diabetes, predict_heart, predict_kidney, predict_hyper

st.title("Multiple Disease Prediction System")

option = st.sidebar.selectbox(
    "Select Disease",
    ["Diabetes", "Heart Disease", "Kidney Disease", "Hypertension"]
)

# ---------------- Diabetes ----------------
if option == "Diabetes":

    st.header("Diabetes Prediction")

    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female"])
    glucose = st.number_input("Sugar Level (Glucose)")
    chol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")
    bmi = st.number_input("BMI")

    gender_val = 1 if gender == "Male" else 0

    if st.button("Predict"):
        result = predict_diabetes([age, gender_val, glucose, chol, bp, bmi])
        st.success(result)

# ---------------- Heart ----------------
elif option == "Heart Disease":

    st.header("Heart Disease Prediction")

    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female"])
    chol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")

    gender_val = 1 if gender == "Male" else 0

    if st.button("Predict"):
        result = predict_heart([age, gender_val, chol, bp])
        st.success(result)

# ---------------- Kidney ----------------
elif option == "Kidney Disease":

    st.header("Kidney Disease Prediction")

    age = st.number_input("Age")
    sugar = st.number_input("Blood Sugar")
    bp = st.number_input("Blood Pressure")

    if st.button("Predict"):
        result = predict_kidney([age, sugar, bp])
        st.success(result)

# ---------------- Hypertension ----------------
elif option == "Hypertension":

    st.header("Hypertension Prediction")

    age = st.number_input("Age")
    bmi = st.number_input("BMI")
    bp = st.number_input("Blood Pressure")

    if st.button("Predict"):
        result = predict_hyper([age, bmi, bp])
        st.success(result)
