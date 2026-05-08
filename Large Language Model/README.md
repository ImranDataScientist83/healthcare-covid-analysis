# 🏥 ML-Powered COVID Risk Assessment API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.3-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

A production-ready REST API that assesses COVID-19 risk based on clinical symptoms using a rule-based clinical scoring algorithm. This project demonstrates **end-to-end ML system deployment** skills,

### 🔥 Key Features

- ✅ **Real-time risk assessment** - Instant predictions via REST API
- ✅ **Batch processing** - Analyze multiple patients at once
- ✅ **Interactive documentation** - Auto-generated Swagger UI
- ✅ **Clinical-grade logic** - Age-weighted, symptom-based scoring
- ✅ **Production ready** - FastAPI with automatic validation

```text
## 🏗️ Architecture
┌─────────────────┐
│ Client/Frontend│
└────────┬────────┘
│ HTTP Request
▼
┌─────────────────┐
│ FastAPI App │ ← /predict, /predict/batch
│ (app.py) │
└────────┬────────┘
│
▼
┌─────────────────┐
│ Risk Calculation│
│ Engine │
│ • Age weighting │
│ • Symptom scoring│
│ • Duration factor│
└────────┬────────┘
│
▼
┌─────────────────┐
│ Decision Logic │
│ High/Medium/Low │
└────────┬────────┘
│
▼
┌─────────────────┐
│ JSON Response │
└─────────────────┘

```
## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

```bash
# Clone repository
git clone https://github.com/ImranDataScientist83/healthcare-covid-analysis.git
cd healthcare-covid-analysis

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn app:app --reload --port 8001
```

### Test the API
Open your browser to: `http://127.0.0.1:8001/docs`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/info` | Model details |
| POST | `/predict` | Single patient prediction |
| POST | `/predict/batch` | Batch predictions |

## 💻 Usage Examples

### Single Prediction

curl -X POST "http://127.0.0.1:8001/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 65,
    "fever": true,
    "cough": true,
    "fatigue": true,
    "difficulty_breathing": true,
    "contact_with_confirmed": true,
    "days_of_symptoms": 7
  }'

**Response:**

{
  "covid_risk": "High",
  "confidence": 0.85,
  "risk_score": 100,
  "recommendation": "⚠️ Seek medical attention immediately",
  "symptoms_checklist": {
    "fever": true,
    "cough": true,
    "fatigue": true,
    "breathing_difficulty": true
  }
}

### Batch Prediction

curl -X POST "http://127.0.0.1:8001/predict/batch" \
  -H "Content-Type: application/json" \
  -d '[
    {"age": 25, "fever": false, "cough": false, "fatigue": false, "difficulty_breathing": false, "contact_with_confirmed": false, "days_of_symptoms": 0},
    {"age": 70, "fever": true, "cough": true, "fatigue": true, "difficulty_breathing": true, "contact_with_confirmed": true, "days_of_symptoms": 5}
  ]'

## 📊 Risk Scoring Logic

| Factor | Weight | Maximum |
|--------|--------|---------|
| Age > 60 | 30 pts | 30 |
| Fever | 15 pts | 15 |
| Cough | 15 pts | 15 |
| Fatigue | 10 pts | 10 |
| Breathing difficulty | 25 pts | 25 |
| Contact with confirmed | 20 pts | 20 |
| Days of symptoms | 2 pts/day | 20 |

**Risk Levels:**
- **High (70+ pts)**: Immediate medical attention required
- **Medium (40-69 pts)**: Monitor symptoms, consider testing
- **Low (0-39 pts)**: Continue standard precautions

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic v2
- **Documentation**: OpenAPI/Swagger

## 📸 Screenshots

![API Documentation](screenshots/api-docs.png)
*Interactive Swagger UI documentation*

![Prediction Response](screenshots/prediction-response.png)
*Sample API response*

## 📝 License

MIT License

## 📧 Contact

Imran - imranscar@hotmail.com

Project Link: [https://github.com/ImranDataScientist83/healthcare-covid-analysis](https://github.com/ImranDataScientist83/healthcare-covid-analysis)
