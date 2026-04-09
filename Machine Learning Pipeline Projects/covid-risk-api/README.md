# 🏥 COVID-19 Risk Assessment API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📊 Overview

A production-ready REST API that assesses COVID-19 risk based on clinical symptoms using a clinical risk scoring algorithm.

### 🔥 Key Features

- ✅ **Real-time risk assessment** - Instant predictions via REST API
- ✅ **Batch processing** - Analyze multiple patients at once
- ✅ **Interactive documentation** - Auto-generated Swagger UI
- ✅ **Clinical-grade logic** - Age-weighted, symptom-based scoring

## 🏗️ Architecture
Patient Symptoms → FastAPI Endpoint → Risk Calculation → JSON Response

## 📸 Screenshots

### API Documentation
![API Docs](screenshots/api-docs.png)

### Prediction Response
![Prediction Response](screenshots/prediction-response.png)

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip package manager

### Installation

```bash
# Clone repository
git clone https://github.com/ImranDataScientist83/healthcare-covid-analysis.git
cd healthcare-covid-analysis/Machine\ Learning\ Pipeline\ Projects/covid-risk-api

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn app:app --reload --port 8000

Test the API
Open your browser to: http://127.0.0.1:8000/docs

📡 API Endpoints
Method	Endpoint	Description
GET	/	API information
GET	/health	Health check
POST	/predict	Single patient prediction
POST	/predict/batch	Batch predictions

USAGE EXAMPLE

curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 65,
    "fever": true,
    "cough": true,
    "difficulty_breathing": true,
    "contact_with_confirmed": true,
    "days_of_symptoms": 5
  }'

RESPONSE

{
  "covid_risk": "High",
  "confidence": 0.85,
  "risk_score": 100,
  "timestamp": "2026-04-09T16:18:50.995210"
}

RISK SCORING LOGIC

Factor	Weight
Age > 60	+30 pts
Fever	+15 pts
Cough	+15 pts
Breathing difficulty	+25 pts
Contact with confirmed	+20 pts
Risk Levels:

High (70+ pts) : Seek medical attention immediately

Medium (40-69 pts) : Monitor symptoms closely

Low (0-39 pts) : Continue normal precautions

🛠️ Tech Stack
Framework: FastAPI

Server: Uvicorn

Validation: Pydantic

Documentation: OpenAPI/Swagger

📝 License
MIT License

📧 Contact
Mas Imran - imranscar@hotmail.com / hp: 90064183 (whatsapp available)

- **LinkedIn:** [Your LinkedIn Profile]
- **Email:** your.email@example.com

---

⭐ Star this repository if you find it useful!
