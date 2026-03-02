import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from xgboost import XGBClassifier
from sklearn.metrics import (
    f1_score,
    classification_report,
    roc_auc_score,
    confusion_matrix,
    roc_curve
)


def train_xgboost(X_train, y_train, X_test, y_test):

    neg = (y_train == 0).sum()
    pos = (y_train == 1).sum()

    scale_weight = neg / pos

    model = XGBClassifier(
        n_estimators=600,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=scale_weight,
        eval_metric="logloss",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    y_prob = model.predict_proba(X_test)[:, 1]

    best_f1 = 0
    best_threshold = 0.5

    for t in np.arange(0.1, 0.9, 0.05):
        y_pred_temp = (y_prob > t).astype(int)
        score = f1_score(y_test, y_pred_temp)
        if score > best_f1:
            best_f1 = score
            best_threshold = t

    y_pred = (y_prob > best_threshold).astype(int)
    roc = roc_auc_score(y_test, y_prob)

    print("\n=== XGBoost Results ===")
    print("Best Threshold:", best_threshold)
    print("Best F1:", best_f1)
    print("ROC AUC:", roc)
    print(classification_report(y_test, y_pred))

    os.makedirs("artifacts", exist_ok=True)

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Oranges")
    plt.title("XGBoost Confusion Matrix")
    plt.savefig("artifacts/xgboost_confusion_matrix.png")
    plt.close()

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    plt.figure(figsize=(6,5))
    plt.plot(fpr, tpr, label=f"AUC = {roc:.3f}")
    plt.plot([0,1],[0,1],'--')
    plt.title("ROC Curve - XGBoost")
    plt.legend()
    plt.savefig("artifacts/xgboost_roc_curve.png")
    plt.close()

    importance_df = pd.DataFrame({
        "feature": X_train.columns,
        "importance": model.feature_importances_
    }).sort_values(by="importance", ascending=False)

    importance_df.to_csv("artifacts/xgboost_feature_importance.csv", index=False)

    return model, best_f1, roc