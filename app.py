import streamlit as st

st.set_page_config(page_title="CS / CC Portal", layout="wide")

# Initialize session state
if "role" not in st.session_state:
    st.session_state.role = None

# ---------------------------------------------------------
# Hide sidebar completely on landing page (before login)
# ---------------------------------------------------------
if st.session_state.role is None:
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"] {visibility: hidden !important; width: 0px !important;}
            [data-testid="collapsedControl"] {visibility: hidden !important;}
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# ---------------------------------------------------------
# Auto-redirect if already logged in
# ---------------------------------------------------------
if st.session_state.role == "admin":
    st.switch_page("pages/1_Admin_Dashboard.py")

if st.session_state.role == "staff":
    st.switch_page("pages/STAFF_Portal.py")

# ---------------------------------------------------------
# LOGIN SCREEN
# ---------------------------------------------------------
st.title("📘 CS / CC Exam Duty Management Portal")

col1, col2 = st.columns(2)

# -------------------------
# ADMIN LOGIN
# -------------------------
with col1:
    st.header("🔐 Admin Login")

    admin_user = st.text_input("Username")
    admin_pass = st.text_input("Password", type="password")

    if st.button("Login as Admin"):
        if admin_user == "admin" and admin_pass == "admin123":
            st.session_state.role = "admin"
            st.success("Logging you in...")
            st.switch_page("pages/1_Admin_Dashboard.py")
        else:
            st.error("Invalid admin login")

# -------------------------
# STAFF LOGIN
# -------------------------
with col2:
    st.header("👨‍🏫 Staff Login")

    staff_id = st.text_input("Staff ID")
    staff_pass = st.text_input("Password", type="password", key="staffpass")

    if st.button("Login as Staff"):
        if staff_id.strip() != "" and staff_pass.strip() != "":
            st.session_state.role = "staff"
            st.success("Logging you in...")
            st.switch_page("pages/STAFF_Portal.py")
        else:
            st.error("Invalid staff login")

st.info("Use the login form to access your dashboard.")
