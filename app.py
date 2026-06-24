import streamlit as st

from chatbot.greetings import check_greeting
from chatbot.intent_classifier import predict_intent
from chatbot.predict import predict_disease
from chatbot.mental_health import analyze_mental_health
from chatbot.symptom_normalizer import normalize_symptoms

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="MediAssist AI",
    page_icon="🏥",
    layout="wide"
)

# =========================
# THEME TOGGLE
# =========================

if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Light"

with st.sidebar:
    st.markdown("## Theme")
    theme_choice = st.radio(
        "Select Mode",
        ["Light", "Dark"],
        index=0 if st.session_state.theme_mode == "Light" else 1
    )
    st.session_state.theme_mode = theme_choice

# =========================
# DYNAMIC THEME COLORS
# =========================

if st.session_state.theme_mode == "Dark":
    app_bg = "#121212"
    card_bg = "#1E1E1E"
    sidebar_bg = "#1A1A1A"
    text_color = "#F5F5F5"
    subtext_color = "#D8B4FE"
    soft_bg = "#2A2238"
    border_color = "#3A3A3A"
    chat_bg = "#FFFFFF"
    chat_text = "#000000"
else:
    app_bg = "#F8FBFF"
    card_bg = "#FFFFFF"
    sidebar_bg = "#EEF5FF"
    text_color = "#2C3E50"
    subtext_color = "#B57EDC"
    soft_bg = "#F3EEFF"
    border_color = "#E0E0E0"
    chat_bg = "#FFFFFF"
    chat_text = "#000000"

# =========================
# CUSTOM CSS
# =========================

st.markdown(f"""
<style>

/* Main app background */
.stApp {{
    background-color: {app_bg};
    color: {text_color};
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background-color: {sidebar_bg};
}}

[data-testid="stSidebar"] * {{
    color: {text_color} !important;
}}

/* Alerts text */
[data-testid="stAlert"] {{
    color: {text_color} !important;
    font-weight: 600 !important;
}}

/* Info/Warning/Error text */
.stInfo, .stWarning, .stError, .stSuccess {{
    color: {text_color} !important;
}}

/* Main title */
.big-title {{
    font-size: 70px;
    font-weight: 800;
    color: #4A6CFF;
    text-align: center;
    margin-bottom: 5px;
}}

/* Subtitle */
.subtitle {{
    font-size: 26px;
    font-weight: 500;
    color: {subtext_color};
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    background-color: {soft_bg};
    margin-bottom: 20px;
}}

/* Card styling */
.card {{
    background-color: {card_bg};
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08);
    color: {text_color};
}}

/* Metrics */
[data-testid="metric-container"] {{
    background-color: {card_bg};
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.08);
    color: {text_color};
    border: 1px solid {border_color};
}}

/* Chat message container */
[data-testid="stChatMessage"] {{
    background-color: {chat_bg} !important;
    color: {chat_text} !important;
    border-radius: 15px !important;
    padding: 12px !important;
    border: 1px solid #D9D9D9 !important;
    margin-bottom: 10px !important;
}}

/* Chat message text */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] span {{
    color: {chat_text} !important;
}}

/* Input box */
[data-testid="stChatInput"] {{
    background-color: {card_bg} !important;
}}

input, textarea {{
    color: white !important;
}}

/* General markdown text */
html, body, [class*="css"] {{
    color: {text_color};
}}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("assets/image.png", width=450)

st.markdown(
    f"""
    <div style="
    background:{soft_bg};
    color:#A06CD5;
    font-size:24px;
    font-weight:600;
    text-align:center;
    padding:15px;
    border-radius:15px;
    margin-bottom:20px;
    ">
    AI-powered healthcare assistant for physical and mental wellness
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.image("assets/logo.png", width=450)

    st.markdown("""
<h2 style="
color:#6A1B9A;
text-align:center;
font-weight:800;
">
PREDICT • PREVENT • PROSPER •
</h2>
""", unsafe_allow_html=True)

    st.markdown(f"""
<div style="color:{text_color};">

<h3> Features</h3>

✔ Physical Disease Prediction<br>
✔ Mental Health Analysis<br>
✔ Emotion Detection<br>
✔ Crisis Detection<br>
✔ Intent Classification<br>
✔ Personalized Recommendations

</div>
""", unsafe_allow_html=True)
with st.sidebar:
   st.markdown("## BMI Calculator")

   height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=1.70
)

   weight = st.number_input(
    "Weight (kg)",
    min_value=10,
    max_value=300,
    value=70
)
   bmi = weight / (height ** 2)

   st.metric(
    "BMI",
    round(bmi, 2)
)
with st.sidebar:
    st.markdown("##  Emergency Support")

    st.info("""Ambulance: 108

Emergency: 112

Tele-MANAS: 14416
24×7 Mental Health Helpline
""")

    st.caption("For emergencies, seek immediate professional help.")

# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(
            message["content"],
            unsafe_allow_html=True
        )

# =========================
# USER INPUT
# =========================

user_input = st.chat_input("Describe your symptoms or feelings...")

