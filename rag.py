from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_qdrant.vectorstores import Qdrant
from qdrant_client import QdrantClient
from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from function.reranking import rerank_documents
from function.answer_prompt import answer_prompt
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

prompt_template = """You are an experienced psychologist specializing in helping people overcome glossophobia (the fear of public speaking). 
Please answer the following question in a warm, casual, and encouraging tone, using everyday language. Avoid technical or overly academic terms.
Use only the information provided below to answer the question, but do **not mention or refer to the context, data, or source of the information in your response**. 
If the context does not contain enough information, simply say "The information provided is not enough to answer this question directly."

Question: {question}
Context: {context}
"""

embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

url = "http://localhost:6333"

client = QdrantClient(
    url=url,
    prefer_grpc=False
)

db = Qdrant(client=client, embeddings=embeddings, collection_name="healthcare")

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

retriever = db.as_retriever(search_kwargs={"k":5})

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_response")
async def get_response(query: str = Form(...)):
    retrieved_docs = retriever.get_relevant_documents(query)
    best_doc = rerank_documents(query=query, documents=retrieved_docs)
    best_doc = best_doc[0]
    context = best_doc.page_content

    final_prompt = prompt.format(question=query, context=context)
    response = answer_prompt(final_prompt)
    response = jsonable_encoder(response)

    return response