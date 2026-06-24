SYMPTOM_MAP = {

    "stomach pain": "stomach_pain",
    "skin rash": "skin_rash",
    "high fever": "fever",
    "chest pain": "chest_pain",
    "joint pain": "joint_pain",
    "back pain": "back_pain",
    "head ache": "headache",
    "loss of appetite": "loss_of_appetite",
    "yellow skin": "yellowish_skin",
    "runny nose": "continuous_sneezing",
    "black heads": "blackheads",
    "muscle pain": "muscle_pain"
}

def normalize_symptoms(text):

    text = text.lower()

    for phrase, symptom in SYMPTOM_MAP.items():

        text = text.replace(
            phrase,
            symptom
        )

    return text