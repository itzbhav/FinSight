# FinSight~ Voice-Based Financial AI Assistant

# Multi-Agent Financial Assistant

A modular, open-source multi-agent financial assistant that ingests data from multiple sources (APIs, web scraping, documents), indexes knowledge in vector embeddings for Retrieval-Augmented Generation (RAG), orchestrates specialized microservices, and delivers spoken market briefs via a Streamlit frontend.

---

## 🚀 Project Overview

This project builds a multi-source, multi-agent financial assistant capable of:

- Fetching stock data, historical prices, and sector information via an **API Agent** (using Yahoo Finance).
- Scraping fresh financial news and filings via a **Scraping Agent**.
- Creating vector embeddings of ingested data and documents for fast similarity search in a **Retriever Agent**.
- Analyzing portfolio allocations, risk, and earnings surprises in an **Analytics Agent**.
- Composing intelligent narrative summaries using a **Language Agent** (e.g., LangGraph, CrewAI).
- Orchestrating all agents using a FastAPI microservice backend.
- Providing voice input/output using open-source toolkits (e.g., Whisper for speech-to-text, Coqui-TTS for text-to-speech).
- Serving the user interface via a **Streamlit app** with text and voice query support.

---

## 🛠️ Features

- **Multi-source data ingestion:** APIs, scraping, document loaders.
- **Vector store for RAG:** Embeddings indexed for fast retrieval.
- **Microservice architecture:** Separate agents for specialized tasks.
- **AI-powered language generation:** Intelligent market briefs and analysis.
- **Voice interaction:** Speech-to-text and text-to-speech pipelines.
- **Streamlit front-end:** Interactive UI for text/voice queries and visualizations.
- **Open-source & modular:** Easily extendable and well-documented.

---

## 📂 Project Structure

