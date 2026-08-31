import streamlit as st
from transformers import pipeline
@st.cache_resource

# =========================
# LOAD LOCAL LLM
# =========================
def load_llm():
    return pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    device=-1
)
llm=load_llm()
# =========================
# GENERATE RESPONSE
# =========================

def generate_response(
    user_query,
    context
):

    messages = [

        {
            "role": "system",
            "content": """
You are MediAssist AI, a healthcare information assistant.

Your job is to provide clear, concise and supportive
health information.

Use ONLY the provided healthcare context.

Do not invent medical facts.

Do not claim that you can replace a doctor.
Do not claim that the user definitely has a disease.
Do not provide a definitive diagnosis.

If the information is insufficient, say that the user
should consult a qualified healthcare professional.

Keep the response concise and easy to understand.
"""
        },

        {
            "role": "user",
            "content": f"""
User question:

{user_query}


Healthcare context:

{context}


Using the healthcare context above, provide a helpful
and concise response to the user.
"""
        }

    ]

    result = llm(
        messages,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.3
    )

    generated = result[0]["generated_text"]

    # Chat models return the conversation
    if isinstance(generated, list):

        for message in reversed(generated):

            if message["role"] == "assistant":

                return message["content"]

    return str(generated)