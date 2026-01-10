import faiss
import pickle
from sentence_transformers import SentenceTransformer

import os

# Get directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "index")

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(os.path.join(INDEX_PATH, "math.index"))

with open(os.path.join(INDEX_PATH, "chunks.pkl"), "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]
