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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_top_matching_chunks(question, chunks, top_n=3):
    if not chunks:
        return []

    documents = chunks + [question]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    question_vector = tfidf_matrix[-1]
    chunk_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(question_vector, chunk_vectors).flatten()

    ranked_indices = similarities.argsort()[::-1][:top_n]

    results = []
    for idx in ranked_indices:
        results.append({
            "chunk": chunks[idx],
            "score": float(similarities[idx])
        })

    return results