import streamlit as st
from datetime import date

# ---------- Initialize State ----------
if "active_section" not in st.session_state:
    st.session_state.active_section = "Child Demographics"

# ---------- Page Setup ----------
st.set_page_config(page_title="MOSES™ – Gross Motor Inventory", layout="wide")

# ---------- Logo ----------
st.markdown("""
    <div style='text-align: center; margin-bottom: 1rem;'>
        <img src='https://i.imgur.com/rqxziEQ.png' width='288'>
    </div>
""", unsafe_allow_html=True)

# ---------- Navigation Sidebar ----------
sections = ["Child Demographics", "Inventory Items", "Reports"]
st.sidebar.title("Navigation")
for section in sections:
    if st.sidebar.button(section):
        st.session_state.active_section = section

st.markdown("---")

# ---------- Section: Child Demographics ----------
if st.session_state.active_section == "Child Demographics":
    st.header("Child Demographics")
    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")
        dob = st.date_input("Date of Birth", value=date.today())
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

    with col2:
        last_name = st.text_input("Last Name")
        doe = st.date_input("Date of Evaluation", value=date.today())
        therapist = st.text_input("Therapist Name")

    # Chronological Age Display
    if dob and doe:
        age_months = (doe.year - dob.year) * 12 + (doe.month - dob.month)
        age_years = age_months // 12
        remaining_months = age_months % 12
        st.markdown(f"**Chronological Age:** {age_years} years, {remaining_months} months")

# ---------- Section: Inventory Items ----------
elif st.session_state.active_section == "Inventory Items":
    st.header("Gross Motor Inventory Items")
    st.write("🚧 Inventory content coming soon...")

# ---------- Section: Reports ----------
elif st.session_state.active_section == "Reports":
    st.header("Report Generator")
    st.write("🚧 Report generation tools will appear here.")
