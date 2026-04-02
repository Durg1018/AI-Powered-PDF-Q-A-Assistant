# from PyPDF2 import PdfReader

# def extract_text_from_pdf(pdf_file):
#     pdf_reader = PdfReader(pdf_file)
#     text = ""

#     for page in pdf_reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text + "\n"

#     return text

# from PyPDF2 import PdfReader

# def extract_text_from_pdf(pdf_file):
#     pdf_reader = PdfReader(pdf_file)
#     text = ""

#     for page_num, page in enumerate(pdf_reader.pages, start=1):
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text + "\n"

#     return text

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    pages = []

    for page_num, page in enumerate(pdf_reader.pages, start=1):
        page_text = page.extract_text()
        if page_text:
            pages.append({
                "page_num": page_num,
                "text": page_text
            })

    return pages