import streamlit as st

def render():
    st.title("📝 Job Application Form")

    with st.form("apply_form"):
        st.subheader("Personal Information")

        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Address")

        st.subheader("Payment Details (Challan)")

        acc_name = st.text_input("Account Holder Name")
        card = st.text_input("Card Number")
        expiry = st.text_input("Expiry Date (MM/YY)")
        cvv = st.text_input("CVV", type="password")

        submitted = st.form_submit_button("Submit Application")

        if submitted:
            st.success("Application submitted successfully!")
