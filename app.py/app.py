from fastapi import FastAPI
import joblib

app = FastAPI()

# Load model
model = joblib.load("covid_model.pkl")

@app.get("/")
def home():
    return {"message": "COVID Prediction API is running"}

@app.get("/predict")
def predict(new_cases: float, new_deaths: float, positivity_rate: float, vaccination_rate: float):
    features = [[new_cases, new_deaths, positivity_rate, vaccination_rate]]
    pred = model.predict(features)
    return {
        "input": {
            "new_cases": new_cases,
            "new_deaths": new_deaths,
            "positivity_rate": positivity_rate,
            "vaccination_rate": vaccination_rate
        },
        "prediction": float(pred[0])
    }
