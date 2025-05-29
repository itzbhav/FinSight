import streamlit as st
import requests

st.title("Multi-Agent Financial Assistant")

query = st.text_input("Enter company ticker (e.g., AAPL)")

if st.button("Analyze"):
    with st.spinner("Orchestrating agents..."):
        try:
            res = requests.post("http://localhost:8000/orchestrate", json={"query": query})
            res.raise_for_status()
            data = res.json()

            st.success("Analysis Complete!")
            st.subheader("📈 Stock Info")
            st.json(data["stock"])
            
            st.subheader("📰 News Headlines")
            for item in data["news"]:
             st.markdown(f"- {item}")

            st.subheader("🧠 Analysis")
            st.json(data["analysis"])

        except Exception as e:
            st.error(f"Something went wrong: {e}")
