from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def answer_question(query, vector_store):

    query_embedding = model.encode([query])

    results = vector_store.search(query_embedding)

    context = " ".join(results)

    answer = f"Based on the document:\n\n{context}"

    return answer