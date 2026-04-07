# 🏥 ML-Powered COVID Risk Assessment API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.3-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Project Overview

A production-ready REST API that assesses COVID-19 risk based on clinical symptoms using a rule-based clinical scoring algorithm. This project demonstrates **end-to-end ML system deployment** skills that top tech companies (ByteDance, TikTok, Shopee) look for.

### 🔥 Key Features

- ✅ **Real-time risk assessment** - Instant predictions via REST API
- ✅ **Batch processing** - Analyze multiple patients at once
- ✅ **Interactive documentation** - Auto-generated Swagger UI
- ✅ **Clinical-grade logic** - Age-weighted, symptom-based scoring
- ✅ **Production ready** - FastAPI with automatic validation

## 🏗️ Architecture
┌─────────────────┐
│ Client/Frontend│
└────────┬────────┘
│ HTTP Request
▼
┌─────────────────┐
│ FastAPI App │ ← /predict, /predict/batch
│ (app.py) │
└────────┬────────┘
│
▼
┌─────────────────┐
│ Risk Calculation│
│ Engine │
│ • Age weighting │
│ • Symptom scoring│
│ • Duration factor│
└────────┬────────┘
│
▼
┌─────────────────┐
│ Decision Logic │
│ High/Medium/Low │
└────────┬────────┘
│
▼
┌─────────────────┐
│ JSON Response │
└─────────────────┘
