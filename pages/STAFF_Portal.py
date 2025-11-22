import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas

# -----------------------------------------------------
# STAFF-ONLY ACCESS CONTROL
# -----------------------------------------------------
if "role" not in st.session_state or st.session_state.role != "staff":
    st.error("Unauthorized. Please login as Staff.")
    st.stop()

# -----------------------------------------------------
# HIDE SIDEBAR FOR STAFF
# -----------------------------------------------------
hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {visibility: hidden !important; width: 0px !important;}
        [data-testid="collapsedControl"] {visibility: hidden !important;}
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

# -----------------------------------------------------
# ALIGN LOGOUT BUTTON RIGHT (TOP RIGHT CORNER)
# -----------------------------------------------------
logout_css = """
<style>
.logout-btn {
    display: flex;
    justify-content: flex-end;
    margin-top: -50px;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(logout_css, unsafe_allow_html=True)

# Wrapper row for logout button
with st.container():
    st.markdown("<div class='logout-btn'>", unsafe_allow_html=True)
    if st.button("🔓 Logout", key="logout_staff"):
        st.session_state.role = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# PDF GENERATOR FUNCTION
# -----------------------------------------------------
def generate_memo(center_name, dates, staff_name, center_address):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 800, "EXAM DUTY MEMO")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Staff Name: {staff_name}")
    c.drawString(50, 740, f"Allotted Center: {center_name}")
    c.drawString(50, 720, f"Center Address: {center_address}")
    c.drawString(50, 700, f"Duty Dates: {dates}")
    c.drawString(50, 680, "Reporting Time: 8:00 AM")

    c.drawString(50, 650, "Instructions:")
    c.drawString(70, 630, "• Report one day prior to duty.")
    c.drawString(70, 610, "• Bring your College ID card.")
    c.drawString(70, 590, "• Follow all exam protocols strictly.")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# -----------------------------------------------------
# STAFF PORTAL UI
# -----------------------------------------------------
st.title("👨‍🏫 Staff Portal")

# Tabs
tab1, tab2, tab3 = st.tabs(["Profile", "Preferences", "Allotment Result"])


# -----------------------------------------------------
# PROFILE TAB
# -----------------------------------------------------
with tab1:
    st.header("Personal Information")

    # Replace with database values later
    st.write("**Name:** Dr. Anil Kumar")
    st.write("**Staff ID:** CS102")
    st.write("**Department:** Computer Science")
    st.write("**Staff Type:** Chief Superintendent (CS)")
    st.write("**Zone:** Zone 2 / St. Joseph’s College")


# -----------------------------------------------------
# PREFERENCES TAB
# -----------------------------------------------------
with tab2:
    st.markdown("## Exam Center Preferences")

    # ------------------------------
    # Sample Data (Replace with DB later)
    # ------------------------------
    districts = {
        "Chennai": [
            "St. Mary’s College (C001)",
            "Loyola College (C002)",
            "Presidency College (C003)"
        ],
        "Coimbatore": [
            "Government College of Tech (C101)",
            "PSG Arts College (C102)"
        ],
        "Madurai": [
            "American College (C201)",
            "Thiagarajar College (C202)"
        ]
    }

    dist_names = list(districts.keys())

    # ------------------------------
    # Two Cards Layout
    # ------------------------------
    col_form, col_saved = st.columns([2, 1], gap="large")

    # -------------------------------------------------
    # LEFT CARD (FORM)
    # -------------------------------------------------
    with col_form:
        st.markdown("""
            <div style="
                background-color: #ffffff;
                padding: 25px;
                border-radius: 16px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            ">
        """, unsafe_allow_html=True)

        st.info("Choose your preferred exam centers (Up to 3).")

        # -------------------------------------------------
        # Preference 1
        # -------------------------------------------------
        st.subheader("Preference 1")

        pref1_dist = st.selectbox("Filter by District", dist_names, key="pref1_dist")
        pref1_center = st.selectbox("— Select —", districts[pref1_dist], key="pref1_center")

        # -------------------------------------------------
        # Preference 2
        # -------------------------------------------------
        st.subheader("Preference 2")

        pref2_dist = st.selectbox("Filter by District", dist_names, key="pref2_dist")
        pref2_center = st.selectbox("— Select —", districts[pref2_dist], key="pref2_center")

        # -------------------------------------------------
        # Preference 3
        # -------------------------------------------------
        st.subheader("Preference 3")

        pref3_dist = st.selectbox("Filter by District", dist_names, key="pref3_dist")
        pref3_center = st.selectbox("— Select —", districts[pref3_dist], key="pref3_center")

        # -------------------------------------------------
        # Save + Lock Buttons
        # -------------------------------------------------
        c1, c2 = st.columns([1, 1])

        with c1:
            save_clicked = st.button("💾 Save Preferences", use_container_width=True)

        with c2:
            lock_clicked = st.button("🔒 Lock Preferences", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------------------------------
        # Save Logic
        # -------------------------------------------------
        if save_clicked:
            st.session_state.saved_preferences = [
                pref1_center,
                pref2_center,
                pref3_center
            ]
            st.success("Preferences saved successfully!")

        if lock_clicked:
            st.session_state.locked = True
            st.warning("Your preferences are locked. You cannot modify them now.")

    # -------------------------------------------------
    # RIGHT CARD (SAVED PREFERENCES)
    # -------------------------------------------------
    with col_saved:
        st.markdown("""
            <div style="
                background-color: #ffffff;
                padding: 25px;
                border-radius: 16px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
            ">
        """, unsafe_allow_html=True)

        st.markdown("### Saved Preferences")

        if "saved_preferences" in st.session_state:
            st.success("Preferences saved successfully!")
            for i, p in enumerate(st.session_state.saved_preferences, 1):
                st.write(f"**{i}. {p}**")
        else:
            st.info("No preferences saved yet.")

        st.markdown("</div>", unsafe_allow_html=True)




# -----------------------------------------------------
# ALLOTMENT RESULT TAB
# -----------------------------------------------------
with tab3:
    st.header("Allotment Result")

    # Sample values (replace with real DB data)
    center_name = "St. Mary’s College"
    center_code = "C001"
    center_address = "Cathedral Road, Chennai"
    duty_dates = "12–15 March 2025"
    staff_name = "Dr. Anil Kumar"

    st.success(f"You have been allotted to **{center_name} ({center_code})**")

    st.write(f"**Center Address:** {center_address}")
    st.write(f"**Duty Dates:** {duty_dates}")
    st.write("**Reporting Time:** 8:00 AM")

    # Generate Memo PDF
    memo_pdf = generate_memo(center_name, duty_dates, staff_name, center_address)

    st.download_button(
        label="📄 Download Duty Memo (PDF)",
        data=memo_pdf,
        file_name="duty_memo.pdf",
        mime="application/pdf"
    )
