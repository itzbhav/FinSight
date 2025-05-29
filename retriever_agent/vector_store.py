# vector_store.py
import faiss
import os
import pickle
import numpy as np

class FAISSRetriever:
    def __init__(self, index_path="vector_index/index.faiss", meta_path="vector_index/meta.pkl"):
        self.index_path = index_path
        self.meta_path = meta_path
        self.index = None
        self.meta = None

    def create_index(self, embeddings, metadata):
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.meta = metadata
        self._save()

    def _save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.meta, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.meta_path, "rb") as f:
            self.meta = pickle.load(f)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.meta[i] for i in I[0]]
