import streamlit as st

st.set_page_config(page_title="CS / CC Exam Duty Portal", layout="wide")

# HOME PAGE
st.title("📘 CS / CC Exam Duty Management Portal")

col1, col2 = st.columns(2)

with col1:
    st.header("🔐 Admin Login")
    admin_user = st.text_input("Username", key="admin_user")
    admin_pass = st.text_input("Password", type="password", key="admin_pass")
    if st.button("Login as Admin"):
        st.session_state['role'] = "admin"
        st.success("Logged in as Admin. Open pages from sidebar.")

with col2:
    st.header("👨‍🏫 Staff Login")
    staff_id = st.text_input("Staff ID", key="staff_id")
    staff_pass = st.text_input("Password", type="password", key="staff_pass")
    if st.button("Login as Staff"):
        st.session_state['role'] = "staff"
        st.success("Logged in as Staff. Open STAFF Portal page.")

st.info("Use the Sidebar to open Admin pages or Staff Portal.")
