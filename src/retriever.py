import faiss
import numpy as np


class VectorStore:

    def __init__(self, embeddings, texts):

        self.texts = texts

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(embeddings))


    def search(self, query_embedding, k=3):

        distances, indices = self.index.search(query_embedding, k)

        results = [self.texts[i] for i in indices[0]]

        return results