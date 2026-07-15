def reciprocal_rank_fusion(docs1, docs2):

    scores={}
    documents={}

    for rank,doc in enumerate(docs1):

        key = doc.page_content
        documents[key] = doc
        scores[key] = scores.get(key, 0) + 1/(rank+1)

    for rank,doc in enumerate(docs2):

        key = doc.page_content
        documents[key] = doc
        scores[key] = scores.get(key, 0) + 1/(rank+1)

    result = sorted(scores, key = scores.get, reverse = True)


    return [documents[x] for x in result[:5]]