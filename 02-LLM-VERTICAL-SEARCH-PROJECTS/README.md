# 🔍 LLM Vertical Search Engine 

**Production-Grade Multi-Modal Search | RAG Pipeline | Real-Time Inference | A/B Testing Framework**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-0194E2)](https://faiss.ai/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow)](https://mlflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://docker.com/)

---

## 📊 Project Overview

This repository implements a **production-grade vertical search engine** for short-form content, demonstrating the complete ML lifecycle from data acquisition to deployment. The system features multi-modal understanding, semantic search, RAG pipeline, and comprehensive A/B testing.

## 🎯 Key Capabilities

| Capability               | Implementation                                | Notebook |
|--------------------------|-----------------------------------------------|----------|
| 🧩 **Multi-Modal Understanding** | CLIP-style embeddings (text + title + genre) | 📓 1, 2 |
| 🔗 **Cross-Modal Alignment**     | Semantic similarity + Top-K accuracy         | 📓 3    |
| 📊 **Relevance Ranking**         | Gradient Boosting, Random Forest, Ridge      | 📓 4    |
| 🤖 **LLM Query Understanding**   | Intent classification + Query expansion      | 📓 5    |
| 🧠 **RAG Pipeline**              | Retrieval + Generation with FAISS            | 📓 6    |
| ⚔️ **Hard Negative Mining**      | Triplet loss training data                   | 📓 7    |
| ⚡ **Inference Optimization**    | FAISS indexing + Caching + Batching          | 📓 8    |
| 📐 **A/B Testing**               | Statistical validation + Power analysis      | 📓 9    |
| 🎨 **Visualization**             | 7 comprehensive dashboards                   | 📓 10   |

---

## 🏆 Performance Metrics

| Metric                  | Value                  |
|--------------------------|------------------------|
| 🌟 **Best NDCG@10**      | 0.68                   |
| ⚡ **Search Latency**    | 1.8ms (FAISS PQ optimized)        |
| 📈 **A/B Test Uplift**   | +10.5% (statistically significant)|
| 📚 **Documents Indexed** | 10,000+                |
| 🔍 **Queries Analyzed**  | 50,000+                |
| ✅ **Relevance Judgments** | 100,000+             |

---

## 📈 Visualization Gallery

> *Click any image to view full resolution*

### 🏆 Executive Dashboard – System Performance at a Glance

[![Master Performance Dashboard](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/master_performance_dashboard.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/master_performance_dashboard.png)

*9-in-1 dashboard covering genre distribution, search intent, relevance scores, similarity distribution, query length, top keywords, model NDCG, A/B uplift, and search latency.*

---

### 📊 A/B Testing & Statistical Validation – Production Readiness

[![A/B Testing Statistical Validation](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/ab_testing_statistical_validation.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/ab_testing_statistical_validation.png)

*Treatment effect distribution, power analysis (sample size vs detection power), 95% confidence intervals, and sequential experiment monitoring with p-value tracking.*

---

### 🧠 Ranking Model Deep Dive – Algorithm Excellence

[![Ranking Model Deep Dive](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/ranking_model_deep_dive.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/ranking_model_deep_dive.png)

*Radar chart comparing Gradient Boosting, Random Forest, and Ridge models; feature importance analysis; predicted vs actual relevance; and prediction error distribution.*

---

### 📌 Executive Summary Dashboard – Key Metrics

[![Executive Summary Dashboard](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/executive_summary%20dashboard%20.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/executive_summary%20dashboard%20(1).png)

*KPI dashboard with 10K+ documents, 50K+ queries, 100K+ judgments, 0.68 NDCG, 1.8ms latency, and +10.5% A/B uplift.*

---

### 🔬 Multi-Modal Embedding Space – Technical Foundation

[![Embedding Space Visualization](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/embedding_space_visualization.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/embedding_space_visualization.png)

*PCA and t-SNE projections of text vs title embeddings, showing multi-modal alignment quality and semantic clustering.*

---

### 🎯 Alignment Quality & Retrieval Performance

[![Alignment Quality Retrieval](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/alignment_quality_retrieval.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/alignment_quality_retrieval.png)

*Top-K alignment accuracy curve (1, 3, 5, 10, 20, 50) and text-title similarity heatmap demonstrating cross-modal retrieval quality.*

---

### 🤖 RAG Pipeline & LLM Understanding

[![RAG Pipeline LLM](https://raw.githubusercontent.com/ImranDataScientist83/healthcare-covid-analysis/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/rag_pipeline_llm.png)](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/02-LLM-VERTICAL-SEARCH-PROJECTS/Images/rag_pipeline_llm.png)

*RAG architecture diagram, query intent distribution, retrieval quality by query length, and LLM response confidence distribution.*

## 📁 Project Structure

```text
02-LLM-VERTICAL-SEARCH-ENGINE/
│
├── 📄 README.md
│
├── 📓 Notebooks/ (10 notebooks)
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 1 Multi-Modal Data Acquisition.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 2 Multi-Modal Embedding Generation CLIP ViT.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 3  Cross-Modal Semantic Alignment.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 4 Relevance Ranking Model.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 5 LLM Query Understanding.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 6 Retrieval-Augmented Generation RAG.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 7 Hard Negative Mining.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 8 Online Inference Optimization.ipynb
│   ├── LLM Machine Learning Engineer, Vertical Search Notebook 9 A B Testing Framework.ipynb
│   └── LLM Machine Learning Engineer, Vertical Search Notebook 10 Comprehensive Visualizations Dashboard.ipynb
│
├── 📊 Data/
│   ├── drama_content.csv (10,000 records)
│   ├── photo_content.csv (10,000 records)
│   ├── query_logs.csv (50,000 records)
│   └── relevance_judgments.csv (100,000 records)
│
├── 🤖 Models/
│   ├── best_ranking_model.pkl
│   └── faiss_index.bin
│
├── 🖼️ Images/
│   ├── master_performance_dashboard.png
│   ├── embedding_space_visualization.png
│   ├── ranking_model_deep_dive.png
│   ├── rag_pipeline_llm.png
│   ├── ab_testing_statistical_validation.png
│   └── executive_summary_dashboard.png
│
└── 📦 requirements.txt
```

### Clone repository
git clone https://github.com/ImranDataScientist83/healthcare-covid-analysis.git
cd healthcare-covid-analysis/02-LLM-VERTICAL-SEARCH-PROJECTS

### Install dependencies
pip install -r requirements.txt

## 📈 Visualization Gallery

| Dashboard                          | Description                                |
|------------------------------------|--------------------------------------------|
| 🖥️ master_performance_dashboard.png | 🔎 9-in-1 performance overview              |
| 🎨 embedding_space_visualization.png| 🧩 PCA + t-SNE of multi-modal embeddings    |
| 📊 ranking_model_deep_dive.png      | ⚖️ Model comparison + feature importance    |
| 🤖 rag_pipeline_llm.png             | 🧠 RAG architecture + LLM understanding     |
| 📈 ab_testing_statistical_validation.png | 📐 A/B test results + power analysis   |
| 🏆 executive_summary_dashboard.png  | 📌 KPI dashboard                            |

## 🛠️ Technology Stack

| Category        | Technologies                                |
|-----------------|---------------------------------------------|
| 🔤 Embeddings   | SentenceTransformers, CLIP-style            |
| 🔍 Search       | FAISS (FlatIP, IVF, PQ)                     |
| 📊 ML Models    | XGBoost, Gradient Boosting, Random Forest   |
| 🤖 LLM          | SentenceTransformer, RAG Pipeline           |
| ⚙️ MLOps        | MLflow, Experiment Tracking                 |
| 🎨 Visualization| Matplotlib, Seaborn, Plotly                 |
| 🚀 Deployment   | FastAPI, Docker                             |


## ✅ Skills Demonstrated

| Skill                  | Evidence                                      |
|-------------------------|-----------------------------------------------|
| 🧩 Multi-modal ML       | CLIP embeddings + cross-modal alignment       |
| 🔍 Search & Ranking     | FAISS + Learning-to-Rank                      |
| 🤖 LLM Integration      | Query understanding + RAG                     |
| ⚡ Production Optimization | Caching, batching, quantization           |
| 📐 A/B Testing          | Statistical validation + power analysis       |
| ⚙️ MLOps                | 10 notebooks, experiment tracking             |

---

## 📝 Author

**MAS IMRAN**  
🎓 Applied Machine Learning Engineer | Master of Computer Science (Feb 2026)

[![Email](https://img.shields.io/badge/Email-imranscar%40hotmail.com-blue?logo=gmail&logoColor=white)](mailto:imranscar@hotmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?logo=github&logoColor=white)](https://github.com/ImranDataScientist83)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mas-imran-38360613a/)
[![Portfolio](https://img.shields.io/badge/Portfolio-AI%2FML%20Projects-FF5722?logo=google-chrome&logoColor=white)](https://github.com/ImranDataScientist83/healthcare-covid-analysis)

✨ Part of **AI / ML / Algorithm Engineering Portfolio**

---

## 📚 Related Projects

- AI Engineering Projects
- AI Algorithm Engineering Projects
- AI/ML Engineering Projects
- ByteDance-Style RAG Support System
- Large Language Model Engineering
- ML Pipeline Projects
- COVID-19 Healthcare Analysis
