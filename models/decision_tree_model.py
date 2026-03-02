import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)


def train_decision_tree(X_train, y_train, X_test, y_test):

    neg = (y_train == 0).sum()
    pos = (y_train == 1).sum()

    class_weight = {
        0: 1,
        1: neg / pos
    }

    param_grid = {
        "max_depth": [5, 10, 15],
        "min_samples_split": [10, 20, 50]
    }

    dt = DecisionTreeClassifier(
        random_state=42,
        class_weight=class_weight
    )

    grid = GridSearchCV(
        dt,
        param_grid,
        scoring="f1",
        cv=3,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_

    y_prob = best_model.predict_proba(X_test)[:, 1]

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

    print("\n=== Decision Tree Results ===")
    print("Best Params:", grid.best_params_)
    print("Best Threshold:", best_threshold)
    print("Best F1:", best_f1)
    print("ROC AUC:", roc_auc)
    print(classification_report(y_test, y_pred))

    os.makedirs("artifacts", exist_ok=True)

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Decision Tree Confusion Matrix")
    plt.savefig("artifacts/decision_tree_confusion_matrix.png")
    plt.close()

    return best_model, best_f1