import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
if st.sidebar.button("🔓 Logout"):
    st.session_state.role = None
    st.rerun()
st.title("⚙️ Settings")

st.number_input("Max Preferences Allowed", min_value=1, max_value=10, value=5)
st.selectbox("Default Allotment Rule", ["FCFS", "Seniority", "Random"])
st.checkbox("Allow Repeat Centers", value=True)
st.date_input("Preference Lock Deadline")
st.selectbox("Conflict Handling", ["Manual", "Automatic"])

if st.button("Save Settings"):
    st.success("Settings saved.")
