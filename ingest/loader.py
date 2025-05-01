from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

def read_pdf_documents(path: str):
    loader = DirectoryLoader(
        path=path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
    )
    
    documents = loader.load()
    return documents