import os
import json
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix
)

os.makedirs('outputs/figures', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('models', exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Load raw dataset
raw_path = 'independent-medical-review-imr-determinations-trends.csv'
df_raw = pd.read_csv(raw_path)
df_raw.columns = df_raw.columns.str.strip()
n_raw = len(df_raw)

# 1. Audit Duplicates
n_dups = df_raw.duplicated().sum()
df_dedup = df_raw.drop_duplicates().copy()
n_dedup = len(df_dedup)

# 2. Audit Missing
missing_summary = df_dedup.isnull().sum()
critical_cols = ['AgeRange', 'PatientGender', 'DaysToReview', 'DiagnosisSubCategory', 'TreatmentSubCategory']
df_clean = df_dedup.dropna(subset=critical_cols).copy()
n_clean = len(df_clean)

# Save figure 1: Data Cleansing Audit
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
steps = ['Raw Ingestion', 'Post De-duplication', 'Complete Case Analysis\n(Post Null Handling)']
counts = [n_raw, n_dedup, n_clean]
bars = ax.bar(steps, counts, color=['#1e3a8a', '#2563eb', '#0d9488'], width=0.5)
ax.set_ylim(35000, 45000)
ax.set_ylabel('Record Count', fontweight='bold')
ax.set_title('IMR Dataset Ingestion & Cleansing Funnel (Sprint 2)', fontsize=12, fontweight='bold', pad=12)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 150, f'{yval:,} ({yval/n_raw*100:.1f}%)', ha='center', va='bottom', fontweight='bold', fontsize=9)
plt.tight_layout()
fig.savefig('outputs/figures/fig1_data_cleaning_audit.png')
fig.savefig('fig1_data_cleaning_audit.png')
plt.close()
print('Figure 1 created.')

# 3. Target Encoding: Overturned = 1, Upheld = 0
df_clean['Target'] = (df_clean['Determination'] == 'Overturned Decision of Health Plan').astype(int)

# 4. Ordinal AgeRange
age_map = {
    '0 to 10': 0, '11 to 20': 1, '21 to 30': 2, '31 to 40': 3,
    '41 to 50': 4, '51 to 64': 5, '65+': 6
}
df_clean['AgeRange_Ord'] = df_clean['AgeRange'].map(age_map)

# 5. Categorical Encoding
cat_cols = ['PatientGender', 'Type', 'IMRType', 'DiagnosisCategory', 'DiagnosisSubCategory', 'TreatmentCategory', 'TreatmentSubCategory']
encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df_clean[col + '_Enc'] = le.fit_transform(df_clean[col].astype(str))
    encoders[col] = le
encoders['AgeRange_Map'] = age_map

# Feature column selection (Omitting ReferenceID and Findings to prevent leakage; keeping clinical review duration)
feature_cols = ['ReportYear', 'AgeRange_Ord', 'DaysToReview', 'DaysToAdopt'] + [c + '_Enc' for c in cat_cols]
X = df_clean[feature_cols]
y = df_clean['Target']

# 6. Stratified Split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Save figure 2: Target Stratification
fig, ax = plt.subplots(figsize=(7, 4), dpi=300)
labels = ['Upheld (0)', 'Overturned (1)']
train_counts = [float(np.mean(y_train == 0)*100), float(np.mean(y_train == 1)*100)]
test_counts = [float(np.mean(y_test == 0)*100), float(np.mean(y_test == 1)*100)]
x = np.arange(len(labels))
width = 0.35
ax.bar(x - width/2, train_counts, width, label=f'Train Set (N={len(y_train):,})', color='#3b82f6')
ax.bar(x + width/2, test_counts, width, label=f'Test Set (N={len(y_test):,})', color='#10b981')
ax.set_ylabel('Proportion (%)', fontweight='bold')
ax.set_title('Target Stratification Consistency (Train vs Test)', fontsize=11, fontweight='bold', pad=10)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontweight='bold')
ax.set_ylim(0, 70)
ax.legend(frameon=True)
for i in range(len(x)):
    ax.text(x[i] - width/2, train_counts[i] + 1.2, f'{train_counts[i]:.2f}%', ha='center', fontsize=9, fontweight='bold')
    ax.text(x[i] + width/2, test_counts[i] + 1.2, f'{test_counts[i]:.2f}%', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
fig.savefig('outputs/figures/fig2_target_stratification.png')
fig.savefig('fig2_target_stratification.png')
plt.close()
print('Figure 2 created.')

# 7. Model Training & Benchmarking
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)

rf = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, n_jobs=4)
rf.fit(X_train, y_train)

hgb = HistGradientBoostingClassifier(max_iter=100, random_state=42)
hgb.fit(X_train, y_train)

models = {
    'Logistic Regression': (lr, X_test_scaled),
    'Random Forest': (rf, X_test),
    'Hist Gradient Boosting': (hgb, X_test)
}

metrics_summary = {}
preds_dict = {}
probs_dict = {}

