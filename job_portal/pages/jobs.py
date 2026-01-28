import streamlit as st

JOBS = {
    "IT": [
        "AI Intern", "Python Intern", "Cyber Security Intern",
        "Web Developer Intern", "WordPress Intern", "SQA Intern",
        "Data Analyst Intern"
    ],
    "Government": [
        "Data Entry Operator", "Office Assistant",
        "Junior Clerk", "Record Keeper", "Typist", "Receptionist"
    ],
    "Federal": [
        "Sweeper", "Carpenter", "Electrician",
        "Waiter", "Gardener", "Security Guard", "Driver"
    ]
}

def render():
    department = st.session_state.get("department")

    if not department:
        st.warning("Please select a department first.")
        return

    st.title(f"📄 Jobs – {department} Department")

    for job in JOBS[department]:
        if st.button(job, key=f"job_{job}"):
            st.session_state.selected_job = job
            st.session_state.page = "Job Detail"
            st.rerun()
