# def get_most_relevant_chunk(question, chunks):
#     if not chunks:
#         return "No chunks available."
#     return chunks[0]

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def get_most_relevant_chunk(question, chunks):
#     if not chunks:
#         return "No chunks available."

#     documents = chunks + [question]

#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(documents)

#     question_vector = tfidf_matrix[-1]
#     chunk_vectors = tfidf_matrix[:-1]

#     similarities = cosine_similarity(question_vector, chunk_vectors).flatten()
#     most_similar_index = similarities.argmax()

#     return chunks[most_similar_index]

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def get_top_matching_chunks(question, chunks, top_n=3):
#     if not chunks:
#         return []

#     documents = chunks + [question]

#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(documents)

#     question_vector = tfidf_matrix[-1]
#     chunk_vectors = tfidf_matrix[:-1]

#     similarities = cosine_similarity(question_vector, chunk_vectors).flatten()

#     ranked_indices = similarities.argsort()[::-1][:top_n]

#     results = []
#     for idx in ranked_indices:
#         results.append({
#             "chunk": chunks[idx],
#             "score": float(similarities[idx])
#         })

#     return results

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def get_top_matching_chunks(question, chunks, top_n=3):
#     if not chunks:
#         return []

#     chunk_texts = [chunk["text"] for chunk in chunks]
#     documents = chunk_texts + [question]

#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(documents)

#     question_vector = tfidf_matrix[-1]
#     chunk_vectors = tfidf_matrix[:-1]

#     similarities = cosine_similarity(question_vector, chunk_vectors).flatten()
#     ranked_indices = similarities.argsort()[::-1][:top_n]

#     results = []
#     for idx in ranked_indices:
#         results.append({
#             "source": chunks[idx]["source"],
#             "chunk_id": chunks[idx]["chunk_id"],
#             "text": chunks[idx]["text"],
#             "score": float(similarities[idx])
#         })

#     return results


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def get_top_matching_chunks(question, chunks, top_n=3, min_score=0.08):
#     if not chunks:
#         return []

#     chunk_texts = [chunk["text"] for chunk in chunks]
#     documents = chunk_texts + [question]

#     vectorizer = TfidfVectorizer(stop_words="english")
#     tfidf_matrix = vectorizer.fit_transform(documents)

#     question_vector = tfidf_matrix[-1]
#     chunk_vectors = tfidf_matrix[:-1]

#     similarities = cosine_similarity(question_vector, chunk_vectors).flatten()
#     ranked_indices = similarities.argsort()[::-1]

#     results = []
#     for idx in ranked_indices:
#         score = float(similarities[idx])
#         if score < min_score:
#             continue

#         results.append({
#             "source": chunks[idx]["source"],
#             "chunk_id": chunks[idx]["chunk_id"],
#             "text": chunks[idx]["text"],
#             "score": score
#         })

#         if len(results) == top_n:
#             break

#     return results


# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def get_top_matching_chunks(question, chunks, top_n=3, min_score=0.25):
#     if not chunks:
#         return []

#     chunk_texts = [chunk["text"] for chunk in chunks]

#     chunk_embeddings = model.encode(chunk_texts)
#     question_embedding = model.encode([question])

#     similarities = cosine_similarity(question_embedding, chunk_embeddings).flatten()
#     ranked_indices = np.argsort(similarities)[::-1]

#     results = []
#     for idx in ranked_indices:
#         score = float(similarities[idx])

#         if score < min_score:
#             continue

#         results.append({
#             "source": chunks[idx]["source"],
#             "chunk_id": chunks[idx]["chunk_id"],
#             "text": chunks[idx]["text"],
#             "score": score
#         })

#         if len(results) == top_n:
#             break

#     return results

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# model = SentenceTransformer("all-MiniLM-L6-v2")

# def compute_chunk_embeddings(chunks):
#     chunk_texts = [chunk["text"] for chunk in chunks]
#     embeddings = model.encode(chunk_texts)
#     return embeddings

# def get_top_matching_chunks(question, chunks, chunk_embeddings, top_n=3, min_score=0.25):
#     if not chunks:
#         return []

#     question_embedding = model.encode([question])

#     similarities = cosine_similarity(question_embedding, chunk_embeddings).flatten()
#     ranked_indices = np.argsort(similarities)[::-1]

#     results = []
#     for idx in ranked_indices:
#         score = float(similarities[idx])

#         if score < min_score:
#             continue

#         results.append({
#             "source": chunks[idx]["source"],
#             "chunk_id": chunks[idx]["chunk_id"],
#             "text": chunks[idx]["text"],
#             "score": score
#         })

#         if len(results) == top_n:
#             break

#     return results

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_chunk_embeddings(chunks):
    chunk_texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(chunk_texts)
    return embeddings

def get_top_matching_chunks(question, chunks, chunk_embeddings, top_n=3, min_score=0.25):
    if not chunks:
        return []

    question_embedding = model.encode([question])

    similarities = cosine_similarity(question_embedding, chunk_embeddings).flatten()
    ranked_indices = np.argsort(similarities)[::-1]

    results = []
    for idx in ranked_indices:
        score = float(similarities[idx])

        if score < min_score:
            continue

        results.append({
            "source": chunks[idx]["source"],
            "page_num": chunks[idx]["page_num"],
            "chunk_id": chunks[idx]["chunk_id"],
            "text": chunks[idx]["text"],
            "score": score
        })

        if len(results) == top_n:
            break

    return results