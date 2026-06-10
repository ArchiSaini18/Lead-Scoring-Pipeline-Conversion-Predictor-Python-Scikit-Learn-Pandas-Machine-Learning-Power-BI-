"""Run the full pipeline end-to-end with one command: python run_pipeline.py"""
import os; [os.makedirs(d, exist_ok=True) for d in ("data","models","output")]
from ingest     import fetch_leads
from preprocess import preprocess
from train      import train
from dashboard  import build_dashboard
import pandas as pd

def main():
    print("\n=== STEP 1: Ingesting leads ===")
    raw = fetch_leads()
    raw.to_csv("data/raw_leads.csv", index=False)
    print(f"  {len(raw)} leads fetched")

    print("\n=== STEP 2: Preprocessing ===")
    X, y = preprocess(raw)
    processed = X.copy(); processed["converted"] = y.values
    processed.to_csv("data/processed_leads.csv", index=False)
    print(f"  {X.shape[1]} features ready")

    print("\n=== STEP 3: Training & Scoring ===")
    train()

    print("\n=== STEP 4: Building Dashboard ===")
    build_dashboard()

    print("\n✅ Pipeline complete. Check the output/ folder.")

if __name__ == "__main__":
    main()
