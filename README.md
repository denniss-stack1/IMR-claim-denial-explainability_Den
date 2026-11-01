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

---

## 🎯 Research Questions

1. Can ML models accurately predict whether a health insurance claim denial will be **overturned or upheld**?
2. Which features (diagnosis, treatment type, demographics) are most influential in the model's prediction? *(Global XAI)*
3. How can individual predictions be explained for specific patient cases? *(Local XAI)*
4. Do patient demographics (age, gender) introduce bias in claim outcomes? *(Fairness Analysis)*

---

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
| **Source** | California DMHC — Independent Medical Review Determinations |
| **Records** | 42,749 |
| **Features** | 14 |
| **Target** | `Determination` (Overturned / Upheld) |
| **Class Balance** | 52.5% Overturned / 47.5% Upheld |
| **Time Span** | 2001 – 2026 |

> ⚠️ The raw dataset file is excluded from this repository due to size (~85 MB). Download it from the [DMHC Open Data Portal](https://www.dmhc.ca.gov/data-and-statistics.aspx).

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

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/denniss-stack1/capstone-xai-healthcare.git
cd capstone-xai-healthcare
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your dataset
Place the raw CSV file in `data/raw/` folder.

### 5. Run notebooks in order
```
notebooks/01_EDA.ipynb → 02_Preprocessing.ipynb → 03_Modeling.ipynb → 04_XAI_Explanations.ipynb
```

---

## 📈 Results Summary

> *This section will be updated as the project progresses.*

| Model | Accuracy | F1-Score | ROC-AUC |
|-------|----------|----------|---------|
| Logistic Regression | TBD | TBD | TBD |
| Random Forest | TBD | TBD | TBD |
| XGBoost | TBD | TBD | TBD |
| LightGBM | TBD | TBD | TBD |

---

## 👤 Author

**Dennis Sebastian**  
Masters Student — Data Science / AI  
📧 dennis.sebastiangeorge1@gmail.com  
🐙 [@denniss-stack1](https://github.com/denniss-stack1)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
