import streamlit as st

st.title("📊 Admin Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Active Session", "March 2025 UG")
col2.metric("Total Staff", 240)
col3.metric("Total Centers", 65)
col4.metric("Preferences Submitted", "220 / 240")

st.subheader("Conflict Summary")
st.warning("18 Centers have high preference load.")

st.subheader("Preference Demand by Center")
st.bar_chart({
    "Loyola": 40,
    "MCC": 32,
    "Presidency": 28,
    "St. Mary's": 25
})
