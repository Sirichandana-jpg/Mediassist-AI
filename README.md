# 🏥 MediAssist AI

<div align="center">

### 🧠 AI-Powered Healthcare & Mental Wellness Assistant

Helping users with **Disease Prediction**, **Mental Health Analysis**, **Emotion Detection**, and **Personalized Healthcare Recommendations**.

</div>

---

## 🌟 Features

### 🩺 Physical Health Analysis

* Disease Prediction from Symptoms
* Symptom Normalization
* Severity Score Calculation
* Disease Description
* Preventive Measures
* Health Risk Assessment

### 🧠 Mental Health Analysis

* Mental Condition Prediction
* Emotion Detection using DistilBERT
* Mental Wellness Scoring
* Personalized AI Responses
* Crisis Detection

### 🤖 Smart Chatbot

* Intent Classification
* Greeting Detection
* Interactive Conversations
* Real-Time Recommendations

### 🚨 Emergency Support

* Ambulance Support
* Mental Health Helpline
* Crisis Alert Detection

---

## 🎥 Application Demo

### Chatbot UI Demo
- [View Demo](assets/Demos/chatbot_ui_demo.mp4)

### Mental Health Module Demo
- [View Demo](assets/Demos/mental_health_demo.mp4)

### Physical Health Module Demo
- [View Demo](assets/Demos/physical_health_demo.mp4)

## 🏗️ System Workflow

```text
User Query
     │
     ▼
Intent Classification
     │
 ┌───┴────────────┐
 │                │
 ▼                ▼
Physical      Mental
Health        Health
 │                │
 ▼                ▼
Disease      Emotion
Prediction   Detection
 │                │
 ▼                ▼
Recommendations AI Response
```

---

## 🛠️ Tech Stack

| Category         | Technologies              |
| ---------------- | ------------------------- |
| Programming      | Python                    |
| Frontend         | Streamlit                 |
| Machine Learning | Scikit-Learn              |
| NLP              | TF-IDF, DistilBERT        |
| Deep Learning    | Hugging Face Transformers |
| Model Storage    | Joblib                    |
| Data Processing  | Pandas, NumPy             |

---

## 📂 Project Structure

```text
PROJECT/
│
├── app.py
├── requirements.txt
│
├── chatbot/
│   ├── greetings.py
│   ├── intent_classifier.py
│   ├── predict.py
│   ├── mental_health.py
│   └── symptom_normalizer.py
│
├── models/
│   ├── physical_health_model.pkl
│   ├── mental_health_model.pkl
│   └── intent_model.pkl
│
├── DATA/
├── preprocessing/
├── assets/
└── README.md
```

---

## 🚀 Installation

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
```

---

## 📊 Machine Learning Models

### Physical Health Model

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

---

## 🎯 Future Enhancements

* 🎤 Voice Assistant
* 📄 Medical Report Analysis
* 🌍 Multilingual Support
* 📱 Mobile App
* 🏥 Doctor Appointment Integration
* 📊 User Analytics Dashboard
* 🤖 LLM Integration

---

## 🌐 Live Demo

```text
https://mediassist-ai-18011979.streamlit.app/
```

---

## 👩‍💻 Developer

### Jalagam Sirichandana

B.Tech Computer Science & Engineering

National Institute of Technology (NIT) Silchar

---

<div align="center">

⭐ If you like this project, consider giving it a star.

</div>
