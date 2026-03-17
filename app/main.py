import streamlit as st
from prediction import predict_diabetes,predict_heart,predict_kidney,predict_hyper

st.title("Multiple Disease Prediction System")

option = st.sidebar.selectbox(
    "Select Disease",
    ["Diabetes","Heart Disease","Kidney Disease","Hypertension"]
)

if option=="Diabetes":

    st.header("Diabetes Prediction")

    pregnancies = st.number_input("Pregnancies")
    glucose = st.number_input("Glucose")
    bp = st.number_input("Blood Pressure")
    skin = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI")
    dpf = st.number_input("Diabetes Pedigree Function")
    age = st.number_input("Age")

    if st.button("Predict"):
        result = predict_diabetes([pregnancies,glucose,bp,skin,insulin,bmi,dpf,age])
        st.success(result)


elif option=="Heart Disease":

    st.header("Heart Disease Prediction")

    age = st.number_input("Age")
    chol = st.number_input("Cholesterol")
    bp = st.number_input("Blood Pressure")

    if st.button("Predict"):
        result = predict_heart([age,chol,bp])
        st.success(result)


elif option=="Kidney Disease":

    st.header("Kidney Disease Prediction")

    bp = st.number_input("Blood Pressure")
    sugar = st.number_input("Blood Sugar")

    if st.button("Predict"):
        result = predict_kidney([bp,sugar])
        st.success(result)


elif option=="Hypertension":

    st.header("Hypertension Prediction")

    age = st.number_input("Age")
    bmi = st.number_input("BMI")

    if st.button("Predict"):
        result = predict_hyper([age,bmi])
        st.success(result)
