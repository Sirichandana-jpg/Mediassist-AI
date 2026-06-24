from transformers import pipeline
import random
import joblib

# LOAD DISTILBERT EMOTION MODEL
from transformers import pipeline

emotion_pipeline = pipeline(
    task="text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)
mental_model = joblib.load(
    "models/mental_health_model.pkl"
)
def predict_condition(text):

    prediction = mental_model.predict(
        [text]
    )[0]

    probability = max(
        mental_model.predict_proba(
            [text]
        )[0]
    )

    return prediction, round(
        probability * 100,
        2
    )
# CRISIS KEYWORDS
crisis_words = [
    "suicide",
    "kill myself",
    "self harm",
    "die",
    "hopeless",
    "worthless"
]

# DETECT EMOTION
def detect_emotion(text):

    results = emotion_pipeline(text)

    # Handle nested output
    if isinstance(results[0], list):

        emotions = results[0]

        best_emotion = max(
            emotions,
            key=lambda x: x["score"]
        )

        return {
            "emotion": best_emotion["label"],
            "confidence": round(
                best_emotion["score"],
                3
            ),
            "all_emotions": emotions
        }

    # Handle single prediction output
    else:

        best_emotion = results[0]

        return {
            "emotion": best_emotion["label"],
            "confidence": round(
                best_emotion["score"],
                3
            ),
            "all_emotions": results
        }

# DETECT CRISIS

def detect_crisis(text):

    text = text.lower()

    for word in crisis_words:

        if word in text:
            return True

    return False

# MENTAL WELLNESS SCORE

def mental_score(emotion, confidence):

    negative_emotions = [
        "sadness",
        "fear",
        "anger"
    ]

    if emotion in negative_emotions:

        score = int(
            (1 - confidence) * 100
        )

    else:

        score = int(
            confidence * 100
        )

    return score

# ADVANCED RESPONSE SYSTEM

def mental_health_response(
    emotion,
    confidence
):

    responses = {

        "sadness": [

            "I'm sorry you're feeling sad. Talking to someone you trust may help.",

            "Please remember that difficult emotions are temporary and support is available.",

            "Take some rest, stay hydrated, and don't hesitate to seek professional support if needed."
        ],

        "fear": [

            "Anxiety can feel overwhelming sometimes. Try slow deep breathing exercises.",

            "It's okay to feel anxious. Focus on one small step at a time.",

            "Please try to rest and avoid overthinking stressful situations."
        ],

        "anger": [

            "Try taking a short break and calming your thoughts.",

            "Deep breathing and relaxation techniques may help reduce anger.",

            "Consider stepping away from stressful situations for a while."
        ],

        "joy": [

            "That's wonderful to hear. Keep taking care of yourself.",

            "Positive emotions are important for mental wellbeing.",

            "I'm glad you're feeling good today."
        ],

        "love": [

            "Emotional support and connection are important for mental health.",

            "Maintaining healthy relationships can improve wellbeing."
        ],

        "surprise": [

            "Unexpected situations can feel overwhelming. Take things slowly.",

            "Give yourself time to process unexpected emotions."
        ]
    }

    if emotion in responses:

        return random.choice(
            responses[emotion]
        )

    return (
        "Thank you for sharing your feelings."
    )

# FULL ANALYSIS

def analyze_mental_health(text):

    # Crisis detection
    crisis = detect_crisis(text)

    # Emotion detection
    result = detect_emotion(text)

    emotion = result["emotion"]

    condition, condition_confidence = (
    predict_condition(text)
)
    
    confidence = result["confidence"]

    # Wellness score
    score = mental_score(
        emotion,
        confidence
    )

    # Response
    response = mental_health_response(
        emotion,
        confidence
    )

    return {
        "condition": condition,

        "condition_confidence":condition_confidence,

        "emotion": emotion,

        "confidence": confidence,

        "mental_score": score,

        "response": response,

        "crisis_detected": crisis
    }

# Testing
if __name__ == "__main__":

    print("\n==============================")
    print(" Mental Health AI Assistant ")
    print("==============================")

    while True:

        text = input("\nYou: ")

        if text.lower() == "exit":
            break

        analysis = analyze_mental_health(
            text
        )
        print(
    "\nMental Condition:",
    analysis["condition"]
)

        print( 
          "Condition Confidence:",
          analysis["condition_confidence"],
          "%"
)
        print(
            "\nDetected Emotion:",
            analysis["emotion"]
        )

        print(
            "Confidence:",
            analysis["confidence"]
        )

        print(
            "Mental Wellness Score:",
            analysis["mental_score"]
        )

        print(
            "\nAI Response:"
        )

        print(
            analysis["response"]
        )

        # Crisis alert
        if analysis["crisis_detected"]:

            print(
                "\n⚠ Crisis Alert Detected"
            )

            print(
                "Please contact a mental health professional or trusted person immediately."
            )