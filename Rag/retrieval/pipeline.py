from retrieval.rrf import reciprocal_rank_fusion
from retrieval.reranker import rerank_documents



def hybrid_search(question, vector, bm25):

    # Vector search
    vector_docs = vector.invoke(question)

    # Keyword search
    keyword_docs = bm25.invoke(question)

    # Combine
    rrf_docs = reciprocal_rank_fusion(vector_docs, keyword_docs, k = 60)

    # Reranking
    final_docs = rerank_documents(question, rrf_docs, top_k=5)
    
    # print("=" * 60)
    # print(final_docs)
    # print("=" * 60)

    return final_docs