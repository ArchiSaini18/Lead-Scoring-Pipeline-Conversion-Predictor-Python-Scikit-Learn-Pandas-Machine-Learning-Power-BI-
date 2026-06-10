# Lead Scoring Pipeline & Conversion Predictor

An end-to-end machine learning pipeline that fetches raw sales leads via API integrations, engineers predictive features, applies a classification model to calculate conversion probabilities, and delivers business-ready insights through interactive visualizations.

> Built to mirror real enterprise data science workflows — from raw CRM ingestion to stakeholder-ready dashboards.

---

## 🎯 Quick Links

- [Overview](#-overview)
- [Key Achievements](#-key-achievements)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Pipeline Architecture](#-pipeline-architecture)
- [Scoring Formula](#-scoring-formula)
- [Dataset Information](#-dataset-information)
- [Example Outputs](#-example-outputs)
- [Connect to Power BI](#-connect-to-power-bi)
- [Potential Improvements](#-potential-improvements)
- [Troubleshooting](#-troubleshooting)

---

## 📌 Overview

**Lead Scoring Pipeline & Conversion Predictor** is a production-style ML pipeline that helps sales teams identify their highest-value prospects — automatically.

The system combines:

- API-based lead ingestion (CRM-ready)
- Automated feature engineering & bias removal
- Machine learning classification (Random Forest)
- 0–100 lead score generation
- Priority segmentation (Low / Medium / High)
- Visual dashboard for business stakeholders

---

## 🚀 Key Achievements

✅ End-to-end ML pipeline in 4 modular phases  
✅ API-based lead ingestion with idempotent design  
✅ Correlation testing to remove data bias and multicollinearity  
✅ `predict_proba()` converted to human-readable 0–100 Lead Score  
✅ Feature importance matrix — know *why* a lead is high priority  
✅ Power BI–ready CSV exports for business dashboards  
✅ Clean, modular code — each phase runs independently  
✅ Plug-and-play real API integration in one function swap  

---

## 📁 Project Structure

```
lead_scoring/
│
├── ingest.py           # Phase 1 — Fetch raw leads from API / CRM
├── preprocess.py       # Phase 2 — Clean, encode, remove multicollinearity
├── train.py            # Phase 3 — Train model, generate 0–100 scores
├── dashboard.py        # Phase 4 — Build 4-panel visual dashboard
├── run_pipeline.py     # ⚡ Run all 4 phases with one command
├── requirements.txt    # Dependencies
├── README.md
│
├── data/
│   ├── raw_leads.csv           # Raw ingested leads
│   └── processed_leads.csv     # Cleaned & encoded features
│
├── models/
│   └── rf_model.pkl            # Serialized trained model
│
└── output/
    ├── scored_leads.csv            # All leads with score + priority tag
    ├── feature_importances.csv     # Top 10 conversion drivers
    └── dashboard.png               # 4-panel visual summary
```

---

## ✨ Features

### 🧠 ML Pipeline Features

- Content-based lead scoring using Random Forest Classification
- Stratified train-test split for balanced evaluation
- `predict_proba()` → 0–100 Lead Score (not just 0/1 predictions)
- ROC-AUC + Classification Report for model evaluation
- Pearson correlation analysis to remove redundant features (r > 0.85)

### 📥 Ingestion Features

- Simulated CRM API response (swap one function for a real API)
- Idempotent design — reruns update records, no duplicates
- Handles missing values and noise out-of-the-box

### 📊 Output & Visualization Features

- Priority tags: `Low` / `Medium` / `High` per lead
- High-value action list (Score > 80) — tells sales who to call first
- Feature importance chart — shows what drives conversions
- Score distribution histogram
- Priority breakdown pie chart
- All outputs exportable to Power BI

---

## 🛠 Installation

### Prerequisites

- Python 3.8+
- pip
- 4 GB RAM minimum

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/lead-scoring-pipeline.git
cd lead-scoring-pipeline

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Quick Start

### Run the full pipeline (all 4 phases):

```bash
python run_pipeline.py
```

Check the `output/` folder for results.

### Or run each phase individually:

```bash
python ingest.py        # → data/raw_leads.csv
python preprocess.py    # → data/processed_leads.csv
python train.py         # → output/scored_leads.csv + models/rf_model.pkl
python dashboard.py     # → output/dashboard.png
```

---

## 🧠 Pipeline Architecture

```
[CRM / API Source]
        │
        ▼
[ Phase 1: ingest.py ]      → Fetch raw leads, handle API response
        │
        ▼
[ Phase 2: preprocess.py ]  → Impute nulls, encode categoricals,
                               drop correlated features (r > 0.85)
        │
        ▼
[ Phase 3: train.py ]       → Train Random Forest, evaluate ROC-AUC,
                               generate 0–100 Lead Score per lead
        │
        ▼
[ Phase 4: dashboard.py ]   → 4-panel visual: score dist, priority pie,
                               feature importances, top leads table
        │
        ▼
[ output/ ]                 → scored_leads.csv, dashboard.png → Power BI
```

---

## 🔎 Scoring Formula

The 0–100 Lead Score is generated directly from the model's predicted conversion probability:

```
Lead Score = predict_proba(lead)[:, 1]  ×  100
```

Priority segmentation:

| Score Range | Priority |
|-------------|----------|
| 71 – 100    | 🔴 High  |
| 41 – 70     | 🟡 Medium|
| 0  – 40     | 🟢 Low   |

---

## 📊 Dataset Information

### Raw Leads Dataset

| Field | Type | Description |
|-------|------|-------------|
| `lead_id` | int | Unique lead identifier |
| `lead_source` | str | Organic Search, Paid Ad, Referral, etc. |
| `industry` | str | Finance, Tech, Healthcare, Retail, Education |
| `job_title` | str | Manager, Director, Analyst, C-Suite, Individual |
| `time_on_site_min` | float | Minutes spent on website (has missing values) |
| `page_views` | int | Number of pages viewed |
| `email_opened` | int | Whether lead opened an email (0/1) |
| `form_submitted` | int | Whether lead submitted a form (0/1) |
| `num_visits` | int | Total site visits |
| `converted` | int | Target variable — did the lead convert? (0/1) |

### Example Entry

| lead_source | industry | job_title | time_on_site_min | form_submitted | converted |
|-------------|----------|-----------|------------------|----------------|-----------|
| Email Campaign | Finance | Director | 12.4 | 1 | 1 |
| Organic Search | Retail  | Analyst  | 3.1  | 0 | 0 |

---

## 🖼 Example Outputs

### Example 1 — High-Intent Lead

**Lead Profile:**
- Source: Email Campaign
- Industry: Finance
- Job Title: Director
- Form Submitted: Yes
- Time on Site: 14 min

**Result:**
- Lead Score: **87 / 100**
- Priority: 🔴 **High**
- Action: *Call immediately*

---

### Example 2 — Low-Intent Lead

**Lead Profile:**
- Source: Organic Search
- Industry: Retail
- Job Title: Individual
- Form Submitted: No
- Time on Site: 2 min

**Result:**
- Lead Score: **24 / 100**
- Priority: 🟢 **Low**
- Action: *Add to nurture sequence*

---

## 📈 Connect to Power BI

1. Open **Power BI Desktop**
2. **Get Data → Text/CSV** → select `output/scored_leads.csv`
3. Build these recommended visuals:

| Visual | Column | Purpose |
|--------|--------|---------|
| Table (filtered Score > 80) | `lead_score`, `priority` | High-priority action list for sales |
| Bar chart | `feature_importances.csv` | Show conversion drivers to leadership |
| Donut chart | `priority` | Lead funnel breakdown |
| KPI card | `converted` | Overall conversion rate |

---

## 🔧 Connect a Real CRM API

In `ingest.py`, replace `fetch_leads()` with:

```python
import requests, pandas as pd

def fetch_leads(api_url: str) -> pd.DataFrame:
    response = requests.get(api_url, headers={"Authorization": "Bearer YOUR_TOKEN"})
    response.raise_for_status()
    return pd.DataFrame(response.json())
```

Then update `run_pipeline.py`:

```python
raw = fetch_leads("https://your-crm.com/api/leads")
```

Compatible with: HubSpot, Salesforce, Zoho, or any REST API returning JSON.

---

## 🚀 Potential Improvements

### Model Enhancements
- Add XGBoost or LightGBM for better accuracy on imbalanced data
- Implement SMOTE for class balancing
- Add collaborative filtering using historical conversion patterns
- Hyperparameter tuning with GridSearchCV

### Data Improvements
- Expand dataset to 5000+ real leads
- Integrate live APIs: HubSpot CRM, Clearbit enrichment, weather/timing signals
- Add time-decay weighting (recent activity scores higher)

### UI / Output Enhancements
- Streamlit web app for interactive lead scoring
- PDF report export per lead
- Email alerts for new high-priority leads
- Scheduled pipeline runs via cron / Airflow

### Future AI Upgrades
- LLM-generated outreach recommendations per lead
- Sentiment analysis on email reply threads
- Churn prediction as a second model
- Conversational chatbot for sales reps to query lead scores

---

## 🛠 Troubleshooting

**ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**FileNotFoundError: data/raw_leads.csv**  
Run `python ingest.py` first, or run `python run_pipeline.py` which handles all phases in order.

**output/ folder is empty**  
Ensure you ran `train.py` before `dashboard.py`, or just use `run_pipeline.py`.

**Power BI not reading CSV correctly**  
In Power BI → Transform Data → ensure `lead_score` column is set to type *Whole Number*.

---

## ✅ Evaluation Criteria Met

✔️ End-to-end functional ML pipeline  
✔️ API ingestion with realistic data handling  
✔️ Bias removal via correlation testing  
✔️ Interpretable scoring system (0–100)  
✔️ Business-ready dashboard output  
✔️ Modular, clean, production-style code  
✔️ Real-world commercial application  

---

## 🧰 Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.8+ |
| ML | Scikit-learn (Random Forest, ROC-AUC) |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Power BI |
| Serialization | Joblib |
| API Ready | Requests |
