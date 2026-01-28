import streamlit as st
import pandas as pd
import os
from datetime import datetime

CONTACT_FILE = "contact_messages.csv"


def init_contact_file():
    if not os.path.exists(CONTACT_FILE):
        pd.DataFrame(columns=["name", "email", "message", "time"]).to_csv(
            CONTACT_FILE, index=False
        )


def render():
    init_contact_file()

    st.title("Contact Us")
    st.write("Have a question or feedback? Send us a message 👇")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=120)

    if st.button("Send Message"):
        if not name or not email or not message:
            st.error("❌ Please fill all fields")
            return

        # Save message locally
        df = pd.read_csv(CONTACT_FILE)
        df.loc[len(df)] = [name, email, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        df.to_csv(CONTACT_FILE, index=False)

        st.success("✅ Message sent successfully! We will contact you soon.")
