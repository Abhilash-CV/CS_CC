import streamlit as st

st.title("📊 Reports & Statistics")

report_type = st.selectbox("Select Report", [
    "Center-wise List",
    "Staff-wise Allotment",
    "Unallotted Staff",
    "Preference Analysis",
    "Repeat Allotment Report"
])

st.info("Report generation logic to be added based on your DB.")
