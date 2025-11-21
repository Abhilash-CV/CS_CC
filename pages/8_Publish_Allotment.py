import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
if st.sidebar.button("🔓 Logout"):
    st.session_state.role = None
    st.rerun()
st.title("📢 Publish Allotments")

if st.button("Publish Now"):
    st.success("Allotments published successfully!")

st.download_button("Download PDF Summary", "PDF coming soon", "summary.pdf")
