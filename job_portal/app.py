import streamlit as st
from auth import login, signup, init_users
from styles import load_css
from pages import home, about, contact, career, jobs, job_detail, apply

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Job Portal", layout="wide")
load_css()
init_users()

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Landing"   # 👈 landing is default

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

if "show_auth" not in st.session_state:
    st.session_state.show_auth = False


# ---------------- NAVBAR ----------------
def navbar():
    c1, c2, c3, c4, c5 = st.columns(5)

    if c1.button("Home"):
        st.session_state.page = "Home"
        st.rerun()

    if c2.button("About"):
        st.session_state.page = "About"
        st.rerun()

    if c3.button("Career"):
        st.session_state.page = "Career"
        st.rerun()

    if c4.button("Contact"):
        st.session_state.page = "Contact"
        st.rerun()

    if c5.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.show_auth = False
        st.session_state.auth_page = "login"
        st.session_state.page = "Landing"
        st.rerun()


# ---------------- AUTH UI ----------------
# ---------- AUTH UI ----------
def auth_ui():
    st.markdown("""
    <style>
    .auth-box {
        max-width: 320px;
        margin: auto;
        padding-top: 120px;
        text-align: center;
    }
    .auth-box input {
        width: 50%;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="auth-box">', unsafe_allow_html=True)

    if st.session_state.auth_page == "login":
        st.subheader("Login")

        username = st.text_input("", placeholder="Username", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Password", label_visibility="collapsed")

        if st.button("Login"):
            login(username, password)

        st.markdown("---")
        if st.button("Sign up", key="to_signup_btn"):
            st.session_state.auth_page = "signup"
            st.rerun()

    else:  # Sign Up Page
        st.subheader("Sign Up")

        username = st.text_input("", placeholder="Username", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Password", label_visibility="collapsed")

        if st.button("Create Account"):
            signup(username, password)

        st.markdown("---")
        if st.button("Sign in", key="to_login_btn"):
            st.session_state.auth_page = "login"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------- LANDING PAGE ----------------
def landing_page():
    st.title("Job Portal System")
    st.subheader("Your future starts here 🚀")

    st.write("")
    st.write("")

    if st.button("Get Started"):
        st.session_state.show_auth = True
        st.session_state.auth_page = "login"
        st.rerun()


# ---------------- MAIN FLOW ----------------
if not st.session_state.logged_in:

    if st.session_state.show_auth:
        auth_ui()

    else:
        landing_page()

else:
    navbar()

    if st.session_state.page == "Home":
        home.render()
    elif st.session_state.page == "About":
        about.render()
    elif st.session_state.page == "Career":
        career.render()
    elif st.session_state.page == "Contact":
        contact.render()
    elif st.session_state.page == "Jobs":
        jobs.render()
    elif st.session_state.page == "Job Detail":
        job_detail.render()
    elif st.session_state.page == "Apply":
        apply.render()
