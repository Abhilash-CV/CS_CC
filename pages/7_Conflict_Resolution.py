import streamlit as st

st.title("⚔️ Conflict Resolution")

st.write("Center: Loyola College")

st.radio("Select Staff to Allot", ["Dr. Kumar (12 yrs)", "Dr. Raj (9 yrs)"])

if st.button("Resolve Conflict"):
    st.success("Conflict resolved.")
