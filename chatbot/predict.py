import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

import joblib

from preprocessing.data_loader import (
    description_dict,
    precaution_dict,
    severity_dict
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load(
    "models/physical_health_model.pkl"
)

# =========================
# PHYSICAL HEALTH FUNCTION
# =========================
def predict_disease(symptoms):

  prediction = model.predict(
        [symptoms]
    )[0]
  probabilities = model.predict_proba(
        [symptoms]
    )[0]
    
  confidence = round(
       max(probabilities) * 100,
    2
    )
  classes = model.classes_

  top_indices = probabilities.argsort()[-3:][::-1]

  top_predictions = []

  for i in top_indices:

      top_predictions.append(
        (
            classes[i],
            round(
                probabilities[i] * 100,
                2
            )
        )
    )

    # =========================
    # DESCRIPTION
    # =========================
      description = description_dict.get(
        prediction,
        "No description available."
    )

    # =========================
    # PRECAUTIONS
    # =========================
      precautions = precaution_dict.get(
        prediction,
        []
    )

    # =========================
    # SEVERITY ANALYSIS
    # =========================

      total_severity = 0

      normalized_text = symptoms.lower()

      for symptom, score in severity_dict.items():

        if symptom in normalized_text:

         total_severity += int(score)

    # =========================
    # CONDITION LEVEL
    # =========================
      if total_severity < 5:

        condition = "Mild"

      elif total_severity < 10:

        condition = "Moderate"

      else:

        condition = "Severe"

    # =========================
    # RETURN EVERYTHING
    # =========================
  return {

        "disease": prediction, 

        "confidence": confidence,

        "description": description,

        "precautions": precautions,

        "severity_score": total_severity,

        "condition": condition,

        "top_predictions": top_predictions
    }

# =========================
# TESTING
# =========================
if __name__ == "__main__":

    while True:

        symptoms = input(
            "\nEnter symptoms: "
        )

        if symptoms.lower() == "exit":
            break

        result = predict_disease(
            symptoms
        )

        print(
            "\nDisease:",
            result["disease"]
        )

        print(
            "\nDescription:"
        )

        print(
            result["description"]
        )

        print(
            "\nPrecautions:"
        )

        for p in result["precautions"]:

            print("-", p)

        print(
            "\nSeverity Score:",
            result["severity_score"]
        )

        print(
            "Condition:",
            result["condition"]
        )