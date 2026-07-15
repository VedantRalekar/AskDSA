from langchain_community.document_loaders import PyPDFLoader
import os

def load_documents(folder):

    documents = []

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder, file))
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = file
                doc.metadata["type"] = "DSA"

            documents.extend(docs)
    
    print(
        "Pages Loaded:",
        len(documents)
    )

    return documents