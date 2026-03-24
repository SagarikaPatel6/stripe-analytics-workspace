import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.title("📊 Product Analytics")

    users = pd.read_csv("data/users.csv")
    onboarding = pd.read_csv("data/onboarding_events.csv")
    activity = pd.read_csv("data/user_activity.csv")

    st.subheader("Onboarding Funnel")

    funnel_counts = onboarding.groupby("step")["user_id"].nunique().reset_index()
    fig = px.funnel(funnel_counts, x="user_id", y="step")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Weekly Active Users")

    activity["activity_date"] = pd.to_datetime(activity["activity_date"])
    weekly = activity.groupby(activity["activity_date"].dt.to_period("W"))["user_id"].nunique()
    st.line_chart(weekly)
