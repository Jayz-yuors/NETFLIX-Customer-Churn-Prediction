import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def run_eda_analysis(df):

    os.makedirs("artifacts/eda", exist_ok=True)

    # ===============================
    # 1️⃣ Churn Distribution
    # ===============================
    plt.figure(figsize=(6,5))
    sns.countplot(x="churn_next_month", data=df)
    plt.title("Churn Distribution")
    plt.savefig("artifacts/eda/churn_distribution.png")
    plt.close()

    # ===============================
    # 2️⃣ Watch Hours vs Churn
    # ===============================
    plt.figure(figsize=(6,5))
    sns.boxplot(x="churn_next_month",
                y="monthly_watch_hours",
                data=df)
    plt.title("Monthly Watch Hours vs Churn")
    plt.savefig("artifacts/eda/watch_vs_churn_boxplot.png")
    plt.close()

    # ===============================
    # 3️⃣ Sessions vs Churn
    # ===============================
    plt.figure(figsize=(6,5))
    sns.boxplot(x="churn_next_month",
                y="monthly_sessions",
                data=df)
    plt.title("Monthly Sessions vs Churn")
    plt.savefig("artifacts/eda/sessions_vs_churn_boxplot.png")
    plt.close()

    print("EDA Analysis Saved Successfully.")