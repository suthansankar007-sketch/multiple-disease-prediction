
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
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
    glucose = st.number_input("Sugar Level")
    chol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")

    bmi = weight / ((height/100) ** 2) if height > 0 else 0
    st.write(f"BMI: {bmi:.2f}")

    if st.button("Predict"):
        result = predict_diabetes([age, bmi, bp, glucose, chol])
        st.success(result)

# ---------------- Heart ----------------
elif option == "Heart Disease":

    st.header("Heart Disease Prediction")

    age = st.number_input("Age")
    chol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")

    if st.button("Predict"):
        result = predict_heart([age, chol, bp])
        st.success(result)

# ---------------- Kidney ----------------
elif option == "Kidney Disease":

    st.header("Kidney Disease Prediction")

    age = st.number_input("Age")
    bp = st.number_input("Blood Pressure")
    sugar = st.number_input("Blood Sugar")

    if st.button("Predict"):
        result = predict_kidney([age, bp, sugar])
        st.success(result)

# ---------------- Hypertension ----------------
elif option == "Hypertension":

    st.header("Hypertension Prediction")

    age = st.number_input("Age")
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
    bp = st.number_input("Blood Pressure")

    bmi = weight / ((height/100) ** 2) if height > 0 else 0
    st.write(f"BMI: {bmi:.2f}")

    if st.button("Predict"):
        result = predict_hyper([age, bmi, bp])
        st.success(result)
