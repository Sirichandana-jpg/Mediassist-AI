import joblib

intent_model = joblib.load(
    "models/intent_model.pkl"
)

def predict_intent(text):

    prediction = intent_model.predict(
        [text]
    )[0]

    confidence = max(
        intent_model.predict_proba(
            [text]
        )[0]
    ) * 100

    return prediction, round(confidence, 2)
