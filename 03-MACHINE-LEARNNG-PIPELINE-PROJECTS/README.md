# 📓 ML Pipeline Development Notebooks

**[← Back to Main Portfolio](../README.md)**

This folder contains Jupyter notebooks documenting the complete development process for the Customer Churn Prediction project.

## 📊 Notebook Outputs Included

This notebook contains **full outputs** including:
- EDA visualizations and graphs (churn distribution, tenure analysis, correlation heatmaps)
- Model training results and logs
- Classification metrics (precision, recall, F1-score)
- Feature importance analysis with bar charts
- Model comparison tables

**Why outputs are included:** To demonstrate data exploration, model evaluation, and business insights derived from the analysis.

## 📁 Notebook

### customer_churn_pipeline.ipynb

Complete ML pipeline for customer churn prediction including:

| Step | Description |
|------|-------------|
| **Data Generation** | Synthetic customer data (10,000 records) with realistic churn patterns based on business rules |
| **Exploratory Data Analysis** | 6 visualizations showing churn distribution, tenure analysis, monthly charges, contract impact, complaints, and correlation heatmap |
| **Feature Engineering** | Created new features: avg_monthly_spend, charge_per_minute, high_risk |
| **Model Training** | Logistic Regression, Random Forest, Gradient Boosting |
| **Model Evaluation** | Accuracy, AUC-ROC, Classification Reports, 5-fold Cross-validation |
| **Feature Importance** | Identified top drivers of customer churn with visualization |
| **Model Export** | Saved models as .pkl files for API deployment |

## 🏆 Key Results

| Model | Accuracy | AUC-ROC |
|-------|----------|---------|
| Logistic Regression | 84.5% | 0.933 |
| Random Forest | **97.9%** | **0.987** |
| Gradient Boosting | 97.9% | 0.985 |

**Best Model:** Random Forest Classifier

## 🔑 Top 5 Churn Drivers

From feature importance analysis:

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Tech Support | 40.7% |
| 2 | Payment Method | 20.6% |
| 3 | Monthly Charges | 7.9% |
| 4 | High Risk Flag | 6.4% |
| 5 | Tenure Months | 4.3% |

## 💡 Business Insights

- Customers without tech support are significantly more likely to churn (40.7% importance)
- Electronic check payments correlate with higher churn rates
- Month-to-month contracts have higher churn risk than annual contracts
- Customers with multiple complaints (>2) are high-risk
- Shorter tenure customers are more likely to leave

## 🚀 How to Run the Notebook

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

## 📝 Author

**MAS IMRAN**  
🎓 Applied Machine Learning Engineer | Master of Computer Science (Feb 2026)

[![Email](https://img.shields.io/badge/Email-imranscar%40hotmail.com-blue?logo=gmail&logoColor=white)](mailto:imranscar@hotmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?logo=github&logoColor=white)](https://github.com/ImranDataScientist83)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mas-imran-38360613a/)
[![Portfolio](https://img.shields.io/badge/Portfolio-AI%2FML%20Projects-FF5722?logo=google-chrome&logoColor=white)](https://github.com/ImranDataScientist83/healthcare-covid-analysis)

✨ Part of **AI / ML / Algorithm Engineering Portfolio**
