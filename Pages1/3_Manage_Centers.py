import streamlit as st

st.title("🏫 Manage Exam Centers")

st.text_input("Center Name")
st.text_area("Address")
col1, col2 = st.columns(2)
col1.text_input("Zone")
col2.text_input("Center Code")

col1, col2 = st.columns(2)
col1.number_input("Vacancy (CS)", min_value=0)
col2.number_input("Vacancy (CC)", min_value=0)

if st.button("Add Center"):
    st.success("Center added successfully.")

st.subheader("Upload Centers (Excel)")
st.file_uploader("Upload Excel File", type=["xlsx"])
