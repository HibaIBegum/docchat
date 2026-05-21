import streamlit as st
from chunker import extract_chunks
from database import build_database
from qa import ask 

st.set_page_config(page_title="DocChat", page_icon="📄")
st.title("📄 DocChat")
st.caption("Upload any document and ask questions about it")

upload_file= st.file_uploader("Upload a PDF", type=["pdf"])

if upload_file:
    if "collection" not in st.session_state:
        with st.spinner("Rading and indexing document..."):
            chunks= extract_chunks(upload_file)
            st.session_state.collection = build_database(chunks)
            st.session_state.chat_history=[]
        st.success(f"Document ready! Ask anything")
    
    question= st.chat_input("Ask a questuon about your document")

    if question:

        answer= ask(st.session_state.collection,question)
        st.session_state.chat_history.append(("user",question))
        st.session_state.chat_history.append(("assistant",answer))

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(message)

    if st.button("Clear"):
        st.session_state.clear()
        st.rerun()


