def reciprocal_rank_fusion(docs1, docs2, k=60):

    scores = {}
    documents = {}

    # Process first retriever
    for rank, doc in enumerate(docs1, 1):

        key = doc.page_content

        documents[key] = doc
        scores[key] = scores.get(key, 0) + 1 / (k + rank)

    # Process second retriever
    for rank, doc in enumerate(docs2, 1):

        key = doc.page_content

        documents[key] = doc
        scores[key] = scores.get(key, 0) + 1 / (k + rank)

    result = sorted(scores, key = scores.get, reverse = True)

    return [documents[x] for x in result[:5]]