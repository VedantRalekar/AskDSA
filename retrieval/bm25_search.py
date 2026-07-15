from langchain_community.retrievers import BM25Retriever

def create_bm25(chunks):


    retriever=BM25Retriever.from_documents(
        chunks
    )
    retriever.k=5


    return retriever