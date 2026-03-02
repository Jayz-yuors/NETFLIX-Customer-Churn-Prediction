import os
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


def plot_combined_roc(models_dict, y_test):

    os.makedirs("artifacts/model_comparison", exist_ok=True)

    plt.figure(figsize=(8,6))

    for name, (model, X_data) in models_dict.items():

        y_prob = model.predict_proba(X_data)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

        plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.3f})")

    plt.plot([0,1], [0,1], '--')
    plt.title("ROC Curve Comparison")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    plt.savefig("artifacts/model_comparison/combined_roc.png")
    plt.close()

    print("Model Comparison ROC Saved.")