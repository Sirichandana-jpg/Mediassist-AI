import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(
    "DATA/clean_mental_health.csv"
)

print("Dataset Shape:", df.shape)

# =========================
# INPUT AND OUTPUT
# =========================
X = df["text"]
y = df["status"]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# PIPELINE
# =========================
mental_model = Pipeline([

    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=10000,
            ngram_range=(1,2)
        )
    ),

    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        )
    )
])

# =========================
# TRAIN MODEL
# =========================
mental_model.fit(
    X_train,
    y_train
)

print("\nTraining Completed")

# =========================
# PREDICTIONS
# =========================
predictions = mental_model.predict(
    X_test
)

# =========================
# ACCURACY
# =========================
accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "\nAccuracy:",
    round(accuracy, 4)
)

# =========================
# CLASSIFICATION REPORT
# =========================
print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# =========================
# SAVE MODEL
# =========================
joblib.dump(
    mental_model,
    r"C:\PROJECT\models\mental_health_model.pkl"
)

print(
    "\nMental Health Model Saved Successfully"
)