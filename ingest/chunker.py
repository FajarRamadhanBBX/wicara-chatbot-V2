from langchain_experimental.text_splitter import SemanticChunker
from langchain.schema import Document
from vectorstore.embedder import embedding

embedder = embedding()

def chunking_documents(documents: list[Document]) -> list[Document]:
    text_splitter = SemanticChunker(
        embedder,
        min_chunk_size = 100,
        breakpoint_threshold_type="gradient")

    texts = text_splitter.split_documents(documents)
    
    return texts