import joblib

intent_model = joblib.load(
    "models/intent_model.pkl"
)


# =========================
# PHYSICAL HEALTH KEYWORDS
# =========================

PHYSICAL_KEYWORDS = [
    "period pain",
    "period cramps",
    "menstrual pain",
    "menstrual cramps",
    "menstruation",
    "cramps",
    "abdominal pain",
    "stomach pain",
    "stomach ache",
    "belly pain",
    "pelvic pain",
    "back pain",
    "chest pain",
    "headache",
    "fever",
    "cough",
    "cold",
    "sore throat",
    "vomiting",
    "nausea",
    "diarrhea",
    "diarrhoea",
    "rash",
    "dizziness",
    "breathing problem",
    "difficulty breathing",
    "shortness of breath",
    "body pain",
    "joint pain",
    "muscle pain",
    "tooth pain"
]


def predict_intent(text):

    text_lower = text.lower()

    # =========================
    # PHYSICAL OVERRIDE
    # =========================

    for keyword in PHYSICAL_KEYWORDS:

        if keyword in text_lower:

            return "physical", 99.0

    # =========================
    # ML INTENT PREDICTION
    # =========================

    prediction = intent_model.predict(
        [text]
    )[0]

    confidence = max(
        intent_model.predict_proba(
            [text]
        )[0]
    ) * 100

    return prediction, round(confidence, 2)