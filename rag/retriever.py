import os

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)


# =========================
# PATH
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

VECTOR_STORE_DIR = os.path.join(
    BASE_DIR,
    "faiss_index"
)


# =========================
# LOAD EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# LOAD VECTOR STORE
# =========================

vector_store = FAISS.load_local(
    VECTOR_STORE_DIR,
    embeddings,
    allow_dangerous_deserialization=True
)


# =========================
# RETRIEVE INFORMATION
# =========================

def retrieve_information(
    query,
    k=3
):

    documents = vector_store.similarity_search(
        query,
        k=k
    )

    return documents


# =========================
# TEST
# =========================

if __name__ == "__main__":

    query = input(
        "Enter healthcare question: "
    )

    results = retrieve_information(
        query
    )

    print("\nRetrieved Information:\n")

    for document in results:

        print(
            document.page_content
        )

        print("\n--------------------\n")