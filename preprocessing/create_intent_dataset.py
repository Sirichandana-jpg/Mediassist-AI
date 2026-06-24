import pandas as pd

# =========================
# LOAD MENTAL DATA
# =========================
mental_df = pd.read_csv(
    "DATA/clean_mental_health.csv"
)

# Keep text column
mental_df = mental_df[["text"]]

# Add intent label
mental_df["intent"] = "mental"

# =========================
# LOAD PHYSICAL DATA
# =========================
import random

templates = [

    "I have {}",

    "I am suffering from {}",

    "I am experiencing {}",

    "These symptoms are bothering me: {}",

    "I feel {}",

    "My symptoms include {}"
]
physical_df = pd.read_csv(
    "DATA/clean_dataset.csv"
)

physical_df = physical_df[["symptoms_text"]]
physical_df["symptoms_text"] = (
    physical_df["symptoms_text"]
    .fillna("")
    .astype(str)
)
def convert_to_sentence(text):

    if pd.isna(text) or text.strip() == "":
        return None

    symptoms = str(text).replace("_", " ")

    template = random.choice(
        templates
    )

    return template.format(
        symptoms
    )


physical_df["text"] = physical_df[
    "symptoms_text"
].apply(
    convert_to_sentence
)
physical_df = physical_df.dropna(
    subset=["text"])
physical_df = physical_df[
    ["text"]
]

physical_df["intent"] = "physical"
# =========================
# BALANCE DATASET
# =========================
"""
physical_df = physical_df.sample(
    n=5000,
    replace=True,
    random_state=42
)

mental_df = mental_df.sample(
    n=5000,
    random_state=42
)"""
# =========================
# COMBINE DATASETS
# =========================
intent_df = pd.concat(
    [mental_df, physical_df],
    ignore_index=True
)

# Remove missing values
intent_df = intent_df.dropna()


# Shuffle dataset
intent_df = intent_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save
intent_df.to_csv(
    "DATA/intent_dataset.csv",
    index=False
)

print(
    "Intent dataset created successfully."
)

print(
    "Shape:",
    intent_df.shape
)

print(
    intent_df["intent"].value_counts()
)