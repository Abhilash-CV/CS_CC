import streamlit as st

st.title("📢 Publish Allotments")

if st.button("Publish Now"):
    st.success("Allotments published successfully!")

st.download_button("Download PDF Summary", "PDF coming soon", "summary.pdf")
