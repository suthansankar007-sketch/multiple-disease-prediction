import pickle

diabetes_model = pickle.load(open("models/diabetes_model.pkl", "rb"))
heart_model = pickle.load(open("models/heart_model.pkl", "rb"))
kidney_model = pickle.load(open("models/kidney_model.pkl", "rb"))
hyper_model = pickle.load(open("models/hyper_model.pkl", "rb"))

def predict_diabetes(data):
    return "Diabetes Detected" if diabetes_model.predict([data])[0] else "No Diabetes"

def predict_heart(data):
    return "Heart Disease Detected" if heart_model.predict([data])[0] else "No Heart Disease"

def predict_kidney(data):
    return "Kidney Disease Detected" if kidney_model.predict([data])[0] else "No Kidney Disease"

def predict_hyper(data):
    return "Hypertension Detected" if hyper_model.predict([data])[0] else "No Hypertension"
