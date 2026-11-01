# 🗺️ Project Roadmap & Sprint Plan
## Transparent AI Framework for Healthcare Claim Denial Explanations
### Masters Capstone — University of Europe for Applied Sciences

> **Author:** Dennis Sebastian | **Updated:** November 2026

---

## 📅 Sprint Timeline at a Glance

| Sprint | Category | Start | Deadline | Status |
|--------|----------|-------|----------|--------|
| Sprint 1 | EDA + Data Engineering (initial) | Oct 1, 2026 | **Nov 1, 2026** | ✅ Completed |
| Sprint 2 | Data Engineering (full pipeline) | Nov 2, 2026 | **Nov 15, 2026** | 🔵 Active |
| Sprint 3 | Machine Learning | Nov 16, 2026 | **Nov 30, 2026** | ⬜ Upcoming |
| Sprint 4 | Explainability (Global XAI) | Dec 1, 2026 | **Dec 14, 2026** | ⬜ Upcoming |
| Sprint 5 | Explainability (Local XAI) | Dec 15, 2026 | **Dec 28, 2026** | ⬜ Upcoming |
| Sprint 6 | Documentation + Presentation | Dec 29, 2026 | **Jan 16, 2027** | ⬜ Upcoming |

---

## ✅ Sprint 1 — EDA & Initial Data Engineering
📅 **Oct 1 – Nov 1, 2026** | 🏷️ Categories: `EDA` `Data Engineering` | ✅ **COMPLETED**

### 🎯 Sprint Goal
Understand the IMR dataset end-to-end, establish the research questions, and complete the first progress report.

### 📋 Tasks

#### 🗄️ Data Engineering
- [x] Download IMR Dataset from DMHC (42,749 rows, 14 columns)
- [x] Review Data Dictionary — understand all 14 columns
- [x] Dataset Profiling: shape, dtypes, missing values, class balance
- [x] Store raw data in `data/raw/`
- [x] Upload dataset to Google Drive for sharing

#### 📊 EDA
- [x] Target variable analysis (`Determination` — 52.5% Overturned / 47.5% Upheld)
- [x] Feature distributions (AgeRange, PatientGender, DiagnosisCategory)
- [x] Temporal trend analysis (ReportYear 2001–2026)
- [x] Missing value audit (691 rows, 1.62% — AgeRange, PatientGender, DaysToReview)
- [x] Correlation and frequency analysis
- [x] Literature Review (XAI, SHAP, LIME, healthcare AI)

#### 📝 Documentation
- [x] GitHub repo initialized and structured
- [x] README.md written with project overview
- [x] ROADMAP.md created
- [x] Progress Report 1 submitted ✅

### 📦 Deliverables
- `notebooks/01_EDA.ipynb`
- `outputs/reports/progress_report_1.pdf`

---

## 🔵 Sprint 2 — Full Data Engineering Pipeline
📅 **Nov 2 – Nov 15, 2026** | 🏷️ Category: `Data Engineering` | 🔵 **ACTIVE NOW**

### 🎯 Sprint Goal
Build a complete, reproducible preprocessing pipeline that transforms raw IMR data into model-ready features.

### 📋 Tasks

#### 🗄️ Data Engineering
- [ ] **Missing Values**: Drop the 691 rows missing AgeRange / PatientGender / DaysToReview (only 1.62%)
- [ ] **Target Encoding**: `Determination` → Binary (Overturned=1, Upheld=0)
- [ ] **Ordinal Encoding**: `AgeRange` → integer order (0–6)
  ```
  0–10=0, 11–20=1, 21–30=2, 31–40=3, 41–50=4, 51–64=5, 65+=6
  ```
- [ ] **Label Encoding**: `PatientGender`, `IMRType`, `Type`
- [ ] **Label Encoding**: `DiagnosisCategory`, `DiagnosisSubCategory` (high cardinality)
- [ ] **Label Encoding**: `TreatmentCategory`, `TreatmentSubCategory`
- [ ] **Keep as Numeric**: `ReportYear`, `DaysToReview`, `DaysToAdopt`
- [ ] **Drop**: `ReferenceID` (ID column), `Findings` (raw text — optional NLP extension)
- [ ] Train/Test split (80/20, stratified, random_state=42)
- [ ] Save processed dataset → `data/processed/imr_processed.csv`
- [ ] Save label encoders → `models/encoders.pkl`

#### 📝 Documentation
- [ ] Update README with preprocessing decisions
- [ ] Commit all changes to GitHub

### 📦 Deliverables
- `notebooks/02_Preprocessing.ipynb`
- `data/processed/imr_processed.csv`
- `models/encoders.pkl`

### ⏰ Deadline: **November 15, 2026**

---

## ⬜ Sprint 3 — Machine Learning
📅 **Nov 16 – Nov 30, 2026** | 🏷️ Category: `Machine Learning` | ⬜ **UPCOMING**

### 🎯 Sprint Goal
Train multiple classifiers, tune the best model, and produce a rigorous evaluation. Select the final model for XAI.

