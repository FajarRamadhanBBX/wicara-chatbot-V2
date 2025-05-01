from langchain_community.vectorstores import Qdrant

def store_documents(chunking, embedding, URL):
    qdrant = Qdrant.from_documents(
        chunking,
        embedding,
        url = URL,
        prefer_grpc = False,
        collection_name="healthcare"
    )

    return qdrant