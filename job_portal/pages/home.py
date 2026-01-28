import streamlit as st
import base64
from pathlib import Path

def render(show_button=True):
    img_path = Path("assets/bg.jpg")

    if img_path.exists():
        with open(img_path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image:
                linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    st.title("Job Portal System")
    st.text(" This is your all in one job apply plateform.")
    st.text(" We have so many jobs for you in departments")
    st.text(" like IT, Government and Federal. you can choose which job you want ")

    st.rerun
