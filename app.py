import streamlit as st
from chunker import extract_chunks
from database import build_database
from qa import ask 

st.set_page_config(page_title="DocChat", page_icon="📄")
st.title("📄 DocChat")
st.caption("Upload any document and ask questions about it")

if "collection" not in st.session_state:
    st.session_state.collection = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "doc_name" not in st.session_state:
    st.session_state.doc_name = None
upload_file= st.file_uploader("Upload a PDF", type=["pdf"])

if upload_file:
    if upload_file.name != st.session_state.doc_name:
        with st.spinner("Rading and indexing document..."):
            chunks,metadatas= extract_chunks(upload_file)
            st.session_state.collection = build_database(chunks,metadatas)
            st.session_state.doc_name = upload_file.name     
            st.session_state.chat_history=[]
        st.success(f"Document ready! Ask anything")

    if st.session_state.collection:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if message["role"] == "assistant" and message.get("source"):
                    st.caption(f"📄 Source: {message['source']}")

        question= st.chat_input("Ask a questuon about your document")

        if question:
            with st.chat_message("user"):
                st.write(question)
            st.session_state.chat_history.append({"role":"user","content":question})

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer,source= ask(st.session_state.collection,question)
                st.write(answer)
                if source:
                    st.caption(f"📄Source: {source}")
            st.session_state.chat_history.append({"role":"assistant","content":answer,"source":source})


        if st.button("Clear"):
            st.session_state.clear()
            st.rerun()
else:
    st.info("Upload a PDF above to get started")


