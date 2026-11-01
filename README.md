# 🏥 Transparent AI Framework for Healthcare Claim Denial Explanations
### Masters Capstone Project — Explainable AI (XAI)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![SHAP](https://img.shields.io/badge/XAI-SHAP-orange)](https://shap.readthedocs.io)
[![LIME](https://img.shields.io/badge/XAI-LIME-green)](https://github.com/marcotcr/lime)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

---

## 📌 Project Overview

This capstone project develops a **Transparent AI Framework** to predict and explain healthcare insurance claim denial outcomes using the California Department of Managed Health Care (DMHC) **Independent Medical Review (IMR)** dataset.

The project applies state-of-the-art **Explainable AI (XAI)** techniques — specifically **SHAP** and **LIME** — to make black-box machine learning models interpretable in a high-stakes healthcare context.


## 📂 Project Structure

```
capstone-xai-healthcare/
│
├── data/
│   ├── raw/                    ← Original IMR dataset (not tracked by git)
│   └── processed/              ← Cleaned & encoded dataset
│
├── notebooks/
│   ├── 01_EDA.ipynb            ← Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb  ← Data Cleaning & Feature Engineering
│   ├── 03_Modeling.ipynb       ← Model Training & Evaluation
│   └── 04_XAI_Explanations.ipynb ← SHAP & LIME Explanations
│
├── models/                     ← Saved trained models (.pkl)
├── outputs/
│   ├── figures/                ← All plots and visualizations
│   └── reports/                ← Interim and final report drafts
│
├── requirements.txt            ← Python dependencies
├── .gitignore                  ← Files excluded from git
└── README.md                   ← This file
```

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| **Name** | IMR Determinations Trends |
| **Source** | California Department of Managed Health Care (DMHC) |
| **Records** | 42,749 |
| **Features** | 14 |
| **Target Variable** | `Determination` (Overturned / Upheld) |
| **Class Balance** | 52.5% Overturned / 47.5% Upheld |
| **Time Span** | 2001 – 2026 |
| **File Size** | ~85 MB |

> ⚠️ **The raw dataset is NOT stored in this repository** (too large for GitHub). Use one of the download options below.

### 📥 How to Get the Dataset

**Option 1 — Official Source (Free)**
Download directly from the California DMHC Open Data Portal:
🔗 [DMHC IMR Determinations Dataset](https://www.dmhc.ca.gov/data-and-statistics.aspx)
- File: `independent-medical-review-imr-determinations-trends.csv`

**Option 2 — Google Drive (Shared by Author)**
🔗 [Download from Google Drive](https://drive.google.com/drive/folders/15fLR5dd4anqQThCnm20Vw2C1Pe7tYKXE?usp=drive_link)

### 📁 After Downloading
Place the CSV file here:
```
data/raw/independent-medical-review-imr-determinations-trends.csv
```

---

## 🧠 Models Used

| Model | Type |
|-------|------|
| Logistic Regression | Baseline (Interpretable) |
| Random Forest | Ensemble (Tree-based) |
| XGBoost | Gradient Boosting |
| LightGBM | Gradient Boosting (Fast) |

---

## 🔍 XAI Techniques

| Technique | Scope | Library |
|-----------|-------|---------|
| SHAP Summary Plot | Global | `shap` |
| SHAP Dependence Plot | Global | `shap` |
| SHAP Force Plot | Local | `shap` |
| SHAP Waterfall Plot | Local | `shap` |
| LIME Explanation | Local | `lime` |


