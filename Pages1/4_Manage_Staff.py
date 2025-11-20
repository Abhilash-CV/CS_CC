import streamlit as st

st.title("👩‍🏫 Manage Staff")

st.text_input("Staff ID")
st.text_input("Name")
st.text_input("Department")
st.selectbox("Staff Type", ["CS", "CC"])
st.text_input("Email")
st.text_input("Mobile Number")
st.text_input("Zone / Base College")

if st.button("Add / Save Staff"):
    st.success("Staff saved successfully.")

st.subheader("Bulk Upload")
st.file_uploader("Upload Staff Excel", type=["xlsx"])
