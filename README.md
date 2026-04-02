# AI-Powered PDF Q&A Assistant

## Overview
AI-Powered PDF Q&A Assistant is an intelligent document question-answering application built using Python and Streamlit.

The application allows users to upload one or more PDF files, extract and process their content, and ask questions in natural language. It uses semantic retrieval with sentence embeddings to find the most relevant document sections and provides grounded answers with source tracking, including file name, page number, and chunk number.

The system also supports chat history, downloadable conversation logs, and fallback retrieval-based answers when LLM generation is unavailable.

---

## Features
- Upload one or more PDF documents
- Extract text from text-based PDF files
- Split content into overlapping chunks
- Semantic search using sentence embeddings
- Multi-PDF question answering
- Page-aware source tracking
- Chunk-level answer grounding
- Chat history for multiple questions
- Download chat history as a text file
- Premium Streamlit UI with answer cards and conversation layout
- LLM answer support with fallback retrieval mode

---

## Tech Stack
- Python
- Streamlit
- PyPDF2
- Scikit-learn
- Sentence Transformers
- Torch
- Torchvision
- Google GenAI / Gemini API
- NumPy

---

## Project Workflow
1. Upload one or more PDF files
2. Extract text page by page
3. Split text into overlapping chunks
4. Generate semantic embeddings for chunks
5. Retrieve top relevant chunks for a user question
6. Generate an answer using LLM or fallback retrieval mode
7. Display grounded answer with source file, page number, chunk number, and similarity score
8. Store the interaction in chat history

---

## Folder Structure
pdf-qa-assistant/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── screenshots/
│── sample_pdfs/
│── utils/
│   ├── pdf_reader.py
│   ├── text_splitter.py
│   ├── retriever.py
│   ├── answer_formatter.py
│   └── llm_answer.py

---

## How to Run
1. Clone the repository
2. Open the project folder in VS Code
3. Create and activate a virtual environment
4. Install dependencies:

   pip install -r requirements.txt

5. Run the app:

   streamlit run app.py

---

## How It Works
The application first extracts text from uploaded PDFs and splits it into smaller overlapping chunks. These chunks are converted into embeddings using Sentence Transformers. When a user asks a question, the application compares the question embedding with stored chunk embeddings and retrieves the most relevant matches.

The retrieved chunks are then used to generate the final answer. If LLM access is available, the app generates a cleaner AI-based answer. If LLM access is unavailable or quota fails, the application falls back to retrieval-based answering.

---

## Current Highlights
- Semantic retrieval instead of simple keyword matching
- Source-aware and page-aware answer grounding
- Better document transparency with chunk tracking
- Interactive conversation history
- Downloadable chat history
- Optional LLM-generated answer flow

---

## Current Limitations
- Works best with text-based PDFs
- Scanned/image PDFs may not work well without OCR
- LLM answers depend on API availability and quota
- Answer quality still depends on retrieved chunk quality

---

## Future Improvements
- OCR support for scanned PDFs
- Better PDF filtering by selected file
- Search inside selected document only
- More advanced citation display
- Export answers to PDF or Markdown
- Full deployment with secret management
- Better loading states and answer streaming

---

## Resume Highlights
- Built an AI-powered multi-PDF question answering system using Python and Streamlit
- Implemented semantic retrieval using sentence embeddings for document-based search
- Added page-aware and chunk-aware source grounding for answer transparency
- Integrated chat history, downloadable answer logs, and premium UI improvements
- Designed fallback retrieval-based answering when LLM generation is unavailable

---

## Sample Questions
- What is this document about?
- What sections are present in the document?
- What are the key points discussed in the PDF?
- Summarize the main arguments from the uploaded files.
- What does the document say about a particular topic?

---

## Author
Durgesh Desale