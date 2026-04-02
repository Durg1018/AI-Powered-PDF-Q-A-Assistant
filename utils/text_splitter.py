# def split_text_into_chunks(text, chunk_size=500):
#     text = text.replace("\n", " ")
#     text = " ".join(text.split())

#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunk = text[i:i + chunk_size]
#         chunks.append(chunk)

#     return chunks

# def split_text_into_chunks(text, source_name, chunk_size=500):
#     text = text.replace("\n", " ")
#     text = " ".join(text.split())

#     chunks = []
#     chunk_id = 1

#     for i in range(0, len(text), chunk_size):
#         chunk_text = text[i:i + chunk_size]
#         chunks.append({
#             "source": source_name,
#             "chunk_id": chunk_id,
#             "text": chunk_text
#         })
#         chunk_id += 1

#     return chunks

# def split_text_into_chunks(text, source_name, chunk_size=120, overlap=30):
#     text = text.replace("\n", " ")
#     words = text.split()

#     chunks = []
#     chunk_id = 1
#     start = 0

#     while start < len(words):
#         end = start + chunk_size
#         chunk_words = words[start:end]
#         chunk_text = " ".join(chunk_words)

#         chunks.append({
#             "source": source_name,
#             "chunk_id": chunk_id,
#             "text": chunk_text
#         })

#         chunk_id += 1
#         start += chunk_size - overlap

#     return chunks

def split_text_into_chunks(pages, source_name, chunk_size=120, overlap=30):
    chunks = []
    chunk_id = 1

    for page in pages:
        page_num = page["page_num"]
        text = page["text"].replace("\n", " ")
        words = text.split()

        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            chunks.append({
                "source": source_name,
                "page_num": page_num,
                "chunk_id": chunk_id,
                "text": chunk_text
            })

            chunk_id += 1
            start += chunk_size - overlap

    return chunks