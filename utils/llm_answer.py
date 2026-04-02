from google import genai

def generate_llm_answer(question, results, api_key):
    if not results:
        return {
            "answer": "No relevant context found to generate an answer.",
            "mode": "No Context"
        }

    combined_text = " ".join([item["text"] for item in results])
    fallback_answer = (
        "Based on the most relevant retrieved sections, the answer is:\n\n"
        + (combined_text[:700] + "..." if len(combined_text) > 700 else combined_text)
    )

    if not api_key:
        return {
            "answer": fallback_answer,
            "mode": "Fallback Retrieval"
        }

    try:
        client = genai.Client(api_key=api_key)

        context = "\n\n".join(
            [
                f"Source: {item['source']}, Page: {item['page_num']}, Chunk: {item['chunk_id']}\n{item['text']}"
                for item in results
            ]
        )

        prompt = f"""
You are a helpful PDF question-answering assistant.

Answer the user's question ONLY using the context provided below.
If the answer is not clearly available in the context, say:
"The answer is not clearly available in the provided document sections."

Keep the answer:
- clear
- concise
- well-structured
- based only on the provided context

User Question:
{question}

Context:
{context}
"""

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        return {
            "answer": response.text.strip() if response.text else fallback_answer,
            "mode": "LLM Generated"
        }

    except Exception:
        return {
            "answer": fallback_answer,
            "mode": "Fallback Retrieval"
        }