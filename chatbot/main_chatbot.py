import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
from chatbot.greetings import (
    check_greeting
)

from chatbot.predict import (
    predict_disease
)

from chatbot.mental_health import (
    analyze_mental_health
)


from chatbot.intent_classifier import (
    predict_intent
)
from chatbot.symptom_normalizer import (
    normalize_symptoms
)

print("\n================================================")
print("      AI HEALTHCARE CHATBOT")
print(" Physical Health + Mental Health AI")
print("================================================")

print("\nType 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print(
            "\nThank you for using the chatbot."
        )

        break
    # =========================
    # GREETING CHECK
    # =========================

    is_greeting, response = (
          check_greeting(
            user_input
          )
        )

    if is_greeting:

        print(
          "\nBot:",
            response
         )
        continue
    # =========================
    # INTENT CLASSIFICATION
    # =========================

    intent, intent_confidence = (
        predict_intent(user_input)
    )

    print(
        "\nDetected Intent:",
        intent
    )

    print(
        "Intent Confidence:",
        intent_confidence,
        "%"
    )

    # =========================
    # MENTAL HEALTH
    # =========================

    if intent == "mental":

        analysis = analyze_mental_health(
            user_input
        )

        print(
            "\n========== Mental Health Analysis =========="
        )

        print(
            "Mental Condition:",
            analysis["condition"]
        )

        print(
            "Condition Confidence:",
            analysis["condition_confidence"],
            "%"
        )

        print(
            "Emotion:",
            analysis["emotion"]
        )

        print(
            "Emotion Confidence:",
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

        if analysis["crisis_detected"]:

            print(
                "\n⚠ CRISIS ALERT DETECTED"
            )

            print(
                "Please contact a trusted person or mental health professional immediately."
            )

    # =========================
    # PHYSICAL HEALTH
    # =========================

    elif intent == "physical":
        normalized_input = normalize_symptoms(
             user_input  
           )
            
        result = predict_disease(
             normalized_input
          )

        print(
            "\n========== Physical Health Analysis =========="
        )

        print(
            "Predicted Disease:",
            result["disease"]
        )

        print(
            "\nDescription:"
        )

        print(
            result["description"]
        )

        print(
            "\nSeverity Score:",
            result["severity_score"]
        )

        print(
            "Condition:",
            result["condition"]
        )

        print(
            "\nPrecautions:"
        )

        for precaution in result[
            "precautions"
        ]:

            print(
                "-",
                precaution
            )

        if result["condition"] == "Severe":

            print(
                "\n⚠ Please consult a doctor immediately."
            )

    else:

        print(
            "\nUnable to determine intent."
        )