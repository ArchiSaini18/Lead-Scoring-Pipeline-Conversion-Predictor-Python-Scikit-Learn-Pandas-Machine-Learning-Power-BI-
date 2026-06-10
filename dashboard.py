"""Phase 4: Generate a 4-panel dashboard saved as PNG (Power BI-ready CSV also exported)."""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def build_dashboard():
    scores = pd.read_csv("output/scored_leads.csv")
    fi     = pd.read_csv("output/feature_importances.csv")

    fig = plt.figure(figsize=(14, 9), facecolor="#f7f8fa")
    fig.suptitle("Lead Scoring Pipeline — Conversion Dashboard", fontsize=15, fontweight="bold", y=0.98)
    gs  = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)

    # 1. Score distribution
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.hist(scores["lead_score"], bins=20, color="#4A90D9", edgecolor="white")
    ax1.set_title("Lead Score Distribution", fontweight="bold")
    ax1.set_xlabel("Score (0–100)"); ax1.set_ylabel("Count")

    # 2. Priority breakdown (pie)
    ax2 = fig.add_subplot(gs[0, 1])
    counts = scores["priority"].value_counts()
    ax2.pie(counts, labels=counts.index, autopct="%1.0f%%",
            colors=["#E74C3C","#F39C12","#27AE60"], startangle=140)
    ax2.set_title("Priority Breakdown", fontweight="bold")

    # 3. Feature importances
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.barh(fi["feature"][::-1], fi["importance"][::-1], color="#6C5CE7")
    ax3.set_title("Top 10 Conversion Drivers", fontweight="bold")
    ax3.set_xlabel("Importance")

    # 4. High-value leads table (score > 80)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")
    hot = scores[scores["lead_score"] > 80][["lead_score","priority","converted"]].head(8)
    hot.insert(0, "Rank", range(1, len(hot)+1))
    tbl = ax4.table(cellText=hot.values, colLabels=hot.columns,
                    cellLoc="center", loc="center")
    tbl.auto_set_font_size(False); tbl.set_fontsize(9)
    tbl.scale(1, 1.4)
    ax4.set_title("Top Leads (Score > 80)", fontweight="bold")

    plt.savefig("output/dashboard.png", dpi=150, bbox_inches="tight")
    print("Dashboard saved → output/dashboard.png")

if __name__ == "__main__":
    build_dashboard()
