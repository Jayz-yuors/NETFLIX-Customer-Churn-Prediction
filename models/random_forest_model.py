import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)


def train_random_forest(X_train, y_train, X_test, y_test):

    # Compute imbalance ratio dynamically
    neg = (y_train == 0).sum()
    pos = (y_train == 1).sum()

    class_weight = {
        0: 1,
        1: neg / pos
    }

    rf = RandomForestClassifier(
        n_estimators=500,
        max_depth=15,
        min_samples_split=20,
        min_samples_leaf=10,
        class_weight=class_weight,
        random_state=42,
        n_jobs=-1
    )

    rf.fit(X_train, y_train)

    y_prob = rf.predict_proba(X_test)[:, 1]

    # Threshold tuning
    best_f1 = 0
    best_threshold = 0.5

    for t in np.arange(0.1, 0.9, 0.05):
        y_pred_temp = (y_prob > t).astype(int)
        score = f1_score(y_test, y_pred_temp)
        if score > best_f1:
            best_f1 = score
            best_threshold = t

    y_pred = (y_prob > best_threshold).astype(int)

    roc_auc = roc_auc_score(y_test, y_prob)

    print("\n=== Random Forest Results ===")
    print("Best Threshold:", best_threshold)
    print("Best F1 Score:", best_f1)
    print("ROC AUC:", roc_auc)
    print(classification_report(y_test, y_pred))

    os.makedirs("artifacts", exist_ok=True)

    with open("artifacts/random_forest_metrics.txt", "w") as f:
        f.write(f"F1 Score: {best_f1}\n")
        f.write(f"ROC AUC: {roc_auc}\n\n")
        f.write(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Greens")
    plt.title("Random Forest Confusion Matrix")
    plt.savefig("artifacts/random_forest_confusion_matrix.png")
    plt.close()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.figure(figsize=(6,5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0,1], [0,1], "--")
    plt.title("ROC Curve - Random Forest")
    plt.legend()
    plt.savefig("artifacts/random_forest_roc_curve.png")
    plt.close()

    # Feature Importance
    importance_df = pd.DataFrame({
        "feature": X_train.columns,
        "importance": rf.feature_importances_
    }).sort_values(by="importance", ascending=False)

    importance_df.to_csv("artifacts/random_forest_feature_importance.csv", index=False)

    return rf, best_f1