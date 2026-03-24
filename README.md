# 📊 Stripe‑Style Analytics Workspace  
A modular, Streamlit‑based analytics workspace showcasing product analytics, operations insights, experimentation, and data‑product thinking — powered by realistic synthetic data (July–December 2025).

This project demonstrates how a modern data team can enable product, operations, and GTM stakeholders with clear, actionable dashboards and a self‑serve metrics layer.

---

## 🚀 Overview

This workspace includes four core analytics domains:

### **1. Product Analytics**
- Onboarding funnel (signup → business info → identity verification → first payment)
- Activation and weekly engagement
- Cohort retention (heatmap)
- Segment‑level insights (SMB, Mid‑market, Enterprise)

### **2. Operations Analytics**
- Ticket volume trends
- SLA performance
- Priority distribution
- Resolution time modeling

### **3. Experimentation**
- A/B test analysis (control vs treatment)
- Conversion uplift
- Variant‑level metrics
- Statistical comparison

### **4. Data Products**
- Metric definitions
- Semantic layer examples
- How teams can self‑serve analytics

---


---

## 📅 Data

All datasets are synthetic and cover **July → December 2025**.

| File | Rows | Description |
|------|------|-------------|
| `users.csv` | 1,000 | User profiles, signup dates, segments |
| `onboarding_events.csv` | ~3,500 | Funnel steps + timestamps |
| `user_activity.csv` | ~10,000 | Weekly engagement events |
| `support_tickets.csv` | ~1,000 | Ticket metadata + SLA |
| `experiment_results.csv` | 2,000 | A/B test assignments + conversions |

---

## 🧠 Key Concepts Demonstrated

### **Product Analytics**
- Funnel analysis  
- Activation modeling  
- Retention cohorts  
- Segment‑level insights  

### **Operations**
- SLA tracking  
- Queue health  
- Ticket lifecycle modeling  

### **Experimentation**
- Variant assignment  
- Conversion rate analysis  
- Uplift measurement  

### **Data Products**
- Metric definitions  
- Reusable semantic layer  
- Stakeholder‑friendly documentation  

---

## ▶️ Running Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


