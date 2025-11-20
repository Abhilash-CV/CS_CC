import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas

# -----------------------------------------------------
# 🔒 ACCESS CONTROL — Only Staff Can Open This Page
# -----------------------------------------------------
if "role" not in st.session_state or st.session_state.role != "staff":
    st.error("Unauthorized access. Please login as Staff.")
    st.stop()

# -----------------------------------------------------
# Function to generate Duty Memo PDF
# -----------------------------------------------------
def generate_memo(center_name, dates, staff_name, center_address):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 800, "EXAM DUTY MEMO")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Staff Name     : {staff_name}")
    c.drawString(50, 740, f"Allotted Center: {center_name}")
    c.drawString(50, 720, f"Center Address : {center_address}")
    c.drawString(50, 700, f"Duty Dates     : {dates}")
    c.drawString(50, 680, "Reporting Time : 8:00 AM")

    c.drawString(50, 650, "Instructions:")
    c.drawString(70, 630, "• Report one day prior to duty.")
    c.drawString(70, 610, "• Bring College ID card.")
    c.drawString(70, 590, "• Follow all exam protocols strictly.")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# -----------------------------------------------------
# Staff Portal UI
# -----------------------------------------------------
st.title("👨‍🏫 Staff Portal")

tab1, tab2, tab3 = st.tabs(["Profile", "Preferences", "Allotment Result"])

# -----------------------------------------------------
# PROFILE TAB
# -----------------------------------------------------
with tab1:
    st.header("Personal Information")

    # In real system - fetch from DB
    st.write("**Name:** Dr. Anil Kumar")
    st.write("**Staff ID:** CS102")
    st.write("**Department:** Computer Science")
    st.write("**Staff Type:** Chief Superintendent (CS)")
    st.write("**Zone / Base College:** Zone 2 / St. Joseph’s College")
    st.write("**Email:** anil.kumar@college.edu")
    st.write("**Mobile:** 98765 43210")

# -----------------------------------------------------
# PREFERENCES TAB
# -----------------------------------------------------
with tab2:
    st.header("Exam Center Preferences")

    st.info("Choose your preferred exam centers (Up to 3).")

    # Example list – replace with DB
    centers = [
        "St. Mary’s College (C001)",
        "Loyola College (C002)",
        "Presidency College (C003)",
        "Govt Arts College (C004)"
    ]

    pref1 = st.selectbox("Preference 1", centers)
    pref2 = st.selectbox("Preference 2", centers)
    pref3 = st.selectbox("Preference 3", centers)

    remarks = st.text_area("Remarks (optional)")

    if st.button("Save Preferences"):
        st.success("Preferences saved successfully!")

    if st.button("Lock Preferences"):
        st.warning("Your preferences are locked. You cannot change them now.")

# -----------------------------------------------------
# ALLOTMENT RESULT TAB
# -----------------------------------------------------
with tab3:
    st.header("Allotment Result")

    # Example allotment (replace with DB results)
    alloted_center = "St. Mary’s College"
    center_code = "C001"
    center_address = "Cathedral Road, Chennai"
    duty_dates = "12–15 March 2025"
    staff_name = "Dr. Anil Kumar"

    st.success(f"🎉 You have been allotted to **{alloted_center} ({center_code})**")

    st.write(f"**Center Address:** {center_address}")
    st.write(f"**Duty Dates:** {duty_dates}")
    st.write("**Reporting Time:** 8:00 AM")
    st.write("**Status:** Confirmed")

    # Generate PDF memo
    pdf_file = generate_memo(alloted_center, duty_dates, staff_name, center_address)

    st.download_button(
        label="📄 Download Duty Memo (PDF)",
        data=pdf_file,
        file_name="duty_memo.pdf",
        mime="application/pdf"
    )

    st.button("Raise Query to Admin")
