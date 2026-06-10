# Lead Scoring Pipeline & Conversion Predictor

An end-to-end ML pipeline that ingests raw CRM leads, engineers features, trains a Random Forest classifier, generates 0–100 lead scores, and outputs an actionable dashboard.

---

## Project Structure

```
lead_scoring/
│
├── ingest.py          # Phase 1 — Simulate / fetch leads from an API
├── preprocess.py      # Phase 2 — Clean, encode, remove multicollinearity
├── train.py           # Phase 3 — Train model, score leads, export results
├── dashboard.py       # Phase 4 — Generate 4-panel visualization
├── run_pipeline.py    # ⚡ Run all 4 phases in one command
├── requirements.txt
│
├── data/
│   ├── raw_leads.csv        # Ingested leads (auto-generated)
│   └── processed_leads.csv  # Cleaned & encoded features
│
├── models/
│   └── rf_model.pkl         # Saved Random Forest model
│
└── output/
    ├── scored_leads.csv         # Leads with 0–100 score + priority
    ├── feature_importances.csv  # Top 10 conversion drivers
    └── dashboard.png            # 4-panel visual summary
```

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the full pipeline

```bash
python run_pipeline.py
```

That's it. All 4 phases execute in sequence. Outputs appear in `output/`.

---

### Run individual phases

```bash
python ingest.py        # Generates data/raw_leads.csv
python preprocess.py    # Generates data/processed_leads.csv
python train.py         # Trains model, saves output/scored_leads.csv
python dashboard.py     # Saves output/dashboard.png
```

---

## Pipeline Overview

| Phase | File | What it does |
|-------|------|-------------|
| 1 – Ingest | `ingest.py` | Simulates a CRM API, returns 500 raw leads with realistic noise & missing values |
| 2 – Preprocess | `preprocess.py` | Median imputation, one-hot encoding, drops correlated features (r > 0.85) |
| 3 – Train & Score | `train.py` | Trains a Random Forest, evaluates with ROC-AUC, scores all leads 0–100 |
| 4 – Dashboard | `dashboard.py` | Generates 4-panel PNG: score distribution, priority pie, feature importances, top leads table |

---

## Output Files

| File | Description |
|------|-------------|
| `output/scored_leads.csv` | All leads with `lead_score` (0–100) and `priority` (Low / Medium / High) |
| `output/feature_importances.csv` | Top 10 features driving conversion predictions |
| `output/dashboard.png` | Ready-to-share visual summary |
| `models/rf_model.pkl` | Serialized model for inference on new leads |

---

## Connect to Power BI

1. Open Power BI Desktop
2. **Get Data → Text/CSV** → select `output/scored_leads.csv`
3. Build visuals:
   - **Table** filtered to `lead_score > 80` → High-priority action list
   - **Bar chart** from `feature_importances.csv` → Conversion drivers
   - **Donut chart** on `priority` column → Lead breakdown

---

## Replacing Simulated Data with a Real API

In `ingest.py`, replace the `fetch_leads()` body with:

```python
import requests, pandas as pd

def fetch_leads(api_url: str) -> pd.DataFrame:
    response = requests.get(api_url, headers={"Authorization": "Bearer YOUR_TOKEN"})
    response.raise_for_status()
    return pd.DataFrame(response.json())
```

Then call `fetch_leads("https://your-crm.com/api/leads")` in `run_pipeline.py`.

---

## Tech Stack

- **Python** — pandas, numpy, scikit-learn, matplotlib, joblib
- **Model** — Random Forest Classifier (`predict_proba` → 0–100 score)
- **Visualization** — Matplotlib (PNG) + Power BI (CSV-connected dashboard)
