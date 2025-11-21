import streamlit as st
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
st.title("⚙️ Run Auto-Allotment")

rule = st.selectbox("Select Rule", [
    "FCFS",
    "Seniority-based",
    "Random",
    "Weighted Score"
])

if st.button("Run Allotment"):
    st.success("Temporary allotment generated.")
    st.write("Preview:")
    st.table({
        "Staff": ["Dr. Kumar", "Ms. Anita"],
        "Allotted Center": ["Loyola", "Conflict"],
        "Rule Used": [rule, rule]
    })
