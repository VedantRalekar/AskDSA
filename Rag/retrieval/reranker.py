from sentence_transformers import CrossEncoder


model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(question, documents,top_k = 5):

    pairs = []

    for doc in documents:
        pairs.append([question, doc.page_content])

    scores = model.predict(pairs)


    ranked = []

    for score,doc in zip(scores, documents):
        ranked.append((score, doc))


    ranked.sort(reverse=True, key=lambda x:x[0])



    return [doc for score,doc in ranked[:top_k]]