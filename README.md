# MediAssist AI

<div align="center">

### AI-Powered Healthcare & Mental Wellness Assistant

Helping users with **Disease Prediction**, **Mental Health Analysis**, **Emotion Detection**, **RAG-based Healthcare Information Retrieval**, and **AI-Powered Healthcare Recommendations**.

</div>

---

## Features

### Physical Health Analysis

* Disease Prediction from Symptoms
* Symptom Normalization
* Severity Score Calculation
* Disease Description
* Preventive Measures
* Health Risk Assessment

### Mental Health Analysis

* Mental Condition Prediction
* Emotion Detection using DistilBERT
* Mental Wellness Scoring
* Personalized AI Responses
* Crisis Detection

### Smart Chatbot

* Intent Classification
* Greeting Detection
* Interactive Conversations
* Real-Time Recommendations
* Context-Aware Healthcare Responses

### RAG-Based Healthcare Knowledge System

* Retrieval-Augmented Generation (RAG)
* Healthcare Knowledge Base
* FAISS Vector Database
* Semantic Document Retrieval
* Healthcare Document Chunking
* Sentence Transformer Embeddings
* Context-Grounded AI Responses
* Local LLM Integration using SmolLM2
* Responses generated using retrieved healthcare information

### Emergency Support

* Ambulance Support
* Mental Health Helpline
* Crisis Alert Detection

---

## Application Demo

### Chatbot UI Demo

- [View Demo](assets/Demos/chatbot_ui_demo.mp4)

### Mental Health Module Demo

- [View Demo](assets/Demos/mental_health_demo.mp4)

### Physical Health Module Demo

- [View Demo](assets/Demos/physical_health_demo.mp4)

---

## System Workflow

