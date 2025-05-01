from langchain_community.embeddings import SentenceTransformerEmbeddings

def embedding(model_name = "NeuML/pubmedbert-base-embeddings"):
    embeddings = SentenceTransformerEmbeddings(model_name=model_name)
    return embeddings