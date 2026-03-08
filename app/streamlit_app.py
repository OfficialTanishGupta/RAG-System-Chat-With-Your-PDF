import sys
sys.path.append("../src")

import streamlit as st

from pdf_loader import load_pdf
from chunking import chunk_text
from embeddings import create_embeddings
from retriever import VectorStore
from qa_system import answer_question


st.title("📄 Chat with your PDF")


uploaded_file = st.file_uploader("Upload PDF", type="pdf")


if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = load_pdf("temp.pdf")

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    vector_store = VectorStore(embeddings, chunks)

    query = st.text_input("Ask a question")

    if query:

        answer = answer_question(query, vector_store)

        st.write(answer)