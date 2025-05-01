# Wicara Chatbot v2
![WICARA cover](https://github.com/user-attachments/assets/61b74f44-5a25-41cf-bb6b-6a735311fe7c)

## Overview

**Wicara** is an application designed to help individuals overcome **glossophobia**—the fear of public speaking—by providing both theoretical lessons and practical training evaluated by AI.

To enhance user experience, this project includes the development of a **chatbot** that can be integrated into the application. The chatbot allows users to directly ask questions related to glossophobia, aiming to improve user interaction and deliver fast, accurate answers. This is a development of the first version of the project, so there are some improvements.

---

## 🚀 Technologies Used

- **LangChain** – Framework for building LLM-powered applications  
- **Qdrant** – Vector database for efficient semantic search  
- **PubMedBERT** – Embedding model trained on biomedical texts  
- **ms-marco-MiniLM-L-6-v2** – Lightweight cross-encoder for re-ranking  
- **OpenAI** – Robust Large Language Model (LLM)
- **FastAPI** – High-performance web framework for API backend  
- **Bootstrap** – Frontend framework for responsive UI

---
## ✅ Features

- Multi-agent architecture  
- Data preprocessing 
- Chunking with semantic search  
- Cross-encoder based re-ranking for better answer relevance
  
## 📈 Improvements

- Implement modular code for project sustainability
- Use OpenAI for LLM, so that the answers are more creative and do not simply continue chunking.
- Increase the amount of data/journals used, so as to answer critical questions that cannot yet be answered 

---

## 🔁 Workflow

1. Data preprocessing
2. Semantic chunking of medical text
3. Embedding generation using PubMedBERT
4. Vector storage and retrieval with Qdrant
5. Re-ranking using ms-marco-MiniLM-L-6-v2
6. Response generation using OpenAI LLM

---

## 📉 Current Limitations

- Limited data sources prevent the retrieval agent from retrieving the maximum amount of information, resulting in unanswered questions.

---

## 🔧 Future Improvements

- Trying out more reliable retrieval and reranking agents
- Translate non-English journals

