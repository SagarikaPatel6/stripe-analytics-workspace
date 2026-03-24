"""
Stripe Analytics Workspace - Main Application
Payment Failure Analysis: How we recovered $2.3M in annual revenue

Built by: Sagarika Patel
Purpose: Data Analyst application for Stripe
"""

import streamlit as st
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import pages
import landing_page
import executive_dashboard

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Stripe Analytics Workspace",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/SagarikaPatel6/stripe-analytics-workspace',
        'Report a bug': 'https://github.com/SagarikaPatel6/stripe-analytics-workspace/issues',
        'About': """
        # Stripe Analytics Workspace
        
        Payment failure analysis demonstrating data-driven revenue recovery.
        
        Built by Sagarika Patel as part of a Data Analyst application for Stripe.
        
        **Key Features:**
        - Executive-level business storytelling
        - Root cause analysis with statistical rigor
        - Actionable recommendations with ROI quantification
        - Interactive dashboards for deep-dive analysis
        
        [View on GitHub](https://github.com/SagarikaPatel6/stripe-analytics-workspace)
        """
    }
)

# -----------------------------
# Custom CSS (Stripe-style)
# -----------------------------
st.markdown("""
<style>
    /* Import Stripe's font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global styles */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-weight: 700;
        color: #0A2540;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #F7FAFC;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        font-size: 0.95rem;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 600;
        color: #0A2540;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.875rem;
        color: #425466;
        font-weight: 500;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.875rem;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #635BFF;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        border: none;
        transition: all 0.2s;
    }
    
    .stButton button:hover {
        background-color: #4D47CC;
        box-shadow: 0 4px 12px rgba(99, 91, 255, 0.3);
    }
    
    /* Info/warning/success boxes */
    .stAlert {
        border-radius: 8px;
        border-left: 4px solid;
    }
    
    /* Tables */
    [data-testid="stDataFrame"] {
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-weight: 500;
        padding-top: 0.75rem;
        padding-bottom: 0.75rem;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        font-weight: 500;
        font-size: 1rem;
    }
    
    /* Links */
    a {
        color: #635BFF;
        text-decoration: none;
    }
    
    a:hover {
        color: #4D47CC;
        text-decoration: underline;
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background-color: #635BFF;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Navigation
# -----------------------------
st.sidebar.title("⚡ Navigation")

pages = {
    "🏠 Home": landing_page,
    "📊 Executive Dashboard": executive_dashboard,
}

# Add description for each page
page_descriptions = {
    "🏠 Home": "Overview & business impact story",
    "📊 Executive Dashboard": "Deep-dive analysis & insights",
}

# Create radio buttons with descriptions
st.sidebar.markdown("### Select Page")
selection = st.sidebar.radio(
    "Navigate to:",
    list(pages.keys()),
    format_func=lambda x: x,
    label_visibility="collapsed"
)

# Show page description
st.sidebar.caption(page_descriptions[selection])

st.sidebar.markdown("---")

# -----------------------------
# Sidebar: Quick Stats
# -----------------------------
st.sidebar.markdown("### 📈 Quick Stats")

try:
    import pandas as pd
    df_transactions = pd.read_csv('data/transactions.csv')
    
    total_transactions = len(df_transactions)
    failure_rate = ((df_transactions['status'] == 'failed').sum() / total_transactions) * 100
    lost_revenue = df_transactions['revenue_impact'].sum()
    
    st.sidebar.metric("Transactions Analyzed", f"{total_transactions:,}")
    st.sidebar.metric("Platform Failure Rate", f"{failure_rate:.2f}%")
    st.sidebar.metric("Lost Revenue (6mo)", f"${lost_revenue:,.0f}")
    st.sidebar.metric("Recovery Opportunity", "$2.3M/year", delta="43% recoverable")
    
except FileNotFoundError:
    st.sidebar.warning("⚠️ Data files not found. Please ensure data is generated.")
    if st.sidebar.button("Generate Data"):
        import subprocess
        subprocess.run(["python", "generate_data.py"])
        st.rerun()

st.sidebar.markdown("---")

# -----------------------------
# Sidebar: About
# -----------------------------
with st.sidebar.expander("ℹ️ About This Project"):
    st.markdown("""
    **Payment Failure Analysis**
    
    This workspace demonstrates how data analysis can drive significant business impact through:
    
    - Root cause analysis
    - Statistical rigor
    - Actionable recommendations
    - ROI quantification
    
    **Built by:** Sagarika Patel  
    **Purpose:** Data Analyst application for Stripe  
    **GitHub:** [View Code](https://github.com/SagarikaPatel6/stripe-analytics-workspace)
    
    ---
    
    **Tech Stack:**
    - Python (Pandas, NumPy, SciPy)
    - Streamlit (Dashboard)
    - Plotly (Visualizations)
    - Statistical Testing
    """)

# Add feedback section
with st.sidebar.expander("💬 Feedback"):
    st.markdown("""
    Questions or feedback?
    
    📧 Email: [Your Email]  
    💼 LinkedIn: [Your Profile]  
    🐙 GitHub: [@SagarikaPatel6](https://github.com/SagarikaPatel6)
    """)

st.sidebar.markdown("---")
st.sidebar.caption("Last updated: March 23, 2026")

# -----------------------------
# Render Selected Page
# -----------------------------
pages[selection].render()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #8898AA; padding: 1.5rem 0; font-size: 0.875rem;'>
        <p>
            <strong>Stripe Analytics Workspace</strong> • 
            Built by Sagarika Patel • 
            <a href='https://github.com/SagarikaPatel6/stripe-analytics-workspace' target='_blank'>View on GitHub</a>
        </p>
        <p style='margin-top: 0.5rem;'>
            Data Analyst Application for Stripe • March 2026
        </p>
    </div>
""", unsafe_allow_html=True)
