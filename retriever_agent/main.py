# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import json

from config import DOCUMENTS_PATH, FAISS_INDEX_PATH, METADATA_PATH, EMBEDDING_MODEL_NAME
from embeddings import get_embedding_model, embed_texts
from vector_store import FAISSRetriever

app = FastAPI()
retriever = FAISSRetriever(index_path=FAISS_INDEX_PATH, meta_path=METADATA_PATH)
model = get_embedding_model(EMBEDDING_MODEL_NAME)

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.post("/retrieve")
def retrieve_docs(req: QueryRequest):
    query_embedding = model.encode(req.query)
    retriever.load()
    results = retriever.search(query_embedding, top_k=req.top_k)
    return {"chunks": results}

@app.on_event("startup")
def startup():
    try:
        retriever.load()
    except:
        with open(DOCUMENTS_PATH, "r") as f:
            docs = json.load(f)
        texts = [d["text"] for d in docs]
        metadata = docs
        embeddings = embed_texts(texts, model)
        retriever.create_index(embeddings, metadata)
