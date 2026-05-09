from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import numpy as np
import uvicorn

app = FastAPI(
    title="ML-powered COVID Risk Assessment API",
    description="Production-ready API for COVID-19 risk prediction based on clinical symptoms",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Request/Response Models
class PatientData(BaseModel):
    age: int
    fever: bool
    cough: bool
    fatigue: bool
    difficulty_breathing: bool
    contact_with_confirmed: bool
    days_of_symptoms: int
    
    class Config:
        schema_extra = {
            "example": {
                "age": 45,
                "fever": True,
                "cough": True,
                "fatigue": False,
                "difficulty_breathing": False,
                "contact_with_confirmed": True,
                "days_of_symptoms": 3
            }
        }

class PredictionResponse(BaseModel):
    covid_risk: str
    confidence: float
    risk_score: int
    recommendation: str
    symptoms_checklist: dict

# Risk Calculation Engine
def calculate_risk(patient: PatientData):
    risk_score = 0
    
    # Age factor
    if patient.age > 60:
        risk_score += 30
    elif patient.age > 50:
        risk_score += 20
    elif patient.age > 40:
        risk_score += 10
    
    # Symptoms weighting
    if patient.fever:
        risk_score += 15
    if patient.cough:
        risk_score += 15
    if patient.fatigue:
        risk_score += 10
    if patient.difficulty_breathing:
        risk_score += 25
    if patient.contact_with_confirmed:
        risk_score += 20
    
    # Duration factor
    risk_score += min(patient.days_of_symptoms * 2, 20)
    
    # Decision logic
    if risk_score >= 70:
        risk = "High"
        confidence = 0.85
        recommendation = "⚠️ Seek medical attention immediately. Isolate and get tested."
    elif risk_score >= 40:
        risk = "Medium"
        confidence = 0.70
        recommendation = "📋 Monitor symptoms. Consider getting tested."
    else:
        risk = "Low"
        confidence = 0.90
        recommendation = "✅ Continue precautions. Watch for symptoms."
    
    return risk, confidence, min(risk_score, 100), recommendation

# API Endpoints
@app.get("/")
def root():
    return {
        "message": "ML-powered COVID risk assessment API",
        "status": "operational",
        "version": "2.0.0",
        "endpoints": ["/predict", "/health", "/info", "/docs", "/predict/batch"]
    }

@app.get("/health")
def health():
    return {"status": "healthy", "model": "clinical-risk-score"}

@app.get("/info")
def info():
    return {
        "api_name": "COVID Risk Assessment System",
        "model_type": "Clinical Risk Scoring Algorithm",
        "features": ["age", "fever", "cough", "fatigue", "difficulty_breathing", 
                    "contact_with_confirmed", "days_of_symptoms"],
        "risk_levels": ["Low", "Medium", "High"]
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(patient: PatientData):
    try:
        risk, confidence, risk_score, recommendation = calculate_risk(patient)
        
        return PredictionResponse(
            covid_risk=risk,
            confidence=confidence,
            risk_score=risk_score,
            recommendation=recommendation,
            symptoms_checklist={
                "fever": patient.fever,
                "cough": patient.cough,
                "fatigue": patient.fatigue,
                "breathing_difficulty": patient.difficulty_breathing,
                "contact_with_confirmed": patient.contact_with_confirmed
            }
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/batch")
async def predict_batch(patients: List[PatientData]):
    results = []
    for patient in patients:
        risk, confidence, risk_score, recommendation = calculate_risk(patient)
        results.append({
            "patient": patient.dict(),
            "covid_risk": risk,
            "confidence": confidence,
            "risk_score": risk_score,
            "recommendation": recommendation
        })
    return {
        "batch_size": len(patients),
        "results": results,
        "summary": {
            "high_risk": sum(1 for r in results if r["covid_risk"] == "High"),
            "medium_risk": sum(1 for r in results if r["covid_risk"] == "Medium"),
            "low_risk": sum(1 for r in results if r["covid_risk"] == "Low")
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
