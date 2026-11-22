# 🏥 Transparent AI Framework for Healthcare Claim Denial Explanations
### Masters Capstone Project — Explainable AI (XAI)
**University of Europe for Applied Sciences — Master of Data Science**  
**Students:** Dennis Sebastian (59593398) & Saran Jayakumaran Nair Sasikala (56500625)  
**Supervisor:** Dr. Humera Noor  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![SHAP](https://img.shields.io/badge/XAI-SHAP-orange)](https://shap.readthedocs.io)
[![LIME](https://img.shields.io/badge/XAI-LIME-green)](https://github.com/marcotcr/lime)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![Sprint 2 Status](https://img.shields.io/badge/Sprint%202-Delivered%20%E2%9C%85-brightgreen)]()

---

## 📌 Project Overview

This capstone project develops a **Transparent AI Framework** to predict and explain healthcare insurance claim denial outcomes using the California Department of Managed Health Care (DMHC) **Independent Medical Review (IMR)** dataset.

By applying state-of-the-art **Explainable AI (XAI)** techniques — specifically **SHAP (SHapley Additive exPlanations)** and **LIME** — the framework makes complex ensemble models transparent and interpretable for clinicians, patients, and healthcare payers (**Cigna, Aetna, CVS Health, Optum, and Elevance Health**).

---

## 📅 Sprint Progress & Milestone Roadmap

| Sprint | Milestone / Focus | Period | Status | Key Deliverable |
|:---|:---|:---:|:---:|:---|
| **Sprint 1** | Foundations & Exploratory Data Analysis (EDA) | 26 Oct – 08 Nov 2026 | ✅ **Completed** | [Progress Report 1 (PDF)](capstone%20AI/Progress_Report_1_IMR_Healthcare_XAI.pdf) |
| **Sprint 2** | Data Preprocessing, Leakage Mitigation & Baseline ML | 09 Nov – 22 Nov 2026 | ✅ **Completed** | [Progress Report 2 (PDF)](capstone%20AI/Progress_Report_2_IMR_Healthcare_XAI.pdf) & [Word Doc](capstone%20AI/Progress_Report_2_IMR_Healthcare_XAI.docx) |
| **Sprint 3** | Machine Learning Optimization & Tuning | 24 Nov – 07 Dec 2026 | 🔵 **Active** | Hyperparameter Tuning & Champion Model Selection |
| **Sprint 4** | Global Explainability (SHAP TreeExplainer) | 08 Dec – 21 Dec 2026 | ⬜ Upcoming | Global Feature Attribution & Bias Audits |
| **Sprint 5** | Local Explainability (SHAP & LIME Case Studies) | 22 Dec – 04 Jan 2027 | ⬜ Upcoming | Patient Case Explanations |
| **Sprint 6** | Final Documentation, Presentation & Pitch | 05 Jan – 18 Jan 2027 | ⬜ Upcoming | Slide Deck, Video Pitch & Final Thesis Report |

---

## 🚀 Sprint 2 Baseline Model Benchmark Results

Evaluated on a strictly isolated, stratified held-out test partition (**8,267 records**, preserving the natural 52.94% Overturned vs. 47.06% Upheld class distribution):

| Model Architecture | Model Family | Accuracy | Precision (Overturned) | Recall | F1-Score | ROC-AUC |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **Random Forest** (100 Trees, Depth 12) | Ensemble Bagging | 67.22% | **72.52%** | 61.32% | 0.665 | **0.747** |
| **Hist Gradient Boosting** (LightGBM equivalent) | Gradient Boosting | **68.07%** | 71.97% | **65.00%** | **0.683** | 0.745 |
| **Logistic Regression** (Standardized Linear) | Linear Baseline | 58.86% | 59.88% | 67.56% | 0.635 | 0.632 |

### 🔬 Key Clinical & Engineering Takeaways
1. **High Precision on Overturned Cases (72.52%):** Tree ensembles accurately detect disputed claims with genuine reversal merit, providing immediate operational value to health plans to correct improper claim denials proactively.
2. **Retrospective Target Leakage Mitigation:** The independent reviewer narrative (`Findings`) was found to contain explicit post-hoc verdict statements (e.g., *"Therefore, the Health Plan denial should be upheld"*). This was strictly sequestered to prevent artificial 100% memorization in tabular models.
3. **Data Hygiene & Non-Overlapping Null Cohorts:** Audited that missing demographic entries (685 rows) and review duration entries (691 rows) occupied non-overlapping cohorts. Complete case sanitization purged 39 duplicates and 1,378 incomplete cases, retaining **41,332 high-fidelity records (96.69% retention rate)** with zero imputation distortion.

---

## 📊 Visual Diagnostic Analytics

<p align="center">
  <img src="capstone%20AI/fig3_roc_comparison.png" width="48%" alt="ROC-AUC Curves" />
  <img src="capstone%20AI/fig5_feature_importance.png" width="48%" alt="Feature Importance" />
</p>

<p align="center">
  <img src="capstone%20AI/fig4_confusion_matrices.png" width="95%" alt="Confusion Matrix Grid" />
</p>

---

## 📂 Repository Structure

```
IMR-claim-denial-explainability_Den/
│
├── capstone AI/
│   ├── Progress_Report_2_IMR_Healthcare_XAI.pdf   ← Official Sprint 2 Report (PDF)
│   ├── Progress_Report_2_IMR_Healthcare_XAI.docx  ← Editable Word source
│   ├── Progress_Report_1_IMR_Healthcare_XAI.pdf   ← Official Sprint 1 Report
│   ├── _XAI_Healthcare_Capestone Project.ipynb   ← Primary executed notebook (Sprint 1 + 2)
│   ├── 02_Preprocessing_and_Baseline_Modeling.ipynb ← Clean Sprint 2 notebook
│   ├── LinkedIn_Post_Drafts_Sprint_2.md           ← Individual LinkedIn post drafts
│   ├── index.html                                 ← Interactive progress dashboard
│   ├── XAI_capestone.html                         ← Academic portfolio showcase
│   ├── fig1_data_cleaning_audit.png               ← Ingestion & cleansing funnel
│   ├── fig2_target_stratification.png             ← Stratified class balance check
│   ├── fig3_roc_comparison.png                    ← Baseline ROC curves
│   ├── fig4_confusion_matrices.png                ← Diagnostic confusion matrices
│   ├── fig5_feature_importance.png                ← Random Forest Gini importances
│   └── sprint2_metrics.json                       ← Evaluated metrics summary
│
├── README.md                                      ← Repository overview & milestones
├── ROADMAP.md                                     ← Comprehensive sprint plan & deliverables
├── requirements.txt                               ← Python dependencies
└── .gitignore                                     ← Ignored datasets (*.csv) & models (*.pkl)
```

---

## 📊 Dataset Information

| Property | Value |
|:---|:---|
| **Name** | IMR Determinations Trends |
| **Source** | California Department of Managed Health Care (DMHC) |
| **Raw Records** | 42,749 |
| **Cleaned Complete Cases** | 41,332 (96.69% retention) |
| **Features** | 11 Engineered Features (Ordinal Age 0–6, Categorical Label Encodings) |
| **Target Variable** | `Determination` (Binarized: 1 = Overturned [52.94%], 0 = Upheld [47.06%]) |
| **Time Span** | 2001 – 2026 |

> ⚠️ **The raw and processed datasets are excluded from Git** (`*.csv` ignored) due to size limitations.  
> 🔗 Official Source: [California DMHC Open Data Portal](https://www.dmhc.ca.gov/data-and-statistics.aspx)  
> 🔗 Google Drive Archive: [Download Dataset](https://drive.google.com/file/d/11apMqXGhHm5qkCJo5GM7O2gXmcyNGZrH/view?usp=sharing)

---


