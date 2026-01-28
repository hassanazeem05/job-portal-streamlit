import streamlit as st

def render():
    st.title("💼 Career")
    st.subheader("Select a Department")

    col1, col2, col3 = st.columns(3)

    if col1.button("IT Department", key="dept_it"):
        st.session_state.department = "IT"
        st.session_state.page = "Jobs"
        st.rerun()

    if col2.button("Government Department", key="dept_gov"):
        st.session_state.department = "Government"
        st.session_state.page = "Jobs"
        st.rerun()

    if col3.button("Federal Department", key="dept_fed"):
        st.session_state.department = "Federal"
        st.session_state.page = "Jobs"
        st.rerun()
