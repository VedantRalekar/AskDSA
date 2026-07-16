from langchain_chroma import Chroma
from config import CHROMA_PATH

def create_database(chunks, embedding):


    db = Chroma.from_documents(
        documents = chunks,
        embedding = embedding,
        persist_directory = CHROMA_PATH
    )

    return db