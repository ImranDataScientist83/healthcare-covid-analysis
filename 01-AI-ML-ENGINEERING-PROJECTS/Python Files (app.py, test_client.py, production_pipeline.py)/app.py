
# app.py - Production API for Churn Prediction
import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime
import uvicorn

# Load model and scaler
model = joblib.load('final_tuned_model.pkl')
scaler = joblib.load('final_scaler.pkl')

# Load feature columns
feature_cols = ['age', 'annual_income', 'purchase_frequency', 'avg_order_value', 'tenure_months', 'customer_satisfaction', 'num_support_tickets', 'total_spend', 'days_since_last_purchase', 'spend_per_purchase', 'avg_monthly_spend', 'customer_lifetime_value', 'engagement_score', 'churn_risk_score', 'recency_score', 'frequency_score', 'monetary_score', 'age_income_interaction', 'support_satisfaction', 'device_type_Desktop', 'device_type_Mobile', 'device_type_Tablet', 'region_Central', 'region_East', 'region_North', 'region_South', 'region_West', 'membership_tier_Bronze', 'membership_tier_Gold', 'membership_tier_Platinum', 'membership_tier_Silver', 'age_group_18-25', 'age_group_26-35', 'age_group_36-50', 'age_group_51-65', 'age_group_65+', 'income_tier_Low', 'income_tier_Medium', 'income_tier_High', 'income_tier_Very High', 'device_type_target_encoded', 'region_target_encoded', 'membership_tier_target_encoded', 'age_group_target_encoded', 'income_tier_target_encoded', 'device_type_freq', 'region_freq', 'membership_tier_freq', 'age_group_freq', 'income_tier_freq', 'purchase_day', 'purchase_month', 'day_sin', 'day_cos', 'month_sin', 'month_cos']

# Create FastAPI app
app = FastAPI(
    title="Churn Prediction API",
    description="ML model for predicting customer churn",
    version="1.0.0"
)

# Define request schema
class PredictionRequest(BaseModel):
    features: Dict[str, Any] = Field(..., description="Customer features for prediction")
    
    class Config:
        json_schema_extra = {
            "example": {
                "features": {
                    "age": 35,
                    "annual_income": 50000,
                    "purchase_frequency": 5,
                    "avg_order_value": 75,
                    "tenure_months": 12,
                    "customer_satisfaction": 4.2,
                    "num_support_tickets": 1,
                    "total_spend": 3750,
                    "days_since_last_purchase": 15
                }
            }
        }

class BatchPredictionRequest(BaseModel):
    customers: List[Dict[str, Any]]

# Define response schema
class PredictionResponse(BaseModel):
    customer_id: int = None
    churn_prediction: int
    churn_probability: float
    risk_level: str
    prediction_timestamp: str

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "Churn Prediction API is running",
        "model": "XGBoost (Random Search Tuned)",
        "f1_score": 1.0,
        "endpoints": ["/predict", "/predict/batch", "/health", "/features"]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/features")
def get_features():
    return {
        "feature_names": feature_cols,
        "num_features": len(feature_cols),
        "expected_format": "Dictionary with these keys"
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([request.features])
        
        # Ensure all required columns exist
        for col in feature_cols:
            if col not in input_df.columns:
                input_df[col] = 0
        
        # Select only required features
        input_df = input_df[feature_cols]
        
        # Scale features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        
        # Determine risk level
        if probability >= 0.7:
            risk_level = "High"
        elif probability >= 0.3:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        return PredictionResponse(
            churn_prediction=int(prediction),
            churn_probability=float(probability),
            risk_level=risk_level,
            prediction_timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/batch")
def predict_batch(request: BatchPredictionRequest):
    try:
        results = []
        for i, customer in enumerate(request.customers):
            input_df = pd.DataFrame([customer])
            for col in feature_cols:
                if col not in input_df.columns:
                    input_df[col] = 0
            input_df = input_df[feature_cols]
            input_scaled = scaler.transform(input_df)
            
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0][1]
            
            if probability >= 0.7:
                risk_level = "High"
            elif probability >= 0.3:
                risk_level = "Medium"
            else:
                risk_level = "Low"
            
            results.append({
                "customer_id": i,
                "churn_prediction": int(prediction),
                "churn_probability": float(probability),
                "risk_level": risk_level
            })
        
        return {
            "predictions": results,
            "total_processed": len(results),
            "timestamp": datetime.now().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
