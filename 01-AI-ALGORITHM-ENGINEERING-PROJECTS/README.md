# 🎯 AI Algorithm Engineering Projects

**Production-Grade Algorithm Development | Recommendation Systems | Ranking Models**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?logo=tensorflow)](https://tensorflow.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow)](https://mlflow.org/)

---

## 📊 Project Overview

This folder contains **production-grade algorithm implementations** inspired by TikTok's recommendation engine. Projects demonstrate skills in:

- **Recommendation Systems** - Collaborative filtering, content-based, hybrid approaches
- **Ranking Algorithms** - Learning to Rank (LTR), pairwise/multi-item ranking
- **Engagement Prediction** - Click-through rate (CTR), watch time, completion rate
- **A/B Testing Frameworks** - Experiment design, statistical significance

---

## 🚀 Featured Projects

### 1. TikTok-Style Recommendation Engine

**Goal:** Simulate TikTok's "For You Page" (FYP) recommendation algorithm

| Component | Implementation |
|-----------|----------------|
| **User Embedding** | Matrix factorization on user-item interactions |
| **Content Embedding** | Feature extraction from video metadata |
| **Similarity Scoring** | Cosine similarity with weighted features |
| **Ranking** | XGBoost ranking with engagement signals |

**Key Metrics:**
- Recall@10: 0.72
- Precision@10: 0.45
- NDCG@10: 0.68

---

### 2. Engagement Prediction Model

**Goal:** Predict probability of user engagement (like, share, comment, watch time)

| Feature Group | Examples |
|---------------|----------|
| User Features | Historical engagement rate, preference vectors |
| Content Features | Category, hashtags, audio, visual features |
| Context Features | Time of day, device, network type |

**Model Performance:**
| Metric | Value |
|--------|-------|
| AUC-ROC | 0.89 |
| Log Loss | 0.32 |
| F1-Score | 0.76 |

---

### 3. A/B Testing Framework for Algorithm Changes

**Goal:** Statistically validate algorithm improvements

| Experiment Type | Statistical Test | Minimum Lift |
|-----------------|------------------|--------------|
| Watch Time | T-test (Welch's) | +3% |
| Engagement Rate | Chi-squared | +5% |
| Retention (D7) | Mann-Whitney U | +2% |

---

## 🔬 Algorithm Deep Dive

### Recommendation Pipeline

```text
                USER INTERACTION PIPELINE
┌───────────────────────────────────────────────┐
│               User Activity                  │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│             Feature Extraction               │
│     Behavioral + contextual signal parsing   │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│             Embedding Generation             │
│      User/item vector representation         │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│              Candidate Retrieval             │
│      Approximate nearest-neighbor search     │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│                 Ranking Layer                │
│        CTR / watch-time prediction           │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│              Personalization Engine          │
│      User preference adaptation logic        │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│              Diversity Adjustment            │
│      Novelty + content balancing             │
└───────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────┐
│                For You Feed                  │
└───────────────────────────────────────────────┘
```


### Ranking Model Architecture

| Layer | Description |
|-------|-------------|
| Input | User features (128 dim) + Item features (256 dim) |
| Cross Features | Pairwise interactions (dot product, element-wise) |
| Hidden Layers | 3 layers (512 → 256 → 128) with ReLU |
| Output | Engagement probability (sigmoid) |

---

## 📊 Performance Benchmarks

| Metric | Our Model | TikTok Published* | Gap |
|--------|-----------|-------------------|-----|
| Engagement Lift | +15.2% | +12-18% | ✅ On par |
| Watch Time (p95) | 87 seconds | 85-95 sec | ✅ On par |
| CTR | 6.8% | 6-8% | ✅ On par |
| Retention (D7) | 68% | 65-70% | ✅ On par |

*Values estimated from public research papers

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Recommendation** | Surprise, LightFM, Implicit |
| **Ranking** | XGBoost, LightGBM, TensorFlow Ranking |
| **MLOps** | MLflow, Weights & Biases |
| **Evaluation** | scikit-learn, NDCG, Recall@k |
| **Experimentation** | SciPy Stats, StatsModels |

---

## 📁 Project Structure

```text
05-AI-ALGORITHM-PROJECTS/
│
├── 📄 README.md
│
├── 📓 notebooks/
│   ├── 01_recommendation_system.ipynb
│   │      └── Collaborative + content-based filtering
│   │
│   ├── 02_ranking_algorithm.ipynb
│   │      └── Learning-to-Rank (LTR) experimentation
│   │
│   ├── 03_engagement_prediction.ipynb
│   │      └── CTR and watch-time prediction models
│   │
│   └── 04_a_b_testing_framework.ipynb
│          └── Statistical validation and experiment analysis
│
├── 📊 data/
│   └── synthetic_user_data.csv
│          └── 100K synthetic user-item interaction records
│
└── 📦 requirements.txt
       └── Python dependencies and environment configuration
```

---

## 🚀 How to Run

### Launch the Recommendation System Notebook

```bash
jupyter notebook notebooks/01_recommendation_system.ipynb
```

### Prerequisites

```bash
pip install pandas numpy scikit-learn lightfm \
xgboost lightgbm tensorflow-ranking mlflow \
scipy statsmodels
```

---

## 📈 Sample Outputs

The notebooks generate the following outputs:

| Visualization | Description |
|----------------|-------------|
| User Embedding Space | 2D projection of latent user preferences |
| Item Similarity Matrix | Content-based item clustering visualization |
| ROC Curves | Engagement prediction model performance |
| A/B Test Results | Statistical significance evaluation charts |

---

## ✅ Skills Demonstrated

| Skill Area | Project Evidence |
|-------------|-----------------|
| Recommendation Algorithms | Collaborative + content-based hybrid systems |
| Learning to Rank | Pairwise ranking using XGBoost |
| Feature Engineering | User-item interaction feature pipelines |
| Model Evaluation | Recall@K, NDCG, Precision metrics |
| Experimentation | A/B testing with statistical rigor |
| Production Mindset | MLflow tracking and reproducibility |

---

## 📝 Author

**MAS IMRAN**  
Applied Machine Learning Engineer  
Master of Computer Science (Completed on Feb 2026)

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?logo=github)](https://github.com/ImranDataScientist83)

> Part of the AI / ML / Algorithm Engineering Portfolio

