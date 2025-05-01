from ingest.loader import read_pdf_documents
from ingest.cleaner import filter_documents
from ingest.chunker import chunking_documents
from vectorstore.store import store_documents
from vectorstore.embedder import embedding

URL = "http://localhost:6333"

def ingest_documents():
    embedder = embedding(model_name="NeuML/pubmedbert-base-embeddings")
    loader = read_pdf_documents(path="data/")
    cleaner = filter_documents(documents=loader)
    chunking = chunking_documents(documents=cleaner)
    qdrant = store_documents(chunking=chunking, embedding=embedder, URL=URL) 