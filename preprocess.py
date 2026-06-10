"""Phase 2: Clean, encode, and remove multicollinear features."""
import pandas as pd
import numpy as np

def preprocess(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    df = df.copy()

    # fill missing
    df["time_on_site_min"] = df["time_on_site_min"].fillna(df["time_on_site_min"].median())
    df["job_title"]        = df["job_title"].fillna("Unknown")

    target = df.pop("converted")

    # drop id (not predictive)
    df.drop(columns=["lead_id"], inplace=True)

    # one-hot encode categoricals
    df = pd.get_dummies(df, columns=["lead_source", "industry", "job_title"], drop_first=True)

    # drop highly correlated numeric features (r > 0.85)
    corr = df.select_dtypes(include=np.number).corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [c for c in upper.columns if any(upper[c] > 0.85)]
    df.drop(columns=to_drop, inplace=True)

    return df, target

if __name__ == "__main__":
    raw = pd.read_csv("data/raw_leads.csv")
    X, y = preprocess(raw)
    X["converted"] = y.values
    X.to_csv("data/processed_leads.csv", index=False)
    print(f"Features after preprocessing: {X.shape[1]-1}  |  rows: {len(X)}")