### 📋 Tasks

#### 🤖 Machine Learning
- [ ] **Train 4 models** on preprocessed data:
  | Model | Notes |
  |-------|-------|
  | Logistic Regression | Interpretable baseline |
  | Random Forest | 100 estimators, max_depth=None |
  | XGBoost | n_estimators=200, learning_rate=0.1 |
  | LightGBM | Fast gradient boosting |
- [ ] **Evaluate all models**:
  - Accuracy, Precision, Recall, F1-Score
  - ROC-AUC Score
  - Confusion Matrix
- [ ] **Model Comparison Table** — identify best performer
- [ ] **Hyperparameter Tuning** on best model (GridSearchCV, 5-fold CV):
  ```python
  param_grid = {
      'n_estimators': [100, 200, 300],
      'max_depth': [3, 5, 7, None],
      'learning_rate': [0.01, 0.1, 0.2]
  }
  ```
- [ ] **Final Evaluation** on held-out test set
- [ ] Save best model → `models/best_model.pkl`
- [ ] Generate output plots:
  - ROC Curve (all 4 models)
  - Confusion Matrix (best model)
  - Learning Curve

#### 📝 Documentation
- [ ] Progress Report 2 — model performance section
- [ ] Commit notebooks and model to GitHub

### 📦 Deliverables
- `notebooks/03_Modeling.ipynb`
- `models/best_model.pkl`
- `outputs/figures/roc_curves_comparison.png`
- `outputs/figures/confusion_matrix_best.png`

### ⏰ Deadline: **November 30, 2026**

---

## ⬜ Sprint 4 — Explainability: Global XAI (SHAP)
📅 **Dec 1 – Dec 14, 2026** | 🏷️ Category: `Explainability` | ⬜ **UPCOMING**

### 🎯 Sprint Goal
Use SHAP to explain the model's overall behaviour — answer *"What does the model rely on globally?"*

### 📋 Tasks

#### 🔍 Explainability
- [ ] Initialize `shap.TreeExplainer(best_model)`
- [ ] Compute SHAP values for entire test set
- [ ] **Global SHAP Plots**:
  - [ ] Summary Bar Chart (feature importance ranking)
  - [ ] Beeswarm Plot (impact direction + magnitude)
  - [ ] Dependence Plot — `DiagnosisCategory`
  - [ ] Dependence Plot — `TreatmentCategory`
  - [ ] Dependence Plot — `Type` (Medical Necessity vs Experimental)
  - [ ] Dependence Plot — `AgeRange`
  - [ ] Dependence Plot — `DaysToReview`
- [ ] **Fairness Analysis**:
  - Mean SHAP value of `PatientGender` → Does gender influence predictions?
  - Mean SHAP value of `AgeRange` → Does age introduce bias?
  - Subgroup analysis: Overturned rate by AgeRange and Gender
- [ ] Compare SHAP importance vs built-in feature importance
- [ ] Write findings narrative (which features drive denials?)

#### 📝 Documentation
- [ ] Document all SHAP findings with domain interpretations
- [ ] Commit to GitHub

### 📦 Deliverables
- `notebooks/04_XAI_Global_SHAP.ipynb`
- `outputs/figures/shap_summary_bar.png`
- `outputs/figures/shap_beeswarm.png`
- `outputs/figures/shap_dependence_[feature].png` (×5)
- `outputs/figures/fairness_analysis.png`

### ⏰ Deadline: **December 14, 2026**

---

## ⬜ Sprint 5 — Explainability: Local XAI (SHAP + LIME)
📅 **Dec 15 – Dec 28, 2026** | 🏷️ Category: `Explainability` | ⬜ **UPCOMING**

### 🎯 Sprint Goal
Explain individual predictions — answer *"Why did the model predict THIS for THIS patient?"* Compare SHAP and LIME.

### 📋 Tasks

#### 🔍 Explainability
- [ ] **Select 5 representative cases** from test set:
  | Case | Type | Why Selected |
  |------|------|-------------|
  | Case 1 | True Positive (correct Overturned) | High-confidence correct |
  | Case 2 | True Negative (correct Upheld) | High-confidence correct |
  | Case 3 | False Positive (wrong Overturned) | Model error — why? |
  | Case 4 | False Negative (wrong Upheld) | Model error — why? |
  | Case 5 | Edge Case (probability ≈ 0.50) | Borderline decision |
- [ ] **SHAP Local Plots** for each case:
  - Force Plot
  - Waterfall Plot
- [ ] **LIME Explanations** for each case:
  - `LimeTabularExplainer` with 10 features
  - Save as HTML + PNG
- [ ] **SHAP vs LIME Comparison Table** — agreements / disagreements
- [ ] Write narrative: What do local explanations reveal that global ones don't?

#### 📝 Documentation
- [ ] Document all local explanations with clinical context
- [ ] Commit to GitHub

