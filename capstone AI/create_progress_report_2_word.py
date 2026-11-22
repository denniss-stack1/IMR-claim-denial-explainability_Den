import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def generate_report():
    doc = Document()

    # Set 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base styling
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(6)

    def add_centered_heading(text, space_before=12, space_after=6):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.bold = True
        run.underline = True
        run.font.size = Pt(11.5)
        run.font.name = 'Arial'
        return p

    def add_body_p(text, space_after=6):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.size = Pt(11)
        run.font.name = 'Arial'
        return p

    # ================= PAGE 1 =================
    p_title1 = doc.add_paragraph()
    p_title1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title1.paragraph_format.space_before = Pt(10)
    p_title1.paragraph_format.space_after = Pt(16)
    r1 = p_title1.add_run("PROGRESS REPORT 2")
    r1.bold = True
    r1.font.size = Pt(16)
    r1.font.name = 'Arial'

    p_title2 = doc.add_paragraph()
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title2.paragraph_format.space_after = Pt(16)
    r2 = p_title2.add_run("Transparent AI Framework for Identifying and\nExplaining Claim Denials in Healthcare")
    r2.bold = True
    r2.font.size = Pt(14)
    r2.font.name = 'Arial'

    meta_lines = [
        "Master of Data Science",
        "UE – University of Europe for Applied Sciences",
        "",
        "Students: Dennis Sebastian (59593398)",
        "Saran Jayakumaran Nair Sasikala (56500625)",
        "",
        "Supervisor: Dr. Humera Noor",
        "",
        "Sprint 2: Data Preprocessing, Leakage Mitigation & Baseline Modeling",
        "Reporting Period: 09 Nov 2026 – 22 Nov 2026",
        "Submission Date: 23 Nov 2026"
    ]
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(18)
    p_meta.paragraph_format.line_spacing = 1.15
    for i, line in enumerate(meta_lines):
        r = p_meta.add_run(line + ("\n" if i < len(meta_lines)-1 else ""))
        r.font.size = Pt(11)
        r.font.name = 'Arial'

    add_centered_heading("Executive Summary", space_before=14, space_after=6)
    add_body_p(
        "Sprint 2 focused on engineering an automated, reproducible data preprocessing pipeline, "
        "resolving non-overlapping missing value cohorts, eliminating duplicate records, mitigating retrospective "
        "clinical data leakage, performing stratified 80/20 partitioning, and benchmarking three baseline machine "
        "learning models on the California DMHC IMR dataset."
    )

    add_centered_heading("Sprint Objectives", space_before=12, space_after=6)
    add_body_p(
        "Data cleansing and deduplication, non-overlapping missing value resolution, clinical text findings isolation, "
        "ordinal and categorical feature encoding, stratified train/test split, baseline model implementation (Logistic Regression, "
        "Random Forest, Hist Gradient Boosting), evaluation benchmarking, and preparation of Progress Report 2."
    )

    add_centered_heading("Project Overview", space_before=12, space_after=6)
    add_body_p(
        "The project aims to develop a transparent AI framework that predicts whether healthcare claim denials are upheld "
        "or overturned during Independent Medical Review (IMR) and explains the reasons behind predictions using Explainable AI "
        "methods such as SHAP and LIME."
    )

    doc.add_page_break()

    # ================= PAGE 2 =================
    add_centered_heading("Dataset Overview", space_before=0, space_after=6)
    add_body_p(
        "The study uses the California Department of Managed Health Care Independent Medical Review Determinations dataset (42,749 raw records). "
        "Key variables identified include ReportYear, DiagnosisCategory, TreatmentCategory, Determination, AgeRange, PatientGender, IMRType, "
        "DaysToReview, DaysToAdopt, and Findings."
    )
    p_link = doc.add_paragraph()
    p_link.paragraph_format.space_after = Pt(12)
    p_link.paragraph_format.line_spacing = 1.15
    r_link_lbl = p_link.add_run("Can find the\nlink:")
    r_link_lbl.font.size = Pt(11)
    r_link_url = p_link.add_run("https://drive.google.com/file/d/11apMqXGhHm5qkCJo5GM7O2gXmcyNGZrH/view?usp=sharing")
    r_link_url.font.size = Pt(11)
    r_link_url.font.color.rgb = RGBColor(0, 0, 238)
    r_link_url.underline = True

    add_centered_heading("GitHub Repository Setup", space_before=10, space_after=6)
    p_gh = doc.add_paragraph()
    p_gh.paragraph_format.space_after = Pt(10)
    p_gh.paragraph_format.line_spacing = 1.15
    r_gh1 = p_gh.add_run(
        "A dedicated GitHub repository and project board were created to manage sprint activities, milestones, deliverables, and project documentation.\n"
    )
    r_gh1.font.size = Pt(11)
    r_gh2 = p_gh.add_run("https://github.com/denniss-stack1/IMR-claim-denial-explainability_Den")
    r_gh2.font.size = Pt(11)
    r_gh2.font.color.rgb = RGBColor(0, 0, 238)
    r_gh2.underline = True

    # Image: GitHub repo screenshot
    gh_img_path = r"extracted_report1_images\p2_img1_Image21.png"
    if os.path.exists(gh_img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(0)
        p_img.add_run().add_picture(gh_img_path, width=Inches(5.7))

    doc.add_page_break()

    # ================= PAGE 3 =================
    add_centered_heading("Data Cleansing and Preprocessing", space_before=0, space_after=6)
    add_body_p(
        "Data hygiene activities in Sprint 2 included auditing duplicate rows, analyzing non-overlapping missing value cohorts across "
        "demographics and review timelines, and establishing complete case sanitization. From 42,749 raw records, 39 duplicates and 1,378 "
        "incomplete cases were purged, retaining 41,332 high-fidelity records (96.69% retention) with preserved 52.94% class balance."
    )

    if os.path.exists("fig1_data_cleaning_audit.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(8)
        p_img.add_run().add_picture("fig1_data_cleaning_audit.png", width=Inches(5.5))

    if os.path.exists("fig2_target_stratification.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(0)
        p_img.add_run().add_picture("fig2_target_stratification.png", width=Inches(5.0))

    doc.add_page_break()

    # ================= PAGE 4 =================
    add_centered_heading("Baseline Model Development & Benchmarking", space_before=0, space_after=6)
    add_body_p(
        "Three baseline machine learning models were developed on the 80/20 stratified split (33,065 training cases, 8,267 testing cases): "
        "standardized Logistic Regression as an interpretable linear baseline, Random Forest (100 trees, depth 12), and Hist Gradient Boosting (LightGBM equivalent). "
        "Random Forest achieved a top ROC-AUC of 0.747 and 72.52% Precision on overturned claim denials, while Hist Gradient Boosting achieved 68.07% Accuracy and a balanced 0.683 F1-Score."
    )

    if os.path.exists("fig3_roc_comparison.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(8)
        p_img.add_run().add_picture("fig3_roc_comparison.png", width=Inches(5.6))

    doc.add_page_break()

    # ================= PAGE 5 =================
    add_centered_heading("Ethics and Limitations", space_before=0, space_after=6)
    add_body_p(
        "The dataset is publicly available and contains no direct patient identifiers. Risks identified include selection bias, "
        "class imbalance across rare diagnoses, and potential demographic bias. Feature importance analysis confirmed that patient gender "
        "accounts for under 2% of overall model split decisions, mitigating disparate impact."
    )

    add_centered_heading("Challenges Encountered", space_before=10, space_after=6)
    add_body_p(
        "Challenges included discovering the non-overlapping nature of demographic vs review duration missing value cohorts, "
        "preventing retrospective text leakage from physician reviewer findings, and harmonizing high-cardinality clinical taxonomies across 500+ subcategories."
    )

    if os.path.exists("fig4_confusion_matrices.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(0)
        p_img.add_run().add_picture("fig4_confusion_matrices.png", width=Inches(5.8))

    doc.add_page_break()

    # ================= PAGE 6 =================
    if os.path.exists("fig5_feature_importance.png"):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(12)
        p_img.add_run().add_picture("fig5_feature_importance.png", width=Inches(5.6))

    add_centered_heading("Sprint 3 Plan", space_before=8, space_after=6)
    add_body_p(
        "Sprint 3 will focus on hyperparameter optimization (5-fold cross-validated GridSearchCV) across tree ensembles (Random Forest, "
        "LightGBM, CatBoost), frequency encoding for high-cardinality clinical categories, and champion model architecture selection (best_model.pkl) "
        "in preparation for SHAP TreeExplainer global explainability in Sprint 4."
    )

    add_centered_heading("Conclusion", space_before=8, space_after=6)
    add_body_p(
        "Sprint 2 successfully engineered an automated, leak-free data preprocessing pipeline, established balanced stratified train/test partitions, "
        "and delivered strong baseline model benchmarks (ROC-AUC 0.747, Overturn Precision 72.52%). Additionally, companies like Cigna, Aetna, "
        "CVS Health, Optum, and Elevance Health can use this transparent model framework to detect and resolve erroneous claim denials proactively."
    )

    docx_path = "Progress_Report_2_IMR_Healthcare_XAI.docx"
    doc.save(docx_path)
    print(f"Saved {docx_path} successfully!")

if __name__ == '__main__':
    generate_report()
