import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
if st.sidebar.button("🔓 Logout"):
    st.session_state.role = None
    st.rerun()
st.title("🗓️ Manage Exam Sessions")

st.text_input("Session Name")
col1, col2 = st.columns(2)
col1.date_input("Start Date")
col2.date_input("End Date")
st.date_input("Preference Deadline")
st.selectbox("Status", ["Active", "Closed"])

if st.button("Save Session"):
    st.success("Session saved successfully.")
