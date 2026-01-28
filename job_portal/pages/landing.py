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

    else:
        st.error(f"Background image not found: {img_path}")

    st.markdown(
        "<h1 style='text-align:center; color:white;'>Job Portal System</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center; color:white;'>Find your dream career</h3>",
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Get Started"):
            st.session_state.show_auth = True
            st.session_state.auth_page = "login"
            st.rerun()
