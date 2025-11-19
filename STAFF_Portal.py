import streamlit as st

st.title("👨‍🏫 Staff Portal")

tab1, tab2, tab3 = st.tabs(["Profile", "Preferences", "Allotment Result"])

with tab1:
    st.header("Personal Information")
    st.write("Name: Dr. Anil Kumar")
    st.write("Staff ID: CS102")
    st.write("Zone: Zone 2")

with tab2:
    st.header("Submit Preferences")
    st.selectbox("Preference 1", ["Loyola", "MCC", "Presidency"])
    st.selectbox("Preference 2", ["Loyola", "MCC", "Presidency"])
    st.selectbox("Preference 3", ["Loyola", "MCC", "Presidency"])

    if st.button("Save Preferences"):
        st.success("Preferences saved.")

with tab3:
    st.header("Allotment Result")
    st.info("Allotted Center: St. Mary’s College (C001)")
    st.button("Download Duty Memo (PDF)")
