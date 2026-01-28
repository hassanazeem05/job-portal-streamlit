import streamlit as st
import pandas as pd
import os

USERS_FILE = "users.csv"


def init_users():
    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=["username", "password"]).to_csv(USERS_FILE, index=False)


def signup(username, password):
    if not username or not password:
        st.error("All fields are required")
        return

    users = pd.read_csv(USERS_FILE)

    if username in users["username"].values:
        st.error("User already exists")
    else:
        users.loc[len(users)] = [username, password]
        users.to_csv(USERS_FILE, index=False)
        st.success("Account created. Please login.")
        st.session_state.auth_page = "login"
        st.rerun()


def login(username, password):
    if not username or not password:
        st.error("All fields are required")
        return

    users = pd.read_csv(USERS_FILE)

    if ((users.username == username) & (users.password == password)).any():
        st.session_state.logged_in = True
        st.session_state.user = username
        st.session_state.show_auth = False
        st.session_state.page = "Home"
        st.rerun()
    else:
        st.error("Invalid credentials")
