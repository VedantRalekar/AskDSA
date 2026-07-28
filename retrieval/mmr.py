from langchain_core.documents import Document



def apply_mmr(documents, top_k=5):

   #filtering and Removes very similar chunks.

    selected = []
    for doc in documents:
        is_duplicate = False
        for selected_doc in selected:

            if similarity(doc.page_content, selected_doc.page_content) > 0.8:
                is_duplicate=True
                break

        if not is_duplicate:
            selected.append(doc)

        if len(selected)==top_k:
            break

    return selected




def similarity(text1,text2):

    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    intersection = len(words1 & words2)

    union = len(words1 | words2)

    if union == 0:
        return 0


    return intersection/union