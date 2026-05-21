# 📄 DocChat — Chat with Any Document

An AI-powered document Q&A app built with Streamlit, ChromaDB, and Groq.

## Features
- Upload any PDF
- Automatically chunks and indexes the document
- Ask questions in natural language
- Answers pulled strictly from the document — no hallucination

## Tech Stack
- Streamlit — UI
- PyMuPDF (fitz) — PDF reading
- ChromaDB — vector storage and semantic search
- Groq (LLaMA 3.1) — answer generation
- Python-dotenv — environment management

## Setup

1. Clone the repo
2. Create a virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
```
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Create a `.env` file and add your Groq API key