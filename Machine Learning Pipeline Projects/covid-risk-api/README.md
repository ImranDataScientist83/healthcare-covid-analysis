# COVID-19 Risk Assessment API

## Overview
FastAPI-based API for assessing COVID-19 risk based on clinical symptoms.

## API Endpoints
- `GET /` - API information
- `GET /health` - Health check
- `POST /predict` - Single patient prediction
- `POST /predict/batch` - Batch predictions

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
