from config import *
import os
from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from ingestion.embedding import get_embedding
from ingestion.vectorstore import create_database, load_database
from ingestion.cleaner import clean_documents
from ingestion.vectorstore import load_database

from retrieval.vector_search import vector_retriever
from retrieval.bm25_search import create_bm25
from retrieval.pipeline import hybrid_search


from llm.model import get_llm
from llm.prompt import PROMPT

from langchain_core.prompts import PromptTemplate

persistent_directory = CHROMA_PATH 

# Load Data
docs = load_documents(PDF_FOLDER)
print("Document loaded successfully..")

# Cleaning
docs = clean_documents(docs)

chunks = split_documents(docs)
print("Chunked successfully..")

# Embedding
embedding = get_embedding()
print("embedding sucessfully..")


# Create Vector Database Before that check if vector store already exist or not 
# if exist then load vectore store
if os.path.exists(persistent_directory):
    db = load_database(embedding)
    print("Vector Database Loaded successfull..")
else:
    db = create_database(chunks, embedding)
    print("Vector Database Created successfully..")


# Retriever
vector = vector_retriever(db)
print("vector search successfully..")

bm25 = create_bm25(chunks)
print("bm_25 search successfully..")
# print(bm25)

llm = get_llm()
print("llm successfully..")

chat_history = []

def ask_question(question):

    results = hybrid_search(question, vector, bm25)
    print("Hybrid retrieval successfully..")

    context = "\n\n".join([r.page_content for r in results])
   
    history = ""
    for chat in chat_history:
        history += f"""
        user :{chat["question"]}
        assistant :{chat["answer"]}"""

    if not history:
        history = "No previous conversation"
    
    prompt = PromptTemplate(
        template=PROMPT,
        input_variables = [
            "history",
            "context",
            "question"
        ]
    )

    prompt = prompt.format(history=history, context=context, question=question)
    response = llm.invoke(prompt)
    
    answer = response.content

    chat_history.append({
        "question":question,
        "answer":answer
    })
    return answer


