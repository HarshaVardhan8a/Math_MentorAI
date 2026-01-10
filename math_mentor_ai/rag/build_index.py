import os
import re
import pickle
import faiss
from sentence_transformers import SentenceTransformer

KB_PATH = "rag/knowledge_base"
INDEX_PATH = "rag/index"

os.makedirs(INDEX_PATH, exist_ok=True)


# ---------------- CHUNKING ----------------
def chunk_text(text, max_length=500):
    """
    Split text by headings and length
    """
    sections = re.split(r"\n## ", text)
    chunks = []

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue

        if len(sec) <= max_length:
            chunks.append(sec)
        else:
            for i in range(0, len(sec), max_length):
                chunks.append(sec[i:i + max_length])

    return chunks


# ---------------- LOAD FILES ----------------
def load_and_chunk_docs():
    all_chunks = []

    for file in os.listdir(KB_PATH):
        if file.endswith(".md"):
            with open(os.path.join(KB_PATH, file), "r", encoding="utf-8") as f:
                text = f.read()
                chunks = chunk_text(text)
                all_chunks.extend(chunks)

    return all_chunks


# ---------------- BUILD INDEX ----------------
def build_faiss_index():
    chunks = load_and_chunk_docs()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, f"{INDEX_PATH}/math.index")

    with open(f"{INDEX_PATH}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print(f"✅ Indexed {len(chunks)} chunks successfully")


if __name__ == "__main__":
    build_faiss_index()
