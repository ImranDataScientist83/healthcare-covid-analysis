# test_client.py - Test the API
import requests
import json

# API endpoint
BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health: {response.json()}")

def test_features():
    """Test features endpoint"""
    response = requests.get(f"{BASE_URL}/features")
    print(f"Features: {response.json()['num_features']} features")

def test_single_prediction():
    """Test single prediction"""
    data = {
        "features": {
            "age": 45,
            "annual_income": 65000,
            "purchase_frequency": 3,
            "avg_order_value": 120,
            "tenure_months": 8,
            "customer_satisfaction": 2.5,
            "num_support_tickets": 4,
            "total_spend": 5000,
            "days_since_last_purchase": 45
        }
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Single Prediction: {response.json()}")

def test_batch_prediction():
    """Test batch prediction"""
    data = {
        "customers": [
            {
                "age": 30,
                "annual_income": 50000,
                "purchase_frequency": 10,
                "avg_order_value": 80,
                "tenure_months": 24,
                "customer_satisfaction": 4.5,
                "num_support_tickets": 0,
                "total_spend": 8000,
                "days_since_last_purchase": 5
            },
            {
                "age": 55,
                "annual_income": 75000,
                "purchase_frequency": 2,
                "avg_order_value": 200,
                "tenure_months": 3,
                "customer_satisfaction": 2.0,
                "num_support_tickets": 6,
                "total_spend": 1500,
                "days_since_last_purchase": 120
            }
        ]
    }
    
    response = requests.post(f"{BASE_URL}/predict/batch", json=data)
    print(f"Batch Prediction: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    print("="*50)
    print("Testing Churn Prediction API")
    print("="*50)
    
    try:
        test_health()
        test_features()
        print("\n--- Single Prediction ---")
        test_single_prediction()
        print("\n--- Batch Prediction ---")
        test_batch_prediction()
    except requests.exceptions.ConnectionError:
        print("\nWARNING: API not running. Start it with: uvicorn app:app --reload")
