
# Dockerfile for Churn Prediction API
FROM python:3.10-slim

WORKDIR /app

COPY requirements_prod.txt .
RUN pip install --no-cache-dir -r requirements_prod.txt

COPY app.py .
COPY final_tuned_model.pkl .
COPY final_scaler.pkl .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
