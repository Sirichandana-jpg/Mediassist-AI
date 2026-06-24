import pandas as pd

# =========================
# MAIN DATASET
# =========================
main_df = pd.read_csv("DATA/dataset.csv")

# =========================
# DESCRIPTION DATA
# =========================
desc_df = pd.read_csv(
    "BIG DATA/symptom_Description.csv"
)

description_dict = dict(
    zip(desc_df.iloc[:,0], desc_df.iloc[:,1])
)

# =========================
# PRECAUTION DATA
# =========================
prec_df = pd.read_csv(
    "BIG DATA/symptom_precaution.csv"
)

precaution_dict = {}

for _, row in prec_df.iterrows():
    disease = row.iloc[0]
    precautions = row[1:].dropna().tolist()
    precaution_dict[disease] = precautions

# =========================
# SEVERITY DATA
# =========================
sev_df = pd.read_csv(
    "BIG DATA/Symptom_severity.csv"
)

severity_dict = dict(
    zip(sev_df.iloc[:,0], sev_df.iloc[:,1])
)

# =========================
# PRINT RESULTS
# =========================
print("Main dataset:", main_df.shape)
print("Descriptions:", len(description_dict))
print("Precautions:", len(precaution_dict))
print("Severity:", len(severity_dict))