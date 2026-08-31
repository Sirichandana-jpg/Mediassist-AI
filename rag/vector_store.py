import os

from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)


# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DOCUMENTS_DIR = os.path.join(
    BASE_DIR,
    "documents"
)

VECTOR_STORE_DIR = os.path.join(
    BASE_DIR,
    "faiss_index"
)


# =========================
# LOAD TXT FILES
# =========================

documents = []

for filename in os.listdir(DOCUMENTS_DIR):

    if filename.endswith(".txt"):

        filepath = os.path.join(
            DOCUMENTS_DIR,
            filename
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": filename
                }
            )
        )


# =========================
# CHECK DOCUMENTS
# =========================

print(
    f"Documents loaded: {len(documents)}"
)


# =========================
# SPLIT DOCUMENTS
# =========================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(
    documents
)

print(
    f"Chunks created: {len(chunks)}"
)


# =========================
# CREATE EMBEDDINGS
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# CREATE FAISS DATABASE
# =========================

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)


# =========================
# SAVE VECTOR DATABASE
# =========================

vector_store.save_local(
    VECTOR_STORE_DIR
)


print(
    "FAISS vector store created successfully."
)