from langchain_chroma import Chroma
from config import CHROMA_PATH

persist_directory = CHROMA_PATH


def create_database(chunks, embedding):

    db = Chroma.from_documents(
        documents = chunks,
        embedding = embedding,
        persist_directory =  persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )
    print(db._collection.count())

    return db


def load_database(embedding):

    db = Chroma(
        persist_directory = persist_directory,
        embedding_function = embedding,
        collection_metadata={"hnsw:space": "cosine"}
    )


    print(db._collection.count())
    return db