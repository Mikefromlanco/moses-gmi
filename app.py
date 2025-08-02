import streamlit as st
from datetime import date

# ---------- Page Setup ----------
st.set_page_config(page_title="MOSES™ – Gross Motor Inventory", layout="wide")

# ---------- Header Logo (optional) ----------
st.markdown("""
    <div style='text-align: center; margin-bottom: 1rem;'>
        <img src='https://i.imgur.com/rqxziEQ.png' width='288'>
    </div>
""", unsafe_allow_html=True)

# ---------- Navigation ----------
sections = ["Child Demographics", "Inventory Items", "Reports"]
if "active_section" not in st.session_state:
    st.session_state.active_section = sections[0]

st.sidebar.title("Navigation")
for section in sections:
    if st.sidebar.button(section):
        st.session_state.active_section = section

st.markdown("---")

# ---------- Section Rendering ----------
if st.session_state.active_section == "Child Demographics":
    st.header("Child Demographics")
    st.text_input("First Name")
    st.text_input("Last Name")
    st.date_input("Date of Birth", value=date.today())
    st.radio("Gender", options=["Male", "Female"], horizontal=True)

elif st.session_state.active_section == "Inventory Items":
    st.header("Gross Motor Inventory Items")
    st.write("🚧 Inventory logic coming soon...")

elif st.session_state.active_section == "Reports":
    st.header("Report Generator")
    st.write("🚧 Report generation coming soon...")
