import streamlit as st

def render():
    st.title("📚 Data Products & Metrics Layer")

    st.markdown("""
    ### Metric Definitions

    **Activation Rate**  
    Percentage of users who complete the onboarding funnel.

    **Weekly Active Users (WAU)**  
    Count of unique users active in a given week.

    **Ticket SLA**  
    Time taken to resolve support tickets.

    **Experiment Conversion Rate**  
    Percentage of users who converted within each variant.

    ### Semantic Layer Example

    - `user_id`: Unique identifier for a user  
    - `signup_date`: Date user joined  
    - `step`: Onboarding step name  
    - `activity_date`: Date of user activity  
    - `priority`: Ticket urgency  
    """)
