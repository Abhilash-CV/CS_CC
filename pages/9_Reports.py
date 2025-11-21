import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
if st.sidebar.button("🔓 Logout"):
    st.session_state.role = None
    st.rerun()
st.title("📊 Reports & Statistics")

report_type = st.selectbox("Select Report", [
    "Center-wise List",
    "Staff-wise Allotment",
    "Unallotted Staff",
    "Preference Analysis",
    "Repeat Allotment Report"
])

st.info("Report generation logic to be added based on your DB.")
