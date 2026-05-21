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
