import streamlit as st
import pandas as pd
if 'role' not in st.session_state or st.session_state['role'] != 'admin':
    st.error("Unauthorized access. Please login as Admin.")
    st.stop()
st.title("🗂️ View Staff Preferences")

df = pd.DataFrame({
    "Staff ID": ["CS101", "CC212"],
    "Name": ["Dr. Kumar", "Ms. Anita"],
    "Pref1": ["Loyola", "MCC"],
    "Pref2": ["MCC", "Loyola"],
    "Pref3": ["Presidency", "-"]
})

st.dataframe(df)

st.download_button("⬇️ Export Preferences", df.to_csv(), "preferences.csv")
