
# production_pipeline.py - Automated ML Pipeline
import pandas as pd
import numpy as np
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

def create_pipeline():
    """Create the production ML pipeline"""
    
    # Define numeric and categorical features
    numeric_features = ['age', 'annual_income', 'purchase_frequency', 
                        'avg_order_value', 'tenure_months', 'num_support_tickets',
                        'total_spend', 'days_since_last_purchase']
    
    categorical_features = ['device_type', 'region', 'membership_tier']
    
    # Numeric pipeline
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Categorical pipeline
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Combine preprocessors
    preprocessor = ColumnTransformer([
        ('numeric', numeric_transformer, numeric_features),
        ('categorical', categorical_transformer, categorical_features)
    ])
    
    # Full pipeline
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    return pipeline

def train_pipeline(data_path, model_path='pipeline_model.pkl'):
    """Train and save the pipeline"""
    df = pd.read_csv(data_path)
    X = df.drop(['customer_id', 'churned'], axis=1)
    y = df['churned']
    
    pipeline = create_pipeline()
    pipeline.fit(X, y)
    
    joblib.dump(pipeline, model_path)
    print(f"Pipeline saved to {model_path}")
    return pipeline

def predict_pipeline(model_path, input_data):
    """Make predictions using saved pipeline"""
    pipeline = joblib.load(model_path)
    predictions = pipeline.predict(input_data)
    probabilities = pipeline.predict_proba(input_data)[:, 1]
    return predictions, probabilities

if __name__ == "__main__":
    print("ML Pipeline Automation Script")
    print("-" * 40)
    
    # Train pipeline
    pipeline = train_pipeline('engineered_dataset.csv')
    
    # Test prediction
    sample = pd.DataFrame([{
        'age': 45,
        'annual_income': 65000,
        'purchase_frequency': 3,
        'avg_order_value': 120,
        'tenure_months': 8,
        'customer_satisfaction': 2.5,
        'num_support_tickets': 4,
        'total_spend': 5000,
        'days_since_last_purchase': 45,
        'device_type': 'Mobile',
        'region': 'North',
        'membership_tier': 'Silver'
    }])
    
    pred, prob = predict_pipeline('pipeline_model.pkl', sample)
    print(f"Sample Prediction: {pred[0]} (Probability: {prob[0]:.2%})")
