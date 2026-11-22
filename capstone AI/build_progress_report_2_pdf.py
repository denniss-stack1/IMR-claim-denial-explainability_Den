import os
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, 750, "Progress Report 2 | Transparent AI Framework for Healthcare Claim Denials")
            self.drawRightString(558, 750, "Sprint 2: Preprocessing & Baseline Models")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)
            
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "Master of Data Science | University of Europe for Applied Sciences — Dennis Sebastian & Saran Jayakumaran")
        self.drawRightString(558, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    pdf_path = "Progress_Report_2_IMR_Healthcare_XAI.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom palette
    c_primary = colors.HexColor("#1e3a8a")     # Deep Academic Blue
    c_secondary = colors.HexColor("#0284c7")   # Tech Blue
    c_dark = colors.HexColor("#0f172a")        # Slate 900
    c_body = colors.HexColor("#334155")        # Slate 700
    c_bg_light = colors.HexColor("#f8fafc")    # Light container
    c_border = colors.HexColor("#cbd5e1")
    
    # Custom typography
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=c_primary,
        alignment=0,
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=c_secondary,
        spaceAfter=8
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_body
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.5,
        textColor=c_body,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_body,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TD',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=c_body,
        alignment=1
    )

    table_cell_left = ParagraphStyle(
        'TDLeft',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=c_body,
        alignment=0
    )

    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#64748b"),
        alignment=1,
        spaceBefore=2,
        spaceAfter=6
    )

    story = []

    # ================= PAGE 1 =================
    story.append(Paragraph("PROGRESS REPORT 2", subtitle_style))
    story.append(Paragraph("Transparent AI Framework for Identifying and Explaining Claim Denials in Healthcare", title_style))
    story.append(Spacer(1, 4))
    
    meta_table_data = [
        [
            Paragraph("<b>Degree Program:</b> Master of Data Science", meta_val),
            Paragraph("<b>Reporting Period:</b> 09 Nov 2026 – 22 Nov 2026", meta_val)
        ],
        [
            Paragraph("<b>Institution:</b> UE – University of Europe for Applied Sciences", meta_val),
            Paragraph("<b>Submission Date:</b> 23 Nov 2026", meta_val)
        ],
        [
            Paragraph("<b>Students:</b> Dennis Sebastian (59593398) &amp; Saran Jayakumaran Nair Sasikala (56500625)", meta_val),
            Paragraph("<b>Sprint Category:</b> Data Engineering &amp; Baseline Modeling", meta_val)
        ],
        [
            Paragraph("<b>Supervisor:</b> Dr. Humera Noor", meta_val),
            Paragraph("<b>Milestone:</b> Sprint 2 Milestone Completion", meta_val)
        ]
    ]
    t_meta = Table(meta_table_data, colWidths=[260, 244])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_light),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Sprint 2 marks the critical evolution of the Transparent AI Capstone project from exploratory data analysis into full-scale data engineering, systematic data leakage mitigation, and baseline predictive modeling. Utilizing the California Department of Managed Health Care (DMHC) Independent Medical Review (IMR) dataset (42,749 raw determinations), the team implemented an automated, reproducible data preparation pipeline that enforces strict integrity standards, resolves demographic and timeline missing cohorts, encodes high-cardinality clinical taxonomies, and constructs stratified partitions. Three baseline machine learning architectures—Logistic Regression, Random Forest, and Hist Gradient Boosting—were benchmarked on a strictly isolated 80/20 test split (8,267 held-out records). The ensemble architectures achieved a top ROC-AUC of <b>0.747</b> and Accuracy of <b>68.1%</b> (with <b>72.5% Precision</b> on overturned claim denials), confirming strong non-linear predictive signal and establishing the foundational benchmark for Sprint 3 optimization and downstream Explainable AI (SHAP/LIME).",
        body_style
    ))

    story.append(Paragraph("2. Sprint 2 Objectives & Key Results (OKRs)", h1_style))
    obj_data = [
        [Paragraph("Objective / Task", table_header_style), Paragraph("Target Deliverable", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("Data Hygiene & Deduplication", table_cell_left), Paragraph("Identify and remove exact duplicate records", table_cell_left), Paragraph("<b>100% Completed</b> (39 dropped)", table_cell_style)],
        [Paragraph("Missing Value Resolution", table_cell_left), Paragraph("Audit demographic and review duration nulls", table_cell_left), Paragraph("<b>100% Completed</b> (1,378 rows handled)", table_cell_style)],
        [Paragraph("Data Leakage Mitigation", table_cell_left), Paragraph("Isolate post-hoc text findings & review timelines", table_cell_left), Paragraph("<b>100% Completed</b> (Findings text isolated)", table_cell_style)],
        [Paragraph("Feature Engineering & Encoding", table_cell_left), Paragraph("Ordinal Age (0–6), Categorical encodings", table_cell_left), Paragraph("<b>100% Completed</b> (encoders.pkl saved)", table_cell_style)],
        [Paragraph("Stratified Partitioning", table_cell_left), Paragraph("80/20 train/test split preserving 52.9% balance", table_cell_left), Paragraph("<b>100% Completed</b> (33,065 train / 8,267 test)", table_cell_style)],
        [Paragraph("Baseline Model Benchmarking", table_cell_left), Paragraph("Logistic Regression, Random Forest, HistGB", table_cell_left), Paragraph("<b>100% Completed</b> (Top AUC: 0.747)", table_cell_style)],
        [Paragraph("Artifact Persistence", table_cell_left), Paragraph("Clean CSV, models.pkl, encoders.pkl, notebook", table_cell_left), Paragraph("<b>100% Completed</b> (All saved to repo)", table_cell_style)]
    ]
    t_obj = Table(obj_data, colWidths=[150, 230, 124])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light])
    ]))
    story.append(t_obj)

    # ================= PAGE 2 =================
    story.append(PageBreak())
    story.append(Paragraph("3. Data Cleansing Pipeline & Audit Funnel", h1_style))
    story.append(Paragraph(
        "A major analytical breakthrough in Sprint 2 was uncovering the non-overlapping nature of dataset nulls. While Sprint 1 audited univariate null counts (691 in <i>AgeRange</i>, 691 in <i>PatientGender</i>, and 691 in <i>DaysToReview</i>), co-occurrence profiling proved that demographic omissions and review duration omissions belong to separate reporting eras and provider reporting groups. Specifically, 685 records lacked age and gender concurrently, while 691 entirely distinct records lacked review turnaround duration. Purging these along with 39 duplicates and 3 missing sub-category codes yielded a high-quality clean dataset of <b>41,332 records (96.69% retention)</b>, entirely free of synthetic imputation distortions.",
        body_style
    ))
    
    if os.path.exists("fig1_data_cleaning_audit.png"):
        story.append(KeepTogether([
            Image("fig1_data_cleaning_audit.png", width=6.2*inch, height=2.35*inch),
            Paragraph("Figure 1: IMR Ingestion, deduplication, and complete-case data cleansing funnel.", caption_style)
        ]))

    story.append(Paragraph("4. Data Leakage Assessment & Risk Controls", h1_style))
    story.append(Paragraph(
        "In healthcare dispute adjudication, models are vulnerable to subtle forms of retrospective data leakage. During Sprint 2, the team designed and implemented explicit safeguards:",
        body_style
    ))
    story.append(Paragraph("• <b>Reviewer Findings Text Isolation:</b> The <i>Findings</i> field contains clinical synopses written by the independent medical reviewer after adjudication. In-depth text inspection revealed explicit decision statements (e.g., <i>'Therefore, the Health Plan denial should be upheld'</i>). Directly using raw Findings in tabular models leads to 100% artificial target memorization. Findings text has been strictly sequestered for downstream natural language explanation validation.", bullet_style))
    story.append(Paragraph("• <b>Timeline Disentanglement:</b> <i>DaysToReview</i> reflects legitimate clinical dispute complexity (intake to determination). Conversely, <i>DaysToAdopt</i> represents administrative state record archiving occurring after decision rendering. Models are monitored to ensure administrative processing speed does not contaminate pre-dispute risk modeling.", bullet_style))
    story.append(Paragraph("• <b>Identifier Decontamination:</b> Administrative keys such as <i>ReferenceID</i> were stripped to prevent high-cardinality memorization.", bullet_style))

    # ================= PAGE 3 =================
    story.append(PageBreak())
    story.append(Paragraph("5. Clinical Feature Engineering & Stratified Partitioning", h1_style))
    story.append(Paragraph(
        "To maximize signal preservation across both clinical and demographic dimensions, the feature engineering pipeline transforms raw attributes into structured numerical representations:",
        body_style
    ))
    story.append(Paragraph("• <b>Target Variable Binarization:</b> The primary outcome <i>Determination</i> was encoded into a binary classification target: <b>1 = Overturned</b> (Health Plan denial revoked; treatment approved) and <b>0 = Upheld</b> (Health Plan denial affirmed). The cleaned cohort maintains a balanced class distribution: 21,881 Overturned (52.94%) vs 19,451 Upheld (47.06%).", bullet_style))
    story.append(Paragraph("• <b>Ordinal Lifecycle Encoding:</b> Patient age bands were mapped to ordered integer intervals representing clinical lifecycle stages: <i>0 to 10</i> → 0; <i>11 to 20</i> → 1; <i>21 to 30</i> → 2; <i>31 to 40</i> → 3; <i>41 to 50</i> → 4; <i>51 to 64</i> → 5; <i>65+</i> → 6.", bullet_style))
    story.append(Paragraph("• <b>Categorical Transformation:</b> Scikit-learn LabelEncoders were fitted on <i>PatientGender</i>, <i>Type</i> (Medical Necessity vs Experimental), <i>IMRType</i> (Standard vs Expedited), <i>DiagnosisCategory</i> (48 classes), <i>DiagnosisSubCategory</i> (532 classes), <i>TreatmentCategory</i> (58 classes), and <i>TreatmentSubCategory</i> (498 classes). Encoders were saved to <code>models/encoders.pkl</code> for production reuse.", bullet_style))
    story.append(Paragraph("• <b>Stratified 80/20 Partition:</b> The cleaned 41,332 cases were partitioned using stratified sampling on the binary target with <code>random_state=42</code>. The training set comprises <b>33,065 records</b> and the held-out evaluation set contains <b>8,267 records</b>. Both partitions maintain identical 52.94% Overturned ratios, eliminating partition skew.", bullet_style))

    if os.path.exists("fig2_target_stratification.png"):
        story.append(KeepTogether([
            Image("fig2_target_stratification.png", width=5.6*inch, height=2.4*inch),
            Paragraph("Figure 2: Target class balance consistency across train (N=33,065) and test (N=8,267) sets.", caption_style)
        ]))

    # ================= PAGE 4 =================
    story.append(PageBreak())
    story.append(Paragraph("6. Baseline Model Development & Benchmark Evaluation", h1_style))
    story.append(Paragraph(
        "To establish rigorous performance benchmarks ahead of advanced hyperparameter optimization in Sprint 3, three distinct model families were implemented on the 80/20 stratified split. StandardScaler was fitted on training features for the linear model, while tree ensembles operated on unscaled integer-encoded matrices.",
        body_style
    ))

    perf_data = [
        [Paragraph("Model Architecture", table_header_style), Paragraph("Accuracy", table_header_style), Paragraph("Precision", table_header_style), Paragraph("Recall", table_header_style), Paragraph("F1-Score", table_header_style), Paragraph("ROC-AUC", table_header_style)],
        [Paragraph("Logistic Regression (Standardized Linear)", table_cell_left), Paragraph("58.86%", table_cell_style), Paragraph("59.88%", table_cell_style), Paragraph("67.56%", table_cell_style), Paragraph("0.635", table_cell_style), Paragraph("0.632", table_cell_style)],
        [Paragraph("Random Forest (100 Trees, Depth 12)", table_cell_left), Paragraph("67.22%", table_cell_style), Paragraph("72.52%", table_cell_style), Paragraph("61.32%", table_cell_style), Paragraph("0.665", table_cell_style), Paragraph("<b>0.747</b>", table_cell_style)],
        [Paragraph("Hist Gradient Boosting (100 Iterations)", table_cell_left), Paragraph("<b>68.07%</b>", table_cell_style), Paragraph("71.97%", table_cell_style), Paragraph("65.00%", table_cell_style), Paragraph("<b>0.683</b>", table_cell_style), Paragraph("0.745", table_cell_style)]
    ]
    t_perf = Table(perf_data, colWidths=[170, 65, 65, 65, 65, 74])
    t_perf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light])
    ]))
    story.append(t_perf)
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>Performance Insights & Clinical Implications:</b><br/>"
        "• <b>Non-Linear Clinical Complexities:</b> Tree ensembles outperform the linear baseline by over 9.2 percentage points in accuracy and +0.114 in ROC-AUC. This highlights that insurance denials and reversals are governed by interaction effects (e.g., treatment category combined with specific age brackets and review urgency) rather than independent linear contributions.<br/>"
        "• <b>High Overturn Precision (72.52%):</b> In healthcare claims operations, precision on overturned denials is paramount. A high precision rate ensures that when the AI flags an appeal as having strong reversal likelihood, clinicians and case managers can intervene with high confidence, avoiding wasted administrative effort.<br/>"
        "• <b>Balanced Generalization:</b> Hist Gradient Boosting achieved the top F1-score (0.683), exhibiting optimal harmonic balance between false positives and false negatives.",
        body_style
    ))

    if os.path.exists("fig3_roc_comparison.png"):
        story.append(KeepTogether([
            Image("fig3_roc_comparison.png", width=5.6*inch, height=2.45*inch),
            Paragraph("Figure 3: ROC-AUC curves comparing Logistic Regression, Random Forest, and Hist Gradient Boosting.", caption_style)
        ]))

    # ================= PAGE 5 =================
    story.append(PageBreak())
    story.append(Paragraph("7. Clinical Confusion Matrices & Error Diagnostics", h1_style))
    story.append(Paragraph(
        "Evaluating confusion matrices across the 8,267 held-out test records reveals notable operational trade-offs between model families. Logistic Regression over-predicts overturned decisions (1,981 false positives), yielding high recall but low specificity. In contrast, Random Forest delivers superior specificity (2,873 true negatives out of 3,890 upheld cases), proving exceptionally reliable at confirming valid denials.",
        body_style
    ))

    if os.path.exists("fig4_confusion_matrices.png"):
        story.append(KeepTogether([
            Image("fig4_confusion_matrices.png", width=6.2*inch, height=1.85*inch),
            Paragraph("Figure 4: Confusion matrix grid across baseline architectures on held-out test data (N=8,267).", caption_style)
        ]))

    story.append(Paragraph("8. Clinical Feature Importance Hierarchy", h1_style))
    story.append(Paragraph(
        "Random Forest Gini importance diagnostics show that dispute outcomes are overwhelmingly governed by clinical procedure details (<i>TreatmentSubCategory</i>, <i>DiagnosisSubCategory</i>), dispute type (<i>Medical Necessity vs Experimental</i>), and case timeline duration. Notably, demographic attributes (gender and age) rank among the lowest predictors, confirming that decisions are medically driven rather than demographically biased.",
        body_style
    ))

    if os.path.exists("fig5_feature_importance.png"):
        story.append(KeepTogether([
            Image("fig5_feature_importance.png", width=6.0*inch, height=2.25*inch),
            Paragraph("Figure 5: Random Forest Gini feature importance ranking across engineered clinical attributes.", caption_style)
        ]))

    # ================= PAGE 6 =================
    story.append(PageBreak())
    story.append(Paragraph("9. Ethical Governance & Subgroup Fairness", h1_style))
    story.append(Paragraph(
        "Because healthcare claim adjudications directly dictate patient access to life-critical procedures, model fairness is an essential project requirement. Our Sprint 2 feature importance analysis verified that <i>PatientGender</i> accounts for less than 2% of overall tree split decisions. In Sprints 4 and 5, rigorous fairness audits (disparate impact ratio, equalized odds, and SHAP Beeswarm subgroup evaluations across age and gender) will be performed to certify that algorithmic recommendations do not perpetuate demographic biases.",
        body_style
    ))

    story.append(Paragraph("10. Business Translation & Industry Applicability", h1_style))
    story.append(Paragraph(
        "The Transparent AI Framework addresses critical friction points across the healthcare payer and provider ecosystem. Enterprise health plans and managed care organizations—including <b>Cigna, Aetna, CVS Health, Optum, and Elevance Health</b>—face millions of dollars in annual administrative overhead and member grievances due to protracted independent medical reviews. By predicting IMR outcomes with over 72% precision prior to formal state adjudication, insurers can proactively overturn erroneous denials, expedite patient care, mitigate litigation exposure, and reduce appeal management costs.",
        body_style
    ))

    story.append(Paragraph("11. Sprint 3 Action Plan & Roadmap Ahead", h1_style))
    story.append(Paragraph(
        "Sprint 3 (24 Nov – 07 Dec 2026) will focus on comprehensive model optimization and champion selection:<br/>"
        "• <b>Hyperparameter Optimization:</b> Implement 5-fold cross-validated GridSearchCV across Random Forest, LightGBM, and CatBoost to maximize ROC-AUC and F1.<br/>"
        "• <b>Feature Refinement:</b> Evaluate frequency encoding and interaction terms for high-cardinality diagnosis and treatment subcategories.<br/>"
        "• <b>Champion Model Finalization:</b> Lock and persist the best-performing model architecture (<code>best_model.pkl</code>) ready for global SHAP TreeExplainer integration in Sprint 4.<br/>"
        "• <b>Progress Report 3 Preparation:</b> Deliver the machine learning benchmark and tuning analysis on 07 Dec 2026.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # Submission Sign-off Box
    signoff_data = [
        [
            Paragraph("<b>Submitted by:</b><br/>Dennis Sebastian (59593398)<br/>Saran Jayakumaran Nair Sasikala (56500625)", meta_val),
            Paragraph("<b>Academic Supervisor:</b><br/>Dr. Humera Noor<br/>University of Europe for Applied Sciences", meta_val),
            Paragraph("<b>Sprint Status:</b><br/><font color='#16a34a'><b>PASSED &amp; DELIVERED</b></font><br/>All Sprint 2 Deliverables Complete", meta_val)
        ]
    ]
    t_signoff = Table(signoff_data, colWidths=[175, 175, 154])
    t_signoff.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_light),
        ('BOX', (0,0), (-1,-1), 1, c_secondary),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_signoff)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated {pdf_path} successfully.")

if __name__ == '__main__':
    build_pdf()
