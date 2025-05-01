from vectorstore.retriever import retrieve_best_documents
from reranker.reranker import best_documents
from rag.prompt_template import prompt
from rag.generator import answer_prompt

def rag(query: str):
    docs = retrieve_best_documents(query)
    best_docs = best_documents(query, docs)
    prompt_template = prompt(query, best_docs[0].page_content)
    answer = answer_prompt(prompt_template)

    return answer