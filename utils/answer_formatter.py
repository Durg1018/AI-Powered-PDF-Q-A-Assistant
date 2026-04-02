# def format_answer(best_chunk, question):
#     text = best_chunk.strip()

#     if len(text) > 500:
#         text = text[:500] + "..."

#     return f"Based on the retrieved document section, the most relevant answer is:\n\n{text}"

def format_answer(results, question):
    if not results:
        return "No relevant answer found."

    combined_text = " ".join([item["text"] for item in results])

    if len(combined_text) > 700:
        combined_text = combined_text[:700] + "..."

    return f"Based on the most relevant retrieved sections, the answer is:\n\n{combined_text}"