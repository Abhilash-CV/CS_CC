import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
st.title("⚔️ Conflict Resolution")

st.write("Center: Loyola College")

st.radio("Select Staff to Allot", ["Dr. Kumar (12 yrs)", "Dr. Raj (9 yrs)"])

if st.button("Resolve Conflict"):
    st.success("Conflict resolved.")
