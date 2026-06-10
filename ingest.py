"""Phase 1: Fetch / generate raw leads data."""
import pandas as pd
import numpy as np

def fetch_leads(n=500, seed=42) -> pd.DataFrame:
    """Simulate a CRM API response with realistic lead data."""
    rng = np.random.default_rng(seed)
    sources   = ["Organic Search", "Paid Ad", "Referral", "Email Campaign", "Social Media"]
    industry  = ["Finance", "Tech", "Healthcare", "Retail", "Education"]
    jobs      = ["Manager", "Director", "Analyst", "C-Suite", "Individual"]

    df = pd.DataFrame({
        "lead_id":           range(1, n + 1),
        "lead_source":       rng.choice(sources,   n),
        "industry":          rng.choice(industry,  n),
        "job_title":         rng.choice(jobs,      n),
        "time_on_site_min":  rng.normal(8, 4, n).clip(0),
        "page_views":        rng.integers(1, 30, n),
        "email_opened":      rng.integers(0, 2,  n),
        "form_submitted":    rng.integers(0, 2,  n),
        "num_visits":        rng.integers(1, 10, n),
        "converted":         rng.integers(0, 2,  n),   # target
    })
    # inject some missing values for realism
    df.loc[rng.choice(n, 40, replace=False), "time_on_site_min"] = np.nan
    df.loc[rng.choice(n, 30, replace=False), "job_title"]        = np.nan
    return df

if __name__ == "__main__":
    df = fetch_leads()
    df.to_csv("data/raw_leads.csv", index=False)
    print(f"Saved {len(df)} leads → data/raw_leads.csv")
