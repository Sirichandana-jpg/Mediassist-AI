from rag.retriever import retrieve_information
from rag.llm_response import generate_response


def rag_answer(
    user_query,
    prediction=None,
    health_type=None
):

    # =========================
    # RETRIEVE RELEVANT DOCUMENTS
    # =========================

    documents = retrieve_information(
        user_query,
        k=3
    )

    # =========================
    # BUILD HEALTHCARE CONTEXT
    # =========================

    context_parts = []

    if health_type:
        context_parts.append(
            f"Health category: {health_type}"
        )

    if prediction:
        context_parts.append(
            f"Existing ML prediction: {prediction}"
        )

    for document in documents:

        context_parts.append(
            document.page_content
        )

    context = "\n\n".join(
        context_parts
    )

    # =========================
    # GENERATE LLM RESPONSE
    # =========================

    response = generate_response(
        user_query,
        context
    )

    return response