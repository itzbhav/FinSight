import streamlit as st
import requests

st.set_page_config(page_title="FinSight Orchestrator", layout="centered")
st.title("🤖 FinSight: AI-Powered Market Analyzer")

query = st.text_input("Enter a company name", "")

if st.button("Analyze") and query:
    with st.spinner("Fetching and analyzing data..."):
        try:
            response = requests.post("http://localhost:8000/orchestrate", json={"query": query})
            response.raise_for_status()
            data = response.json()

            st.subheader("📊 Stock Data")
            st.json(data["stock"])

            st.subheader("📰 News Headlines")
            for article in data["news"]:
                st.markdown(f"- {article['title']}")

            st.subheader("📈 AI Analysis")
            st.json(data["analysis"])

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
