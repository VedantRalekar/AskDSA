# from retrieval.rrf import reciprocal_rank_fusion



# def hybrid_search(question, vector, bm25):

#     vector_docs = vector.invoke(question)
#     keyword_docs = bm25.invoke(question)
#     final_docs=reciprocal_rank_fusion(vector_docs, keyword_docs)


#     return final_docs

from retrieval.rrf import reciprocal_rank_fusion

from retrieval.mmr import apply_mmr

from retrieval.reranker import rerank_documents



def hybrid_search(

        question,

        vector,

        bm25

):


    # Vector search

    vector_docs = vector.invoke(
        question
    )


    # Keyword search

    keyword_docs = bm25.invoke(
        question
    )



    # Combine

    fused_docs = reciprocal_rank_fusion(

        vector_docs,

        keyword_docs

    )


    # MMR

    diverse_docs = apply_mmr(

        fused_docs,

        top_k=10

    )


    # Reranking

    final_docs = rerank_documents(

        question,

        diverse_docs,

        top_k=5

    )


    return final_docs