# from config import *

# print("Google API Key:", GOOGLE_API_KEY[:10], "...")
# print("PDF Folder:", PDF_FOLDER)
# print("Chroma Path:", CHROMA_PATH)
# print("Embedding Model:", EMBEDDING_MODEL)
# print("LLM:", LLM_MODEL)


# from rag.loader import load_documents
# from rag.splitter import split_documents
# from rag.embedding import load_embedding
# from rag.vectorstore import create_vectorstore
# from rag.retriever import get_retriever
# from rag.chain import ask_question

# print("Loading PDFs...")

# documents = load_documents(PDF_FOLDER)

# print("Splitting Documents...")

# chunks = split_documents(documents)

# print("Loading Embedding Model...")

# embedding = load_embedding()

# print("Creating ChromaDB...")

# db = create_vectorstore(chunks, embedding)

# retriever = get_retriever(db)

# print("\nDSA Instructor Ready!\n")

# while True:

#     question = input("You : ")

#     if question.lower() == "exit":

#         break

#     answer = ask_question(

#         retriever,

#         question

#     )

#     print("\nAI :", answer)

#     print("-"*60)

from config import *


from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from ingestion.embedding import get_embedding
from ingestion.vectorstore import create_database
from ingestion.cleaner import clean_documents

from retrieval.vector_search import vector_retriever
from retrieval.bm25_search import create_bm25
from retrieval.pipeline import hybrid_search


from llm.model import get_llm
from llm.prompt import PROMPT



from langchain_core.prompts import PromptTemplate



# LOAD DATA

docs=load_documents(
    PDF_FOLDER
)
print("Document loaded successfully..")

docs = clean_documents(
        docs
)




chunks=split_documents(
    docs
)
print("Chunked successfully..")


# EMBEDDING

embedding=get_embedding()
print("embedding sucessfully..")


# VECTOR DB

db=create_database(
    chunks,
    embedding
)
print("Vector Database Created successfully..")

# RETRIEVERS

vector=vector_retriever(
    db
)
print("vector search successfully..")

bm25=create_bm25(
    chunks
)
print("bm_25 search successfully..")
print(bm25)

llm=get_llm()
print("llm successfully..")


while True:


    question=input(
        "\nAsk DSA : "
    )


    if question=="exit":
        break



    results=hybrid_search(
        question,
        vector,
        bm25

    )
    print("=" * 60)
    print(results)

    # print("=" * 60)
    # print("Retrieved Documents:", len(results))

    # for i, doc in enumerate(results):
    #     print(f"\nDocument {i+1}")
    #     print(doc.page_content[:300])
    #     print(doc.metadata)

    # print("=" * 60)
    print("Hybrid retrieval successfully..")

    context="\n\n".join(
        [
            r.page_content
            for r in results
        ]

    )
    # print(context)


    prompt=PromptTemplate(

        template=PROMPT,
        input_variables=[
            "context",
            "question"
        ]

    )


    response=llm.invoke(
        prompt.format(
            context=context,
            question=question

        )

    )


    print("=" * 60)
    print(response)


    print(
        "\nAI:",
        response.content
    )