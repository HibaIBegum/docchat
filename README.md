---
title: DocChat
emoji: 📄
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# 📄 DocChat — Chat with Any Document

An AI-powered document Q&A app built with Streamlit, ChromaDB, and Groq.

## Live Demo
[👉 Try DocChat Live](https://huggingface.co/spaces/hibabegum/docchat)

## Features
- Upload any PDF
- Automatically chunks and indexes the document with 20% overlap for accurate retrieval
- Ask questions in natural language
- Answers pulled strictly from the document — no hallucination

## Tech Stack
- Streamlit — UI
- PyMuPDF (fitz) — PDF reading and text extraction
- ChromaDB — vector storage and semantic search
- Groq — answer generation (OpenAI open model `openai/gpt-oss-20b`)
- Python-dotenv — environment management

## How It Works
1. PDF is read and split into overlapping chunks
2. Chunks are embedded and stored in ChromaDB
3. User question is converted to a vector and matched against chunks
4. Top matching chunks are sent to Groq as context
5. Groq returns an answer strictly based on the document

## Setup Locally
1. Clone the repo
```bash
   git clone https://github.com/HibaIBegum/docchat.git
   cd docchat
```
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
5. Run the app
```bash
   streamlit run app.py
```

## Author
Hiba Iqbal Begum — [LinkedIn](https://www.linkedin.com/in/hibabegum/)
