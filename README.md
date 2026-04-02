# AI-Powered PDF Q&A Assistant

## Overview
AI-Powered PDF Q&A Assistant is a beginner-friendly NLP project built using Python and Streamlit.  
The application allows users to upload a PDF, extract its text, split it into chunks, and ask questions based on the uploaded document.  
It retrieves the most relevant sections of the PDF using TF-IDF vectorization and cosine similarity.

## Features
- Upload PDF documents
- Extract text from PDF files
- Split large text into manageable chunks
- Ask questions about the uploaded PDF
- Retrieve the most relevant answer from the document
- Display top matching sections with similarity scores
- Simple and interactive Streamlit user interface

## Tech Stack
- Python
- Streamlit
- PyPDF2
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## Project Workflow
1. Upload PDF file
2. Extract text from the PDF
3. Clean and split text into chunks
4. Convert chunks and question into TF-IDF vectors
5. Compute cosine similarity
6. Retrieve the most relevant chunk(s)
7. Display answer and matching sections

## Folder Structure
pdf-qa-assistant/
│── app.py
│── requirements.txt
│── README.md
│── sample_pdfs/
│── screenshots/
│── utils/
│   ├── pdf_reader.py
│   ├── text_splitter.py
│   └── retriever.py

## How to Run
1. Clone the repository
2. Open the project folder in VS Code
3. Create and activate a virtual environment
4. Install dependencies:
   pip install -r requirements.txt
5. Run the application:
   streamlit run app.py

## Sample Questions
- What is this document about?
- Which topics are included in the PDF?
- What are the important points discussed?

## Current Limitations
- Works best with text-based PDFs
- Does not work well with scanned/image PDFs
- Answers are retrieval-based and not generative

## Future Improvements
- Multiple PDF support
- Better chunking strategy
- Page number/source citation
- Semantic embeddings
- FAISS-based retrieval
- LLM-generated answers

## Resume Highlights
- Built an AI-powered PDF question answering system using Python and Streamlit
- Implemented PDF text extraction, text chunking, and retrieval-based question answering
- Used TF-IDF vectorization and cosine similarity to identify relevant content from uploaded documents
- Designed an interactive UI for document-based query handling

## Author
Durgesh Desale