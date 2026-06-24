import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report

# Load dataset
df = pd.read_csv(
    "DATA/intent_dataset.csv"
)

X = df["text"]
y = df["intent"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([

 (
    "tfidf",
    TfidfVectorizer(
        max_features=10000,
        ngram_range=(1, 2),
        stop_words="english"
    )
),

(
    "classifier",
    LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        random_state=42
    )
)
])

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "Accuracy:",
    accuracy
)
print(
    "\nClassification Report:\n"
)

print(
    classification_report(
        y_test,
        predictions
    )
)
joblib.dump(
    model,
    "models/intent_model.pkl"
)

print(
    "Intent model saved."
)
print(
    "\nIntent Distribution:\n"
)
print(df["intent"].value_counts())