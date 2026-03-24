import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.title("🧪 Experimentation")

    exp = pd.read_csv("data/experiment_results.csv")

    summary = exp.groupby("variant")["converted"].mean().reset_index()
    summary["conversion_rate"] = summary["converted"] * 100

    st.subheader("Conversion Rate by Variant")
    fig = px.bar(summary, x="variant", y="conversion_rate", text="conversion_rate")
    st.plotly_chart(fig, use_container_width=True)

    uplift = (
        summary.loc[summary["variant"] == "treatment", "conversion_rate"].iloc[0]
        - summary.loc[summary["variant"] == "control", "conversion_rate"].iloc[0]
    )

    st.metric("Uplift (%)", f"{uplift:.2f}")
