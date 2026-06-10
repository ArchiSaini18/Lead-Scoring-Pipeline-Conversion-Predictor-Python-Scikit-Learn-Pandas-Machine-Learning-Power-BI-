"""Phase 3: Train model, evaluate, export scored leads + feature importances."""
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report

def train(processed_csv="data/processed_leads.csv"):
    df = pd.read_csv(processed_csv)
    y  = df.pop("converted")
    X  = df

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_tr, y_tr)

    auc = roc_auc_score(y_te, rf.predict_proba(X_te)[:, 1])
    print(f"ROC-AUC (Random Forest): {auc:.3f}")
    print(classification_report(y_te, rf.predict(X_te)))

    # score ALL leads 0-100 (use only training columns)
    X_scored = X[X_tr.columns]
    df["lead_score"] = (rf.predict_proba(X_scored)[:, 1] * 100).astype(int)
    df["converted"]  = y.values
    df["priority"]   = pd.cut(df["lead_score"], bins=[0,40,70,100],
                              labels=["Low","Medium","High"])
    df.to_csv("output/scored_leads.csv", index=False)

    fi = (pd.Series(rf.feature_importances_, index=X_tr.columns)
            .sort_values(ascending=False).head(10).reset_index())
    fi.columns = ["feature", "importance"]
    fi.to_csv("output/feature_importances.csv", index=False)

    joblib.dump(rf, "models/rf_model.pkl")
    print("Saved → output/scored_leads.csv | output/feature_importances.csv | models/rf_model.pkl")
    return df, fi

if __name__ == "__main__":
    train()
