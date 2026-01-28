import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* REMOVE global centering */
    
    /* Input fields */
    input[type="text"], input[type="password"] {
        max-width: 280px;
        margin: auto;
        display: block;
        height: 36px;
        font-size: 15px;
    }

    /* Buttons */
    div.stButton > button {
        max-width: 160px;
        margin: 12px auto;
        display: block;
    }

    /* Hide Streamlit footer */
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
