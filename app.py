import streamlit as st
from datetime import date

# Set initial section if not already set
if "active_section" not in st.session_state:
    st.session_state.active_section = "Child Demographics"

# ---------- Page Setup ----------
st.set_page_config(page_title="MOSES™ – Gross Motor Inventory", layout="wide")
