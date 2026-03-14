# Disease Prediction System

A machine learning-based web application for predicting multiple diseases (Diabetes, Heart Disease, Kidney Disease, and Hypertension) using user input data and trained models.

## Features
- Predicts risk for Diabetes, Heart Disease, Kidney Disease, and Hypertension
- User-friendly web interface (Streamlit)
- Trained models using scikit-learn and XGBoost
- Modular code structure for easy maintenance

## Project Structure
```
├── app/
│   ├── analytics.py
│   ├── database.py
│   ├── login.py
│   ├── main.py
│   └── prediction.py
├── dataset/
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── hypertension.csv
│   └── kidney.csv
├── models/
├── requirements.txt
├── train_models.py
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/multiple-disease-prediction.git
   cd multiple-disease-prediction
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix/Mac
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Train the models:
   ```bash
   python train_models.py
   ```
5. Run the web app:
   ```bash
   streamlit run app/main.py
   ```

## Usage
- Open the Streamlit app in your browser as instructed in the terminal.
- Enter the required medical data for prediction.
- View the prediction results for each disease.

## License
This project is licensed under the MIT License.