for name, (mod, X_eval) in models.items():
    preds = mod.predict(X_eval)
    probs = mod.predict_proba(X_eval)[:, 1]
    preds_dict[name] = preds
    probs_dict[name] = probs
    acc = float(accuracy_score(y_test, preds))
    prec = float(precision_score(y_test, preds))
    rec = float(recall_score(y_test, preds))
    f1 = float(f1_score(y_test, preds))
    auc = float(roc_auc_score(y_test, probs))
    metrics_summary[name] = {
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-Score': f1,
        'ROC-AUC': auc,
        'ConfusionMatrix': confusion_matrix(y_test, preds).tolist()
    }
    print(f'{name} -> Acc: {acc:.4f}, AUC: {auc:.4f}')

# Save figure 3: ROC Curve Comparison
fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
colors = {'Logistic Regression': '#ef4444', 'Random Forest': '#3b82f6', 'Hist Gradient Boosting': '#10b981'}
for name in models.keys():
    fpr, tpr, _ = roc_curve(y_test, probs_dict[name])
    auc_val = metrics_summary[name]['ROC-AUC']
    ax.plot(fpr, tpr, label=f'{name} (AUC = {auc_val:.3f})', color=colors[name], lw=2)
ax.plot([0, 1], [0, 1], 'k--', lw=1.5, alpha=0.6, label='Random Guess (AUC = 0.500)')
ax.set_xlabel('False Positive Rate (1 - Specificity)', fontweight='bold')
ax.set_ylabel('True Positive Rate (Sensitivity / Recall)', fontweight='bold')
ax.set_title('Baseline Model ROC-AUC Comparison (Sprint 2 Benchmark)', fontsize=11, fontweight='bold', pad=10)
ax.legend(loc='lower right', frameon=True)
plt.tight_layout()
fig.savefig('outputs/figures/fig3_roc_comparison.png')
fig.savefig('fig3_roc_comparison.png')
plt.close()
print('Figure 3 created.')

# Save figure 4: Confusion Matrix Grid
fig, axes = plt.subplots(1, 3, figsize=(14, 4), dpi=300)
for idx, name in enumerate(models.keys()):
    cm = np.array(metrics_summary[name]['ConfusionMatrix'])
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=False,
                xticklabels=['Upheld', 'Overturned'], yticklabels=['Upheld', 'Overturned'])
    f1_val = metrics_summary[name]['F1-Score']
    acc_val = metrics_summary[name]['Accuracy'] * 100
    axes[idx].set_title(f'{name}\nF1: {f1_val:.3f} | Acc: {acc_val:.1f}%', fontweight='bold', fontsize=10)
    axes[idx].set_xlabel('Predicted Label', fontweight='bold')
    if idx == 0:
        axes[idx].set_ylabel('True Label', fontweight='bold')
plt.tight_layout()
fig.savefig('outputs/figures/fig4_confusion_matrices.png')
fig.savefig('fig4_confusion_matrices.png')
plt.close()
print('Figure 4 created.')

# Save figure 5: Feature Importance from Random Forest
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
feat_imp = pd.Series(rf.feature_importances_, index=feature_cols).sort_values(ascending=True)
clean_names = {
    'ReportYear': 'Report Year',
    'AgeRange_Ord': 'Patient Age Range (Ordinal)',
    'DaysToReview': 'Days to Complete Review',
    'DaysToAdopt': 'Days to Adopt Ruling',
    'PatientGender_Enc': 'Patient Gender',
    'Type_Enc': 'Review Type (Medical Necessity vs Exp)',
    'IMRType_Enc': 'IMR Processing Type (Std vs Expedited)',
    'DiagnosisCategory_Enc': 'Diagnosis Primary Category',
    'DiagnosisSubCategory_Enc': 'Diagnosis Sub-Category',
    'TreatmentCategory_Enc': 'Treatment Primary Category',
    'TreatmentSubCategory_Enc': 'Treatment Sub-Category'
}
feat_imp.index = [clean_names.get(x, x) for x in feat_imp.index]
feat_imp.plot(kind='barh', color='#0284c7', ax=ax, width=0.6)
ax.set_xlabel('Gini Feature Importance', fontweight='bold')
ax.set_title('Random Forest Feature Importance Hierarchy (Baseline)', fontsize=11, fontweight='bold', pad=10)
plt.tight_layout()
fig.savefig('outputs/figures/fig5_feature_importance.png')
fig.savefig('fig5_feature_importance.png')
plt.close()
print('Figure 5 created.')

# 8. Save Processed Datasets & Models
df_clean.to_csv('data/processed/imr_processed.csv', index=False)
df_clean.to_csv('imr_processed.csv', index=False)
joblib.dump(encoders, 'models/encoders.pkl')
joblib.dump(encoders, 'encoders.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump({'lr': lr, 'rf': rf, 'hgb': hgb}, 'models/baseline_models.pkl')
joblib.dump({'lr': lr, 'rf': rf, 'hgb': hgb}, 'baseline_models.pkl')

with open('sprint2_metrics.json', 'w') as f:
    json.dump(metrics_summary, f, indent=2)

print('All Sprint 2 pipeline tasks, models, figures, and data saved successfully!')
