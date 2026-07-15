import re

def clean_documents(documents):

    for doc in documents:

        text = doc.page_content

        # Remove chapter headers
        text = re.sub(
            r"CHAPTER\s+\d+\..*?\n",
            "",
            text,
            flags=re.IGNORECASE
        )

        # Remove page numbers
        text = re.sub(
            r"\n\d+\n",
            "\n",
            text
        )

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        doc.page_content = text.strip()

    return documents