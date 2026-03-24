import streamlit as st
from app import product_analytics, operations, experiments, data_products

# -----------------------------
# Stripe‑style global page config
# -----------------------------
st.set_page_config(
    page_title="Analytics Workspace",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Stripe‑style typography + card styling
# -----------------------------
st.markdown("""
<style>

.big-header {
    font-size: 36px;
    font-weight: 700;
    color: #1A1F36;
    padding-bottom: 4px;
}

.sub-header {
    font-size: 18px;
    font-weight: 400;
    color: #4F5B67;
    margin-bottom: 25px;
}

.metric-card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.metric-value {
    font-size: 28px;
    font-weight: 600;
    color: #1A1F36;
}

.metric-label {
    font-size: 14px;
    color: #6B7C93;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Navigation
# -----------------------------
PAGES = {
    "Product Analytics": product_analytics,
    "Operations": operations,
    "Experiments": experiments,
    "Data Products": data_products,
}

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))

# -----------------------------
# Page Header (Stripe‑style)
# -----------------------------
st.markdown("<div class='big-header'>Analytics Workspace</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Financial infrastructure for your data</div>", unsafe_allow_html=True)

# -----------------------------
# Render selected page
# -----------------------------
PAGES[choice].render()
