

import pandas as pd
import streamlit as st


risk_df = pd.read_csv('../data/risk_scores.csv')


try:
    with open('../data/auc.txt', 'r') as f:
        auc = float(f.read().strip())
except:
    auc = None


st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("Insurance Claim Fraud Detection Dashboard")

st.subheader("📊 Combined Risk Score Distribution")
st.bar_chart(risk_df['combined_risk_score'])

st.subheader("🚩 Flagged Top 10% Risk Claims")
st.dataframe(risk_df[risk_df['flagged'] == 1].reset_index(drop=True))

st.subheader("📋 Full Claims Overview")
st.dataframe(risk_df.reset_index(drop=True))

if auc:
    st.success(f"Model ROC AUC Score: {auc:.2f}")
else:
    st.warning("AUC score not found.")
