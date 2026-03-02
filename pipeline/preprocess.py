import os
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(df):

    # Convert date column
    df['snapshot_month'] = pd.to_datetime(df['snapshot_month'])

    # Time-based split
    train_df = df[df['snapshot_month'] < '2025-07-01']
    test_df  = df[df['snapshot_month'] >= '2025-07-01']

    # Separate features and target
    X_train = train_df.drop(columns=['user_id', 'snapshot_month', 'churn_next_month'])
    y_train = train_df['churn_next_month']

    X_test  = test_df.drop(columns=['user_id', 'snapshot_month', 'churn_next_month'])
    y_test  = test_df['churn_next_month']

    # One-hot encoding
    X_train = pd.get_dummies(X_train, drop_first=True)
    X_test  = pd.get_dummies(X_test, drop_first=True)

    # Align test columns with train
    X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

    # Handle missing values
    X_train.fillna(0, inplace=True)
    X_test.fillna(0, inplace=True)

    # Scaling (only needed for Logistic Regression)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    # -------------------------------
    # Save artifacts safely
    # -------------------------------

    # Create folders only if they do not exist
    os.makedirs("artifacts", exist_ok=True)
    os.makedirs("artifacts/scaler", exist_ok=True)
    os.makedirs("artifacts/feature_columns", exist_ok=True)

    # Save scaler and feature column order
    joblib.dump(scaler, "artifacts/scaler/scaler.pkl")
    joblib.dump(X_train.columns.tolist(), "artifacts/feature_columns/columns.pkl")

    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled