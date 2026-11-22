# 🚀 Sprint 2 LinkedIn Post Drafts
**Project:** Transparent AI Framework for Healthcare Claim Denial Explanations  
**Master of Data Science | University of Europe for Applied Sciences**  
**Reporting Period:** 09 Nov 2026 – 22 Nov 2026 | **Submission Date:** 23 Nov 2026  
**Supervisor:** Dr. Humera Noor  

---

## 📌 Post Draft 1: Dennis Sebastian (Lead Focus: Data Engineering, Leakage Mitigation & Baseline Modeling)

```text
🚀 [Sprint 2 Update] Milestone Achieved: Building a Leak-Free Preprocessing Pipeline & Baseline ML Models for Healthcare Claim Denial Explainability! 🏥📊

I am pleased to share our Sprint 2 progress for our Master of Data Science Capstone Project at the University of Europe for Applied Sciences, guided by Dr. Humera Noor and alongside my teammate Saran Jayakumaran Nair Sasikala.

In this sprint, we transitioned from preliminary data exploration into engineering an end-to-end, production-grade preprocessing and baseline modeling pipeline on the California Department of Managed Health Care (DMHC) Independent Medical Review (IMR) dataset.

🔍 Key Engineering & Modeling Highlights:
1️⃣ Data Hygiene & Missing Cohort Auditing:
From 42,749 raw records, we flagged 39 exact duplicate entries and uncovered that missing demographic attributes (Age/Gender) and review timelines occupied distinct, non-overlapping reporting cohorts. Through complete-case sanitization, we retained 41,332 high-fidelity cases (96.69% retention) without introducing synthetic imputation noise.

2️⃣ Mitigating Retrospective Data Leakage:
A vital lesson in healthcare analytics: post-hoc physician reviewer text summaries (`Findings`) contain direct outcome declarations (e.g., "denial should be upheld"). Including unmasked text in tabular models creates artificial 100% memorization. We systematically isolated clinical text narratives and separated pre-determination review turnaround duration (`DaysToReview`) from post-adjudication administrative lag (`DaysToAdopt`).

3️⃣ Baseline Machine Learning Benchmarks (80/20 Stratified Test Partition):
• Logistic Regression (Linear Baseline): Accuracy: 58.86% | ROC-AUC: 0.632
• Random Forest (100 Trees, Depth 12): Accuracy: 67.22% | ROC-AUC: 0.747 | Precision (Overturned): 72.52%
• Hist Gradient Boosting (LightGBM equivalent): Accuracy: 68.07% | ROC-AUC: 0.745 | F1-Score: 0.683

💡 Clinical & Economic Impact:
Achieving 72.52% precision on overturned claim denials proves that tree ensembles can reliably detect disputed claims with strong reversal merit—offering immediate operational value to enterprise health plans (such as Cigna, Aetna, CVS Health, Optum, and Elevance Health) to proactively correct erroneous claim rejections and accelerate patient access to vital care.

Up Next in Sprint 3: Hyperparameter optimization across gradient-boosted trees (GridSearchCV/RandomizedSearchCV) and preparing our model weights for Global Explainable AI (SHAP TreeExplainer).

Feedback and insights from healthcare AI practitioners and data scientists are always welcome! 👇

#DataScience #MachineLearning #HealthcareAnalytics #ExplainableAI #XAI #HealthTech #HealthInsurance #Python #ScikitLearn #UniversityOfEurope #SprintProgress #Capstone
```

---

## 📌 Post Draft 2: Saran Jayakumaran Nair Sasikala (Teammate Focus: Clinical Feature Hierarchy & Algorithmic Fairness)

```text
💡 [Sprint 2 Progress] From Raw Clinical Records to Interpretable AI: Feature Engineering & Baseline Model Benchmarking in Healthcare Claims 🩺🤖

Excited to share our latest milestone in our Master's Capstone Project at the University of Europe for Applied Sciences under the supervision of Dr. Humera Noor, together with my project partner Dennis Sebastian.

Our core mission is creating a **Transparent AI Framework** that not only predicts healthcare claim denial determinations from California DMHC IMR data but explains the underlying clinical rationale to clinicians and patients.

Key Milestones from Sprint 2:
✅ Clinical Taxonomies & Feature Architecture:
Transformed 41,332 cleaned patient dispute records using ordinal lifecycle mappings (Age bands 0–6) and high-cardinality encodings across 532 diagnosis subcategories and 498 treatment classifications.

✅ Feature Importance & Fairness Insights:
Gini importance diagnostics in our ensemble models revealed that claim adjudications are overwhelmingly driven by procedure subcategories and medical necessity dispute criteria, while demographic attributes (Patient Gender and Age) contribute minimally (<2%). This provides a crucial early safeguard against algorithmic demographic bias.

✅ Benchmark Results:
Our tree ensembles demonstrated strong non-linear signal, reaching an ROC-AUC of 0.747 and an F1-Score of 0.683 on strictly isolated, stratified held-out data (N=8,267).

Looking forward to diving into Sprint 3 hyperparameter fine-tuning and laying the groundwork for SHAP and LIME interpretability frameworks!

#HealthcareAI #ExplainableAI #DataEngineering #ResponsibleAI #HealthInformatics #MachineLearning #GraduateResearch #DataScience
```
