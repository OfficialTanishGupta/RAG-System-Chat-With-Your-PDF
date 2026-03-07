import faiss
import numpy as np

def create_vector_store(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index


def retrieve(query_embedding, index, chunks, k=3):

    distances, indices = index.search(query_embedding, k)

    results = [chunks[i] for i in indices[0]]

    return results