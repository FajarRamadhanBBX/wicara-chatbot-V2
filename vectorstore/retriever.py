from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from vectorstore.embedder import embedding

URL = "http://localhost:6333/dashboard"

embeddings = embedding()
client = QdrantClient(url=URL, prefer_grpc=False)

def retrieve_best_documents(query, k=5):
    db = Qdrant(
        client=client,
        embeddings=embeddings,
        collection_name="healthcare",
    )

    results = db.similarity_search(query, k=k)

    return results