if user_input:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(
            f"""
            <div style="
                background-color: white;
                color: black;
                padding: 12px;
                border-radius: 12px;
                border: 1px solid #D9D9D9;
            ">
                {user_input}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # GREETING DETECTION
    # =========================

    is_greeting, greeting_response = check_greeting(user_input)

    if is_greeting:
        assistant_reply = greeting_response

        with st.chat_message("assistant"):
            st.markdown(
                f"""
                <div style="
                    background-color: white;
                    color: black;
                    padding: 12px;
                    border-radius: 12px;
                    border: 1px solid #D9D9D9;
                ">
                    {assistant_reply}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

    else:
        intent, confidence = predict_intent(user_input)

        with st.chat_message("assistant"):
            st.markdown(
                f"""
                <div style="
                    background-color: white;
                    color: black;
                    padding: 12px;
                    border-radius: 12px;
                    border: 1px solid #D9D9D9;
                    margin-bottom: 10px;
                ">
                    <b>Intent:</b> {intent}<br>
                    <b>Confidence:</b> {confidence}%
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(int(confidence))

            # =========================
            # MENTAL HEALTH
            # =========================

            if intent == "mental":
                analysis = analyze_mental_health(user_input)

                mental_reply = f"""
<b> Mental Condition:</b> {analysis['condition']}<br><br>
<b>Condition Confidence:</b> {analysis['condition_confidence']}%<br>
<b>Emotion:</b> {analysis['emotion']}<br>
<b>Mental Wellness Score:</b> {analysis['mental_score']}<br><br>
<b> AI Response:</b><br>
{analysis['response']}
"""

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": mental_reply
                    }
                )

                st.markdown(
                    f"""
                    <div style="
                        background-color:white;
                        padding:15px;
                        border-radius:12px;
                        border:1px solid #D9D9D9;
                        font-size:18px;
                        color:#2C3E50;
                        margin-bottom:10px;
                    ">
                    <b> Mental Condition:</b> {analysis['condition']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Condition Confidence",
                        f"{analysis['condition_confidence']}%"
                    )

                with col2:
                    st.metric(
                        "Emotion",
                        analysis["emotion"]
                    )

                with col3:
                    st.metric(
                        "Wellness Score",
                        analysis["mental_score"]
                    )

                st.markdown(
                    f"""
                    <div style="
                        background-color:white;
                        padding:20px;
                        border-radius:15px;
                        border:1px solid #D9D9D9;
                        color:#2C3E50;
                        font-size:18px;
                        margin-top:15px;
                    ">
                    <b> AI Response</b><br><br>
                    {analysis["response"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if analysis["crisis_detected"]:
                    st.error("⚠ Crisis Alert Detected")

            # =========================
            # PHYSICAL HEALTH
            # =========================

            elif intent == "physical":
                normalized_input = normalize_symptoms(user_input)
                result = predict_disease(normalized_input)

                physical_reply = f"""
<b>Predicted Disease:</b> {result['disease']}<br><br>
<b>Condition:</b> {result['condition']}<br>
<b>Severity Score:</b> {result['severity_score']}<br><br>
<b>Description:</b><br>
{result['description']}<br><br>
<b>Precautions:</b><br>
{"<br>".join([f"- {p}" for p in result["precautions"]])}
"""

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": physical_reply
                    }
                )

                st.markdown(
                    f"""
                    <div style="
                        background-color:white;
                        color:black;
                        padding:15px;
                        border-radius:12px;
                        border:1px solid #D9D9D9;
                        margin-bottom:10px;
                    ">
                    <b>Predicted Disease:</b> {result['disease']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div style="
                        background-color:white;
                        color:black;
                        padding:15px;
                        border-radius:12px;
                        border:1px solid #D9D9D9;
                        margin-bottom:10px;
                    ">
                    {result["description"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.success(
                    f"Predicted Disease: {result['disease']}"
                )

                st.metric(
                    "Prediction Confidence",
                    f"{result['confidence']}%"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Severity Score",
                        result["severity_score"]
                    )

                with col2:
                    st.metric(
                        "Condition",
                        result["condition"]
                    )

                st.write("### Precautions")

                for precaution in result["precautions"]:
                    st.markdown(
                        f"""
                        <div style="
                            background-color:white;
                            color:black;
                            padding:10px;
                            border-radius:10px;
                            border:1px solid #D9D9D9;
                            margin-bottom:8px;
                        ">
                        {precaution}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                st.write("### Top Predictions")

                for disease, prob in result["top_predictions"]:

                   st.write(
                       f"• {disease} ({prob}%)"
                   )
                if result["condition"] == "Severe":
                    st.error("⚠ Please consult a doctor immediately.")

# =========================
# FOOTER
# =========================

st.markdown(f"""
<div style="
padding:20px;
color:{text_color};
">

<h3 style="color:{text_color};">
🛠 Technologies Used
</h3>

<ul style="color:{text_color}; font-size:18px;">
<li>Python</li>
<li>Streamlit</li>
<li>Scikit-Learn</li>
<li>TF-IDF</li>
<li>Logistic Regression</li>
<li>Naive Bayes</li>
<li>Hugging Face Transformers</li>
<li>DistilBERT</li>
<li>Natural Language Processing (NLP)</li>
</ul>

</div>
""", unsafe_allow_html=True)
