
def vector_retriever(db):

    search =  db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":5,
            "fetch_k":20,
             "lambda_mult":0.6
        }

    )

    return search