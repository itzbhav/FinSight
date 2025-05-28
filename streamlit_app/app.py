import streamlit as st
import requests

st.title("🧠 AI Financial Assistant")

query = st.text_input("Enter stock ticker (e.g., AAPL)")

if st.button("Analyze"):
    res = requests.post("http://127.0.0.1:8000/analyze", json={"query": query})
    if res.status_code == 200:
        data = res.json()
        st.success(data.get("response", "No summary returned"))
    else:
        st.error("Failed to get response from orchestrator.")
