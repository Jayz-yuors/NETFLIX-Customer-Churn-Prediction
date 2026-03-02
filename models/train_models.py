import os
import joblib

from features.load_dataset import load_user_month_dataset
from pipeline.preprocess import preprocess_data

from models.logistic_model import train_logistic
from models.decision_tree_model import train_decision_tree
from models.random_forest_model import train_random_forest
from models.xgboost_model import train_xgboost

from evaluate import compare_models

# 🔥 NEW
from analysis.eda_analysis import run_eda_analysis
from analysis.model_analysis import plot_combined_roc


def main():

    print("Loading dataset...")
    df = load_user_month_dataset()

    print("Preprocessing...")
    X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled = preprocess_data(df)

    results = {}
    trained_models = {}

    # ====================================================
    # 1️⃣ EDA ANALYSIS (Structured Graphical Outputs)
    # ====================================================
    print("Running EDA Analysis...")
    run_eda_analysis(df)

    # ====================================================
    # 2️⃣ Logistic Regression
    # ====================================================
    log_model, f1_log, roc_log = train_logistic(
        X_train_scaled,
        y_train,
        X_test_scaled,
        y_test,
        X_train.columns
    )

    results["Logistic"] = f1_log
    trained_models["Logistic"] = log_model

    # ====================================================
    # 3️⃣ Decision Tree
    # ====================================================
    dt_model, f1_dt = train_decision_tree(
        X_train,
        y_train,
        X_test,
        y_test
    )

    results["Decision Tree"] = f1_dt
    trained_models["Decision Tree"] = dt_model

    # ====================================================
    # 4️⃣ Random Forest
    # ====================================================
    rf_model, f1_rf = train_random_forest(
        X_train,
        y_train,
        X_test,
        y_test
    )

    results["Random Forest"] = f1_rf
    trained_models["Random Forest"] = rf_model

    # ====================================================
    # 5️⃣ XGBoost
    # ====================================================
    xgb_model, f1_xgb, roc_xgb = train_xgboost(
        X_train,
        y_train,
        X_test,
        y_test
    )

    results["XGBoost"] = f1_xgb
    trained_models["XGBoost"] = xgb_model

    # ====================================================
    # 6️⃣ Model Comparison
    # ====================================================
    best_model_name = compare_models(results)

    print("\nTraining complete.")
    print("Best model:", best_model_name)

    # ====================================================
    # 7️⃣ Save Best Model
    # ====================================================
    os.makedirs("artifacts/best_model", exist_ok=True)

    best_model = trained_models[best_model_name]

    joblib.dump(best_model, "artifacts/best_model/churn_model.pkl")

    with open("artifacts/best_model/model_info.txt", "w") as f:
        f.write(f"Best Model: {best_model_name}\n")
        f.write(f"F1 Score: {results[best_model_name]}\n")

    print("Best model saved successfully.")

    # ====================================================
    # 8️⃣ Combined ROC Comparison Plot
    # ====================================================
    print("Generating Combined ROC Comparison...")

    # Logistic needs scaled test
    models_for_roc = {
        "Logistic": (log_model, X_test_scaled),
        "Decision Tree": (dt_model, X_test),
        "Random Forest": (rf_model, X_test),
        "XGBoost": (xgb_model, X_test)
    }

    plot_combined_roc(models_for_roc, y_test)

    print("All structured outputs generated successfully.")


if __name__ == "__main__":
    main()