# import streamlit as st
# from utils.pdf_reader import extract_text_from_pdf

# st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

# st.title("AI-Powered PDF Q&A Assistant")
# st.write("Upload a PDF and ask questions about it.")

# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# question = st.text_input("Ask a question about the PDF")

# if uploaded_file is not None:
#     st.success("PDF uploaded successfully.")

#     pdf_text = extract_text_from_pdf(uploaded_file)

#     st.subheader("Extracted Text from PDF")
#     if pdf_text.strip():
#         st.text_area("PDF Content", pdf_text, height=300)
#     else:
#         st.warning("No readable text found in this PDF.")

# if question:
#     st.write("Your question:", question)

# import streamlit as st
# from utils.pdf_reader import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks

# st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

# st.title("AI-Powered PDF Q&A Assistant")
# st.write("Upload a PDF and ask questions about it.")

# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
# question = st.text_input("Ask a question about the PDF")

# if uploaded_file is not None:
#     st.success("PDF uploaded successfully.")

#     pdf_text = extract_text_from_pdf(uploaded_file)

#     st.subheader("Extracted Text from PDF")
#     if pdf_text.strip():
#         st.text_area("PDF Content", pdf_text, height=200)

#         chunks = split_text_into_chunks(pdf_text, chunk_size=500)

#         st.subheader("Text Chunks")
#         st.write(f"Total Chunks: {len(chunks)}")

#         for i, chunk in enumerate(chunks[:5]):   # show first 5 chunks only
#             st.write(f"**Chunk {i+1}:**")
#             st.write(chunk)
#             st.write("---")
#     else:
#         st.warning("No readable text found in this PDF.")

# if question:
#     st.write("Your question:", question)

# import streamlit as st
# from utils.pdf_reader import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks
# from utils.retriever import get_most_relevant_chunk

# st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

# st.title("AI-Powered PDF Q&A Assistant")
# st.write("Upload a PDF and ask questions about it.")

# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file is not None:
#     st.success("PDF uploaded successfully.")

#     pdf_text = extract_text_from_pdf(uploaded_file)

#     if pdf_text.strip():
#         st.subheader("Extracted Text from PDF")
#         st.text_area("PDF Content", pdf_text, height=200)

#         chunks = split_text_into_chunks(pdf_text, chunk_size=500)

#         st.subheader("Text Chunks")
#         st.write(f"Total Chunks: {len(chunks)}")

#         for i, chunk in enumerate(chunks[:3]):
#             st.write(f"**Chunk {i+1}:**")
#             st.write(chunk)
#             st.write("---")

#         question = st.text_input("Ask a question about the PDF")

#         if question:
#             answer = get_most_relevant_chunk(question, chunks)

#             st.subheader("Answer")
#             st.write(answer)

#     else:
#         st.warning("No readable text found in this PDF.")
# else:
#     st.info("Please upload a PDF file to continue.")

# import streamlit as st
# from utils.pdf_reader import extract_text_from_pdf
# from utils.text_splitter import split_text_into_chunks
# from utils.retriever import get_most_relevant_chunk

# st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

# st.title("AI-Powered PDF Q&A Assistant")
# st.write("Upload a PDF and ask questions about its content.")

# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file is not None:
#     st.success("PDF uploaded successfully.")

#     pdf_text = extract_text_from_pdf(uploaded_file)

#     if pdf_text.strip():
#         chunks = split_text_into_chunks(pdf_text, chunk_size=500)

#         st.subheader("Ask Questions")
#         question = st.text_input("Enter your question")

#         if question:
#             answer = get_most_relevant_chunk(question, chunks)
#             st.subheader("Answer")
#             st.write(answer)

#         show_text = st.checkbox("Show extracted PDF text")
#         if show_text:
#             st.subheader("Extracted Text")
#             st.text_area("PDF Content", pdf_text, height=250)

#         show_chunks = st.checkbox("Show text chunks")
#         if show_chunks:
#             st.subheader("Text Chunks")
#             st.write(f"Total Chunks: {len(chunks)}")

#             for i, chunk in enumerate(chunks[:5]):
#                 st.write(f"**Chunk {i+1}:**")
#                 st.write(chunk)
#                 st.write("---")
#     else:
#         st.warning("No readable text found in this PDF.")
# else:
#     st.info("Please upload a PDF file to continue.")

import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.text_splitter import split_text_into_chunks
from utils.retriever import get_top_matching_chunks

st.set_page_config(page_title="PDF Q&A Assistant", layout="wide")

st.title("AI-Powered PDF Q&A Assistant")
st.write("Upload a PDF and ask questions about its content.")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully.")

    pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text.strip():
        chunks = split_text_into_chunks(pdf_text, chunk_size=500)

        st.subheader("Ask Questions")
        question = st.text_input("Enter your question")

        if question:
            results = get_top_matching_chunks(question, chunks, top_n=3)

            if results:
                st.subheader("Best Answer")
                st.info(results[0]["chunk"])

                st.subheader("Top Matching Sections")
                for i, result in enumerate(results, start=1):
                    st.write(f"**Match {i}**  |  Similarity Score: `{result['score']:.4f}`")
                    st.write(result["chunk"])
                    st.write("---")
            else:
                st.warning("No relevant chunks found.")

        show_text = st.checkbox("Show extracted PDF text")
        if show_text:
            st.subheader("Extracted Text")
            st.text_area("PDF Content", pdf_text, height=250)

        show_chunks = st.checkbox("Show text chunks")
        if show_chunks:
            st.subheader("Text Chunks")
            st.write(f"Total Chunks: {len(chunks)}")

            for i, chunk in enumerate(chunks[:5]):
                st.write(f"**Chunk {i+1}:**")
                st.write(chunk)
                st.write("---")
    else:
        st.warning("No readable text found in this PDF.")
else:
    st.info("Please upload a PDF file to continue.")