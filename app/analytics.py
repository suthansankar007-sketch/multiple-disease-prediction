import streamlit as st
import pandas as pd
from database import get_predictions

def show_analytics(username):

    st.subheader("User Analytics")

    data = get_predictions(username)

    if not data:
        st.warning("No data available")
        return

    df = pd.DataFrame(data, columns=["Username", "Disease", "Result", "Date"])

    st.write("### Prediction History")
    st.dataframe(df)

    # Count by disease
    st.write("### Disease Count")
    disease_count = df["Disease"].value_counts()
    st.bar_chart(disease_count)

    # Result count
    st.write("### Result Distribution")
    result_count = df["Result"].value_counts()
    st.bar_chart(result_count)
