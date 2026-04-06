from fastapi import FastAPI
from transformers import pipeline

app = FastAPI(title="LLM Moderation API")

# Load model once (important)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "safe",
    "spam",
    "fraud",
    "hate speech",
    "violence",
    "policy violation"
]

def classify_text(text):
    result = classifier(text, candidate_labels=labels)
    
    return {
        "text": text,
        "prediction": result["labels"][0],
        "confidence": float(result["scores"][0])
    }

def moderation_decision(text):
    result = classify_text(text)
    
    if result["prediction"] in ["fraud", "hate speech", "violence"]:
        action = "REJECT"
    elif result["prediction"] == "spam":
        action = "REVIEW"
    else:
        action = "ALLOW"
    
    result["action"] = action
    return result

@app.get("/")
def home():
    return {"message": "LLM Moderation API Running"}

@app.get("/moderate")
def moderate(text: str):
    return moderation_decision(text)
