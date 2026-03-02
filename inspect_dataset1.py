import os
import pandas as pd

# ---------------- CONFIG ---------------- #

PROJECT_ROOT = os.getcwd()
DATA_FOLDER = "Netflix 2025 User Behavior Dataset (210k+ records)"
BASE_PATH = os.path.join(PROJECT_ROOT, DATA_FOLDER)

# ---------------- MAIN INSPECTION ---------------- #

def inspect_csv(file_path):
    print("\n" + "=" * 80)
    print(f"FILE: {os.path.basename(file_path)}")
    print("=" * 80)

    try:
        df = pd.read_csv(file_path)

        print("\nColumns:")
        for col in df.columns:
            print(f" - {col}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nShape:")
        print(df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 3 Rows:")
        print(df.head(3))

    except Exception as e:
        print(f"Error reading {file_path}: {e}")


def main():

    if not os.path.exists(BASE_PATH):
        raise FileNotFoundError(
            f"Dataset folder not found:\n{BASE_PATH}"
        )

    print(f"\nScanning folder:\n{BASE_PATH}")

    for file in os.listdir(BASE_PATH):
        if file.endswith(".csv"):
            file_path = os.path.join(BASE_PATH, file)
            inspect_csv(file_path)


if __name__ == "__main__":
    main()