```text
                         User Query
                             |
                             v
                    Intent Classification
                       /             \
                      /               \
                     v                 v
             Physical Health      Mental Health
                    |                  |
                    v                  v
             Disease Prediction   Mental Analysis
                    |                  |
                    v                  v
              Health Information   Emotion Detection
                    |                  |
                    \                 /
                     \               /
                      v             v
                    RAG Knowledge Retrieval
                             |
                             v
                      FAISS Vector Search
                             |
                             v
                  Relevant Healthcare Context
                             |
                             v
                     Local LLM (SmolLM2)
                             |
                             v
                  Grounded AI Explanation
                             |
                             v
                       User Response
```--
## RAG Architecture
MediAssist AI uses Retrieval-Augmented Generation to provide healthcare information based on a local knowledge base.
```text
Healthcare Documents
        |
        v
Document Loading
        |
        v
Text Chunking
        |
        v
Sentence Transformer Embeddings
        |
        v
FAISS Vector Index
        |
        v
User Healthcare Query
        |
        v
Semantic Similarity Search
        |
        v
Relevant Healthcare Context
        |
        v
SmolLM2 Local LLM
        |
        v
Context-Grounded Response
```--
## Tech Stack
| Category | Technologies |
| ---------------- | ------------------------- |
| Programming | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-Learn |
| NLP | TF-IDF, Natural Language Processing |
| Deep Learning | Hugging Face Transformers |
| Emotion Detection | DistilBERT |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| RAG Framework | LangChain |
| Local LLM | SmolLM2 1.7B Instruct |
| Data Processing | Pandas, NumPy |
| Model Storage | Joblib |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |--
## Project Structure
```text
Mediassist-AI
|
+-- app.py
+-- requirements.txt
+-- README.md
+-- .gitignore
|
+-- DATA
|   +-- dataset.csv
|   +-- clean_dataset.csv
|   +-- clean_mental_health.csv
|   +-- intent_dataset.csv
|   +-- Training.csv
|   +-- Testing.csv
|
+-- BIG DATA
|   +-- mental_health_combined_test.csv
|   +-- mental_heath_unbalanced.csv
|   +-- symptom_Description.csv
|   +-- symptom_precaution.csv
|   +-- Symptom_severity.csv
|
+-- chatbot
|   +-- greetings.py
|   +-- intent_classifier.py
|   +-- main_chatbot.py
|   +-- mental_health.py
|   +-- predict.py
|   +-- symptom_normalizer.py
|
+-- models
|   +-- physical_health_model.pkl
|   +-- mental_health_model.pkl
|   +-- intent_model.pkl
|   +-- train_model.py
|   +-- train_mental_model.py
|   +-- train_intent_model.py
|
+-- preprocessing
|   +-- data_loader.py
|   +-- create_intent_dataset.py
|   +-- Notebook
|       +-- rawdatapreprocess.ipynb
|       +-- Mental_Health_EDA.ipynb
|
+-- rag
|   +-- __init__.py
|   +-- documents
|   |   +-- anxiety.txt
|   |   +-- asthma.txt
|   |   +-- common_cold.txt
|   |   +-- dengue.txt
|   |   +-- depression.txt
|   |   +-- diabetes.txt
|   |   +-- emergency_warning_signs.txt
|   |   +-- gastroenteritis.txt
|   |   +-- hepatitis_a.txt
|   |   +-- hepatitis_b.txt
|   |   +-- hydration.txt
|   |   +-- hygiene.txt
|   |   +-- hypertension.txt
|   |   +-- influenza.txt
|   |   +-- malaria.txt
|   |   +-- migraine.txt
|   |   +-- nutrition.txt
|   |   +-- panic_disorder.txt
|   |   +-- physical_activity.txt
|   |   +-- pneumonia.txt
|   |   +-- sleep_health.txt
|   |   +-- stress.txt
|   |   +-- tuberculosis.txt
|   |   +-- typhoid.txt
|   |   +-- vaccination.txt
|   |
|   +-- faiss_index
|   |   +-- index.faiss
|   |   +-- index.pkl
|   |
|   +-- llm_response.py
|   +-- rag_pipeline.py
|   +-- retriever.py
|   +-- vector_store.py
|
+-- assets
    +-- logo.png
    +-- image.png
    +-- Demos
        +-- chatbot_ui_demo.mp4
        +-- mental_health_demo.mp4
        +-- physical_health_demo.mp4
```--
## Installation
### Clone Repository
```bash
git clone https://github.com/Sirichandana-jpg/Mediassist-AI.git
cd Mediassist-AI
```
### Create Virtual Environment
```bash
python -m venv venv
```
### Activate Environment
#### Windows
```bash
venv\Scripts\activate
```
#### Linux / Mac
```bash
source venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run Application
```bash
streamlit run app.py
```
### Open Browser
```text
http://localhost:8501
```--
## RAG Setup
The repository contains the healthcare documents and generated FAISS vector index required by the RAG system.
### Healthcare Documents
```text
rag/documents/
```
### Vector Store
```text
rag/faiss_index/
+-- index.faiss
+-- index.pkl
```
### Retriever
```text
rag/retriever.py
```
### RAG Pipeline
```text
rag/rag_pipeline.py
```
### Local LLM
```text
HuggingFaceTB/SmolLM2-1.7B-Instruct
```
The model is integrated through:
```text
rag/llm_response.py
```--
## Machine Learning Models
### Physical Health Model
* Naive Bayes
* TF-IDF Vectorizer
* Disease Classification
* Severity Assessment
### Mental Health Model
* TF-IDF Vectorizer
* Logistic Regression
* Mental Condition Prediction
### Emotion Detection
* DistilBERT
* Hugging Face Transformers
### Intent Classification
* Physical vs Mental Query Classification
* Intent-based chatbot routing--
## Healthcare Knowledge Base
The RAG knowledge base currently contains information related to:
* Anxiety
* Asthma
* Common Cold
* Dengue
* Depression
* Diabetes
* Emergency Warning Signs
* Gastroenteritis
* Hepatitis A
* Hepatitis B
* Hydration
* Hygiene
* Hypertension
* Influenza
* Malaria
* Migraine
* Nutrition
* Panic Disorder
* Physical Activity
* Pneumonia
* Sleep Health
* Stress
* Tuberculosis
* Typhoid
* Vaccination--
## Deployment
MediAssist AI is deployed using Streamlit Community Cloud.
### Live Application
```text
https://mediassist-ai-18011979.streamlit.app/
```
### Deployment Configuration
```text
Repository:
Sirichandana-jpg/Mediassist-AI
Branch:
main
Main file:
app.py
```--
## Safety Disclaimer
MediAssist AI is an educational healthcare information system.
It does not replace professional medical diagnosis, treatment, or consultation with a qualified healthcare professional.
Users should seek appropriate medical care for persistent, severe, or emergency symptoms.--
## Future Enhancements
* Voice Assistant
* Medical Report Analysis
* Multilingual Support
* Mobile Application
* Doctor Appointment Integration
* User Analytics Dashboard
* Improved Healthcare Knowledge Retrieval
* Expanded Healthcare Knowledge Base
* Retrieval Quality Optimization--
## Live Demo
```text
https://mediassist-ai-18011979.streamlit.app/
```--
