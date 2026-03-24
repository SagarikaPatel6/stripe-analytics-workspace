import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.title("🛠 Operations Analytics")

    tickets = pd.read_csv("data/support_tickets.csv")
    tickets["created_at"] = pd.to_datetime(tickets["created_at"])

    st.subheader("Ticket Volume Over Time")
    daily = tickets.groupby(tickets["created_at"].dt.date).size()
    st.line_chart(daily)

    st.subheader("Priority Distribution")
    fig = px.pie(tickets, names="priority")
    st.plotly_chart(fig, use_container_width=True)
