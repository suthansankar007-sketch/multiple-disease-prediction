import streamlit as st
from database import add_user, login_user, create_tables

create_tables()

def login_page():
    st.subheader("Login / Register")

    menu = ["Login", "Register"]
    choice = st.selectbox("Menu", menu)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Register":
        if st.button("Create Account"):
            add_user(username, password)
            st.success("Account created successfully!")

    elif choice == "Login":
        if st.button("Login"):
            result = login_user(username, password)
            if result:
                st.success(f"Welcome {username}")
                return username
            else:
                st.error("Invalid credentials")

    return None
