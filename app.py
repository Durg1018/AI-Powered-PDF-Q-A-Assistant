import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.retriever import compute_chunk_embeddings, get_top_matching_chunks
from utils.llm_answer import generate_llm_answer

st.set_page_config(page_title="AI PDF Assistant", page_icon="📄", layout="wide")


def build_chat_history_text(chat_history):
    if not chat_history:
        return "No chat history available."

    lines = []
    lines.append("AI-Powered PDF Q&A Assistant - Chat History")
    lines.append("=" * 50)
    lines.append("")

    for i, item in enumerate(chat_history, start=1):
        lines.append(f"Question {i}:")
        lines.append(f"Q: {item['question']}")
        lines.append(f"Answer Mode: {item['mode']}")
        lines.append(f"A: {item['answer']}")
        lines.append(f"Source File: {item['source']}")
        lines.append(f"Page Number: {item['page_num']}")
        lines.append(f"Chunk Number: {item['chunk_id']}")
        lines.append(f"Similarity Score: {item['score']:.4f}")
        lines.append("-" * 50)

    return "\n".join(lines)


st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
h1, h2, h3 {
    color: #f8fafc;
}
.custom-subtitle {
    color: #cbd5e1;
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
}
.card {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    margin-bottom: 16px;
}
.answer-box {
    background-color: #0f766e;
    padding: 16px;
    border-radius: 14px;
    color: white;
    font-size: 1rem;
    line-height: 1.6;
    margin-top: 10px;
}
.meta-box {
    background-color: #334155;
    padding: 12px;
    border-radius: 12px;
    color: #e2e8f0;
    margin-top: 10px;
    font-size: 0.95rem;
}
.user-bubble {
    background-color: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
}
.bot-bubble {
    background-color: #1e293b;
    color: white;
    padding: 14px 16px;
    border-radius: 16px;
    margin: 8px 0 18px 0;
    border: 1px solid #334155;
}
.small-note {
    color: #94a3b8;
    font-size: 0.9rem;
}
.badge-llm {
    display: inline-block;
    background-color: #15803d;
    color: white;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 10px;
}
.badge-fallback {
    display: inline-block;
    background-color: #b45309;
    color: white;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown("# 📄 AI-Powered PDF Q&A Assistant")
st.markdown(
    "<div class='custom-subtitle'>Upload one or more PDFs, ask questions, and get grounded answers with source tracking.</div>",
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.markdown("## ⚙️ Settings")

secret_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else ""
sidebar_key = st.sidebar.text_input("Gemini API Key (optional)", type="password")
gemini_api_key = sidebar_key if sidebar_key else secret_key

if gemini_api_key:
    st.sidebar.success("API key available")
else:
    st.sidebar.info("No API key detected. App will use fallback retrieval answers.")

st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ App Features")
st.sidebar.markdown("""
- Multi-PDF upload  
- Semantic retrieval  
- Page-aware answers  
- Chat history  
- Source grounding  
- Download chat history  
""")

# Upload
st.markdown("<div class='card'>", unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Upload PDF file(s)",
    type=["pdf"],
    accept_multiple_files=True
)
st.markdown("</div>", unsafe_allow_html=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} PDF file(s) uploaded successfully.")

    all_chunks = []
    extracted_texts = {}

    for uploaded_file in uploaded_files:
        pages = extract_text_from_pdf(uploaded_file)

        if pages:
            full_text = " ".join(page["text"] for page in pages)
            extracted_texts[uploaded_file.name] = full_text

            file_chunks = split_text_into_chunks(
                pages=pages,
                source_name=uploaded_file.name,
                chunk_size=120,
                overlap=30
            )
            all_chunks.extend(file_chunks)

    chunk_embeddings = compute_chunk_embeddings(all_chunks) if all_chunks else None

    if all_chunks:
        col_main, col_side = st.columns([2.3, 1])

        with col_main:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 💬 Ask a Question")
            question = st.text_input("Ask anything from your uploaded PDFs")
            search_clicked = st.button("Get Answer", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if search_clicked:
                if question.strip():
                    results = get_top_matching_chunks(
                        question,
                        all_chunks,
                        chunk_embeddings,
                        top_n=3,
                        min_score=0.25
                    )

                    if results:
                        best = results[0]

                        with st.spinner("Analyzing document and generating answer..."):
                            llm_result = generate_llm_answer(question, results, gemini_api_key)

                        st.session_state.chat_history.append({
                            "question": question,
                            "answer": llm_result["answer"],
                            "mode": llm_result["mode"],
                            "source": best["source"],
                            "page_num": best["page_num"],
                            "chunk_id": best["chunk_id"],
                            "score": best["score"],
                            "matches": results
                        })
                    else:
                        st.warning("No relevant chunks found.")
                else:
                    st.warning("Please enter a question.")

            if st.session_state.chat_history:
                st.markdown("### 🧠 Conversation")

                for item in reversed(st.session_state.chat_history):
                    st.markdown(
                        f"<div class='user-bubble'><b>You:</b> {item['question']}</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown("<div class='bot-bubble'>", unsafe_allow_html=True)

                    if item["mode"] == "LLM Generated":
                        st.markdown("<div class='badge-llm'>LLM Generated</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='badge-fallback'>Fallback Retrieval</div>", unsafe_allow_html=True)

                    st.markdown("**Assistant Answer**")
                    st.markdown(f"<div class='answer-box'>{item['answer']}</div>", unsafe_allow_html=True)

                    st.markdown(
                        f"""
<div class='meta-box'>
<b>Source File:</b> {item['source']}<br>
<b>Page Number:</b> {item['page_num']}<br>
<b>Chunk Number:</b> {item['chunk_id']}<br>
<b>Similarity Score:</b> {item['score']:.4f}
</div>
""",
                        unsafe_allow_html=True
                    )

                    with st.expander("View Top Matching Sections"):
                        for i, result in enumerate(item["matches"], start=1):
                            st.markdown(f"**Match {i}**")
                            st.markdown(
                                f"<div class='small-note'>Source: {result['source']} | Page: {result['page_num']} | Chunk: {result['chunk_id']} | Score: {result['score']:.4f}</div>",
                                unsafe_allow_html=True
                            )
                            st.write(result["text"])
                            st.markdown("---")

                    st.markdown("</div>", unsafe_allow_html=True)

        with col_side:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 📂 Uploaded Files")
            for file in uploaded_files:
                st.write(f"• {file.name}")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            show_text = st.checkbox("Show extracted PDF text")
            show_chunks = st.checkbox("Show all chunks")

            clear_history = st.button("Clear Chat History", use_container_width=True)
            if clear_history:
                st.session_state.chat_history = []
                st.rerun()

            chat_text = build_chat_history_text(st.session_state.chat_history)

            st.download_button(
                label="Download Chat History",
                data=chat_text,
                file_name="pdf_qa_chat_history.txt",
                mime="text/plain",
                use_container_width=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

        if show_text:
            st.markdown("### 📖 Extracted Text by File")
            for file_name, text in extracted_texts.items():
                st.text_area(f"{file_name}", text, height=220)

        if show_chunks:
            st.markdown("### 🧩 Generated Chunks")
            st.write(f"Total Chunks: {len(all_chunks)}")
            for chunk in all_chunks[:10]:
                with st.expander(
                    f"Source: {chunk['source']} | Page: {chunk['page_num']} | Chunk: {chunk['chunk_id']}"
                ):
                    st.write(chunk["text"])
    else:
        st.warning("No readable text found in uploaded PDFs.")
else:
    st.info("Please upload one or more PDF files to continue.")