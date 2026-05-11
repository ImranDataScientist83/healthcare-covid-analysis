# 🏥 COVID-19 Healthcare Utilization Analysis

**Academic Research Project | Master of Computer Science | Universita Degli Studi Guglielmo Marconi**

[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E?logo=scikit-learn)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

---

## 📊 Project Overview

This project conducts **comprehensive analysis of COVID-19 healthcare utilization patterns** using publicly available datasets. The analysis identifies temporal infection patterns, outcome correlations, and develops predictive models for case severity exploration.

### 🎯 Key Objectives

| Objective | Method |
|-----------|--------|
| **Temporal Pattern Analysis** | Time series decomposition and trend modeling |
| **Feature Engineering** | Structured extraction from noisy public datasets |
| **Severity Prediction** | Supervised learning for case outcome classification |
| **Data Validation** | Cleaning pipelines for real-world healthcare data |

---

## 📁 Notebook Structure

```text
PROJECT 1-7 COVID19.ipynb (3500+ lines)
│
├── 1. Data Acquisition & Loading
│ └── Public healthcare dataset ingestion
│
├── 2. Data Cleaning & Validation
│ ├── Missing value handling
│ ├── Outlier detection
│ └── Data type normalization
│
├── 3. Exploratory Data Analysis (EDA)
│ ├── Temporal infection trends
│ ├── Demographic distributions
│ ├── Correlation heatmaps
│ └── Visualization dashboards
│
├── 4. Feature Engineering
│ ├── Lag features for time series
│ ├── Rolling statistics
│ └── Interaction terms
│
├── 5. Statistical Modeling
│ ├── Regression analysis
│ ├── Time series decomposition
│ └── Trend identification
│
├── 6. Machine Learning for Severity Prediction
│ ├── Classification models (Logistic Regression, Random Forest, XGBoost)
│ ├── Cross-validation strategy
│ ├── Hyperparameter tuning
│ └── Model evaluation (Accuracy, Precision, Recall, F1, AUC-ROC)
│
└── 7. Insights & Conclusions
├── Key findings documentation
├── Business impact recommendations
└── Limitations & future work

```


---

## 📈 Key Visualizations Included

The notebook contains **fully rendered outputs** including:

| Visualization | Purpose |
|---------------|---------|
| **Time Series Plots** | Infection rate trends over time |
| **Heatmaps** | Correlation between features |
| **Distribution Plots** | Age, demographic, outcome distributions |
| **ROC Curves** | Model performance comparison |
| **Feature Importance** | Top predictors of severity |
| **Confusion Matrices** | Classification error analysis |

---

## 🔬 Methodology

### Data Sources
- Publicly available COVID-19 healthcare datasets
- Real-world case reports with temporal markers

### Technical Approach


## 🔬 Models Implemented

| Model | Use Case | Key Metric |
|-------|----------|------------|
| Linear Regression | Trend forecasting | R², RMSE |
| Logistic Regression | Severity classification | Accuracy, AUC |
| Random Forest | Feature importance | Gini importance |
| Gradient Boosting | High-performance prediction | F1-score |

## 📊 Key Findings

| Finding | Implication |
|---------|-------------|
| Temporal Patterns | Identified peak infection periods and lag effects |
| Risk Factors | Age and comorbidity as top severity predictors |
| Healthcare Utilization | Correlation between case volume and resource demand |
| Model Performance | Achieved 85%+ accuracy on severity prediction |

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Data Processing | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn, XGBoost |
| Statistics | Statsmodels, SciPy |
| Environment | Jupyter Notebook 7.0.8 |

## 🚀 How to Run

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels xgboost plotly

git clone https://github.com/ImranDataScientist83/healthcare-covid-analysis.git
cd healthcare-covid-analysis/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS

jupyter notebook "PROJECT 1-7 COVID19.ipynb"
```

---

## 🔬 Methodology

### Data Sources
- Publicly available COVID-19 healthcare datasets
- Real-world case reports with temporal markers

### Technical Approach

```python
# Pipeline Overview

Data Ingestion
   ↓
Cleaning
   ↓
EDA
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Cross-Validation
   ↓
Evaluation
   ↓
Insights
```

---

## 📚 Academic Context

This project was completed as part of:

**Master of Computer Science**  
Universita Degli Studi Guglielmo Marconi

### Core Focus
- Machine Learning
- Statistical Modeling
- End-to-end ML lifecycle on real-world healthcare data

---

## 🔍 Preview of Notebook Outputs

The notebook includes fully executed outputs with:

- 📊 6+ EDA visualizations (time series, distributions, heatmaps)
- 📈 Model training logs with hyperparameters
- 📉 Evaluation metrics (confusion matrices, ROC curves)
- 💡 Business insights derived from analysis

> Screenshots of key visualizations can be added to the `/images` folder.

---

## ✅ Skills Demonstrated

| Skill Area | Specific Competencies |
|------------|----------------------|
| Data Engineering | Cleaning noisy public datasets, validation pipelines |
| Statistical Analysis | Time series decomposition, trend modeling |
| Feature Engineering | Lag features, rolling statistics, interaction terms |
| Model Validation | Cross-validation, bias-variance tradeoff |
| Reproducibility | Documented methodology, full notebook outputs |

---

## 📝 Author

**MAS IMRAN**  
Applied Machine Learning Engineer  
Master of Computer Science (Expected Feb 2026)

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?logo=github)](https://github.com/ImranDataScientist83)

[![Email](https://img.shields.io/badge/Email-imranscar@hotmail.com-red?logo=gmail)](mailto:imranscar@hotmail.com)

---

## 📚 References

- Public COVID-19 healthcare datasets
- Scikit-learn documentation
- Time series analysis methodologies

---

## 📌 Live Notebook

[View on GitHub](https://github.com/ImranDataScientist83/healthcare-covid-analysis)

---

## 📸 Sample Visualizations

### Hospital Beds vs Fatality Rate
![Hospital Beds Heatmap](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/hospital_beds_fatality_heatmap.png.png)

### Global Vaccination Trend
![Vaccination Trend](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/global_vaccination_trend.png.png)

### Global Fatality Rate Trend
![Fatality Rate](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/global_fatality_rate_trend.png.png)

### Positivity Rate vs Testing Volume
![Positivity vs Testing](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/positivity_vs_testing_scatter.png.png)

### Distribution of Cases Across Continents
![Continental Distribution](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/continent_cases_boxplot.png.png)

### Smoking vs Fatality Relationship
![Smoking Fatality](https://github.com/ImranDataScientist83/healthcare-covid-analysis/blob/main/04-UNIVERSITY-COVID19-HEALTHCARE-ANALYSIS/SCREENSHOTS/smoking_vs_fatality_analysis.png.png)
