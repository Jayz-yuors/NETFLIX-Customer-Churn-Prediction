import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    f1_score,
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)


def train_logistic(X_train_scaled, y_train, X_test_scaled, y_test, feature_names):

    model = LogisticRegression(
        class_weight='balanced',
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train_scaled, y_train)

    # ============================
    # Probability Predictions
    # ============================
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    # ============================
    # Automatic Threshold Tuning
    # ============================
    best_f1 = 0
    best_threshold = 0.5

    for t in np.arange(0.1, 0.9, 0.05):
        preds = (y_prob > t).astype(int)
        score = f1_score(y_test, preds)

        if score > best_f1:
            best_f1 = score
            best_threshold = t

    y_pred = (y_prob > best_threshold).astype(int)

    roc_auc = roc_auc_score(y_test, y_prob)

    print("\n=== Logistic Regression Results ===")
    print("Best Threshold:", best_threshold)
    print("Best F1 Score:", best_f1)
    print("ROC AUC:", roc_auc)
    print(classification_report(y_test, y_pred))

    # ============================
    # Save Metrics
    # ============================
    os.makedirs("artifacts", exist_ok=True)

    with open("artifacts/logistic_metrics.txt", "w") as f:
        f.write(f"Best Threshold: {best_threshold}\n")
        f.write(f"F1 Score: {best_f1}\n")
        f.write(f"ROC AUC: {roc_auc}\n\n")
        f.write(classification_report(y_test, y_pred))

    # ============================
    # Confusion Matrix
    # ============================
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Logistic Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("artifacts/logistic_confusion_matrix.png")
    plt.close()

    # ============================
    # ROC Curve
    # ============================
    fpr, tpr, _ = roc_curve(y_test, y_prob)

    plt.figure(figsize=(6,5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0,1], [0,1], linestyle="--")
    plt.title("ROC Curve - Logistic")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()
    plt.savefig("artifacts/logistic_roc_curve.png")
    plt.close()

    # ============================
    # Feature Importance
    # ============================
    importance_df = pd.DataFrame({
        "feature": feature_names,
        "coefficient": model.coef_[0]
    })

    importance_df["abs_coeff"] = importance_df["coefficient"].abs()
    importance_df = importance_df.sort_values(by="abs_coeff", ascending=False)

    importance_df.to_csv("artifacts/logistic_feature_importance.csv", index=False)

    # ============================
    # Model Confidence Output
    # ============================
    sample_confidence = y_prob[:10]
    print("\nSample Churn Confidence Scores (first 10 users):")
    print(sample_confidence)

    # ============================
    # Save Model
    # ============================
    joblib.dump(model, "artifacts/best_model.pkl")

    return model, best_f1, roc_auc