#  Market - Agentic RAG System
![Uploading WhatsApp Image 2025-12-30 at 12.29.24 AM.jpeg…](https://github.com/user-attachments/assets/ebbb3548-55c5-4e9c-b55c-b65876131fba)

An advanced **Market Intelligence Analyst** built with a **RAG (Retrieval-Augmented Generation)** architecture. This system performs real-time web searching using **Tavily AI** and synthesizes professional market reports using **Llama-3 (Groq)** and **LangChain**.

---

## 🚀 Features
* **Real-time Web Research:** No more outdated LLM knowledge. It searches the live web for the latest news and trends.
* **Agentic Analysis:** Automatically cleans and summarizes search results into a professional business report.
* **FastAPI Backend:** Robust API layer for handling research queries.
* **Streamlit Frontend:** Clean, user-friendly interface for market analysts.
* **Downloadable Reports:** Save your research directly as text files.

---

## 📁 Project Structure
```text
market_analyst_rag/
├── main.py             # FastAPI Backend - The API Layer
├── processor.py        # LangChain Logic - The Analytical Brain
├── search_engine.py    # Tavily Integration - The Search Component
├── streamlit_app.py    # Streamlit UI - The Frontend
├── .env                # API Keys (Tavily, Groq/OpenAI)

└── requirements.txt    # Project Dependencies