### 📦 Deliverables
- `notebooks/05_XAI_Local_SHAP_LIME.ipynb`
- `outputs/figures/shap_force_case_[1-5].png`
- `outputs/figures/shap_waterfall_case_[1-5].png`
- `outputs/figures/lime_case_[1-5].html`

### ⏰ Deadline: **December 28, 2026**

---

## ⬜ Sprint 6 — Documentation & Presentation
📅 **Dec 29, 2026 – Jan 16, 2027** | 🏷️ Category: `Documentation` `Presentation` | ⬜ **UPCOMING**

### 🎯 Sprint Goal
Compile all work into a polished academic report and deliver a compelling final presentation.

### 📋 Tasks

#### 📝 Documentation (Final Report)
- [ ] **Abstract** (250 words): Summary of research, methods, findings
- [ ] **Chapter 1 — Introduction**: Motivation, problem statement, RQs, objectives
- [ ] **Chapter 2 — Literature Review**: XAI, SHAP, LIME, healthcare AI papers (20+ references)
- [ ] **Chapter 3 — Dataset & Methodology**: IMR data, preprocessing decisions, model pipeline
- [ ] **Chapter 4 — Results**: Model performance tables, ROC curves, confusion matrices
- [ ] **Chapter 5 — XAI Analysis**:
  - Global SHAP findings
  - Local SHAP + LIME findings
  - SHAP vs LIME comparison
- [ ] **Chapter 6 — Discussion & Fairness**: Domain implications, bias analysis, limitations
- [ ] **Chapter 7 — Conclusion**: Summary, limitations, future work
- [ ] **References** (IEEE format, 20+ sources)
- [ ] **Appendix**: Full code listing, extra plots
- [ ] Final proofreading and formatting

#### 🎤 Presentation
- [ ] Create slide deck (15–20 slides):
  | Slide | Content |
  |-------|---------|
  | 1 | Title + Author |
  | 2 | Agenda |
  | 3 | Problem Statement & Motivation |
  | 4 | Dataset Overview |
  | 5 | Methodology Pipeline |
  | 6 | EDA Highlights |
  | 7 | Model Results |
  | 8 | Global SHAP — Summary Plot |
  | 9 | Global SHAP — Feature Dependence |
  | 10 | Fairness Analysis |
  | 11–13 | Local XAI — 3 Case Studies |
  | 14 | SHAP vs LIME Comparison |
  | 15 | Discussion & Limitations |
  | 16 | Conclusion & Future Work |
  | 17 | Q&A |
- [ ] Practice presentation (aim for 15 minutes + 5 min Q&A)

#### GitHub Final Cleanup
- [ ] Clean and comment all 5 notebooks
- [ ] Update README with final model results table
- [ ] Ensure all figures are in `outputs/figures/`
- [ ] Tag final release: `git tag v1.0.0`

### 📦 Deliverables
- `outputs/reports/capstone_final_report.pdf`
- `outputs/reports/capstone_presentation.pptx`
- All 5 notebooks cleaned and documented
- GitHub repo fully finalized

### ⏰ Deadline: **January 16, 2027** 🎓

---

## 🧭 Research Questions Tracker

| # | Research Question | Sprint | Status |
|---|------------------|--------|--------|
| RQ1 | Can ML predict claim denial outcomes accurately? | Sprint 3 | ⬜ |
| RQ2 | Which features drive model decisions globally? | Sprint 4 | ⬜ |
| RQ3 | How to explain individual case predictions? | Sprint 5 | ⬜ |
| RQ4 | Do demographics (age/gender) introduce bias? | Sprint 4–5 | ⬜ |
| RQ5 | How do SHAP and LIME compare? | Sprint 5 | ⬜ |

---

## 📊 Category Coverage Map

| Category | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Sprint 5 | Sprint 6 |
|----------|----------|----------|----------|----------|----------|----------|
| 🗄️ Data Engineering | ✅ | 🔵 | | | | |
| 📊 EDA | ✅ | ✅ | | | | |
| 🤖 Machine Learning | | | ⬜ | | | |
| 🔍 Explainability | | | | ⬜ | ⬜ | |
| 📝 Documentation | ✅ | 🔵 | 🔵 | 🔵 | 🔵 | ⬜ |
| 🎤 Presentation | | | | | | ⬜ |

---

## 🔗 Key Links

| Resource | Link |
|----------|------|
| GitHub Repository | [IMR-claim-denial-explainability_Den](https://github.com/denniss-stack1/IMR-claim-denial-explainability_Den) |
| GitHub Project Board | [Project Board](https://github.com/users/denniss-stack1/projects/3/views/3) |
| Dataset (Google Drive) | [Download CSV](https://drive.google.com/drive/folders/15fLR5dd4anqQThCnm20Vw2C1Pe7tYKXE?usp=drive_link) |
| Dataset (Official) | [DMHC Open Data](https://www.dmhc.ca.gov/data-and-statistics.aspx) |

---

*Last updated: November 2026 | Dennis Sebastian | University of Europe for Applied Sciences*
