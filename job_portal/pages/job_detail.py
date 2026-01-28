import streamlit as st

def render():
    job = st.session_state.get("selected_job")
    department = st.session_state.get("department")

    if not job:
        st.warning("No job selected.")
        return

    st.title(job)
    st.subheader(f"{department} Department")

    if department == "IT":
        st.write("**Requirement:** Bachelor Degree")
        st.write("**Age:** 22–28 years")
        st.write("**Challan Fee:** PKR 2,000")

    elif department == "Government":
        st.write("**Requirement:** Matric / Intermediate")
        st.write("**Age:** 18–30 years")
        st.write("**Challan Fee:** PKR 1,500")

    elif department == "Federal":
        st.write("**Requirement:** Age 30–35 years")
        st.write("**Challan Fee:** PKR 1,000")

    if st.button("Apply Now"):
        st.session_state.page = "Apply"
        st.rerun()
