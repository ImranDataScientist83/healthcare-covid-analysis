# 🤖 ByteDance-Style Multilingual RAG Support System

Production-oriented Retrieval-Augmented Generation (RAG) pipeline for multilingual customer support systems inspired by large-scale social media platforms such as TikTok, CapCut, and Lark.

---

## 🎯 Project Overview

This project simulates a **production-aware AI support system** with:

| Feature | Details |
|---------|---------|
| 🌐 **Multilingual retrieval** | English, Indonesian, Malay, Chinese, Thai |
| 📝 **Structured LLM responses** | JSON outputs with confidence scoring |
| 📊 **MLflow experiment tracking** | Full reproducibility across configurations |
| ⚡ **Production simulation** | Latency benchmarks and error handling |

---

## 📁 Project Structure

```text
byte-dance-rag-support/
│
├── 📓 notebooks/
│ ├── 01_data_prep.ipynb # Create synthetic ByteDance tickets
│ ├── 02_embedding_retrieval.ipynb # Build embedding-based retrieval
│ ├── 03_llm_response_gen.ipynb # Generate structured LLM responses
│ ├── 04_evaluation_mlflow.ipynb # Track experiments with MLflow
│ └── 05_visualizations.ipynb # Generate portfolio dashboards
│
├── 🖼️ images/ # 8 visualization outputs (.png)
├── 📄 reports/ # HTML portfolio report
├── 💾 data/ # JSON knowledge base & tickets
└── 📦 requirements.txt # Python dependencies

```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Retrieval | Cosine similarity with top-k |
| LLM | Google Gemini / Mock mode |
| Tracking | MLflow 3.7+ |
| Analytics | Pandas, NumPy, scikit-learn |
| Visualization | Matplotlib, Seaborn, Plotly |

---

## 🧠 Core AI Engineering Concepts Demonstrated

- Embedding-based semantic retrieval
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- Structured LLM response pipelines
- Prompt engineering workflows
- Confidence-based escalation logic
- MLflow experiment tracking
- Multilingual NLP processing
- Production-aware latency monitoring

---

## 📊 Key Results

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Best k value | 3 | - | ✅ |
| Avg LLM Confidence | 78.5% | >70% | ✅ |
| Escalation Rate | 21.5% | <30% | ✅ |
| Recall@3 | 65.2% | >60% | ✅ |

---

## 📏 Evaluation Methodology

| Component | Evaluation Metric |
|-----------|------------------|
| Retrieval | Recall@K, cosine similarity |
| LLM Output | Confidence scoring, escalation rate |
| Pipeline | Average latency and throughput |
| System Quality | Manual validation + rule-based checks |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/ImranDataScientist83/healthcare-covid-analysis.git
cd healthcare-covid-analysis/byte-dance-rag-support
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the first notebook
```
jupyter notebook notebooks/01_data_prep.ipynb
```

### 4. Launch MLflow UI
```
mlflow ui --port 5000
```

## 🤖 AI Engineering Projects - Visualizations

### Ticket Demographics
![Ticket Demographics](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/01_ticket_demographics.png)

### Knowledge Base Analysis
![Knowledge Base Analysis](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/02_knowledge_base_analysis.png)

### Retrieval Performance
![Retrieval Performance](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/03_retrieval_performance.png)

### LLM Quality Analysis
![LLM Quality Analysis](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/04_llm_quality_analysis.png)

### Performance Radar
![Performance Radar](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/06_performance_radar.png)

### Time Series Analysis
![Time Series Analysis](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/07_time_series_analysis.png)

### Comprehensive Summary
![Comprehensive Summary](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/01-AI-ENGINEERING-PROJECTS/byte-dance-rag-support/images/08_comprehensive_summary.png)
