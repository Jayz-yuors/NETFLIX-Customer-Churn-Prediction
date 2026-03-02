import pandas as pd
from db_config_1 import create_connection


DATASET1_TABLES = [
    "users1",
    "movies",
    "watch_history",
    "recommendation_logs",
    "search_logs",
    "reviews"
]


def inspect_table(conn, table):

    print("\n" + "="*90)
    print(f"TABLE: {table}")
    print("="*90)

    cursor = conn.cursor()

    # Row count
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    row_count = cursor.fetchone()[0]
    print(f"\nRow Count: {row_count}")

    # Column info
    cursor.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{table}'
        ORDER BY ordinal_position;
    """)

    columns = cursor.fetchall()

    print("\nColumns & Data Types:")
    for col, dtype in columns:
        print(f" - {col} ({dtype})")

    # Null counts
    print("\nNull Counts:")
    for col, _ in columns:
        cursor.execute(f"""
            SELECT COUNT(*)
            FROM {table}
            WHERE {col} IS NULL;
        """)
        null_count = cursor.fetchone()[0]
        print(f" - {col}: {null_count}")

    # Distinct user_id
    col_names = [c[0] for c in columns]

    if "user_id" in col_names:
        cursor.execute(f"SELECT COUNT(DISTINCT user_id) FROM {table};")
        print(f"\nDistinct user_id count: {cursor.fetchone()[0]}")

    if "movie_id" in col_names:
        cursor.execute(f"SELECT COUNT(DISTINCT movie_id) FROM {table};")
        print(f"Distinct movie_id count: {cursor.fetchone()[0]}")

    # Date range detection
    date_columns = [c[0] for c in columns if "date" in c[0] or "timestamp" in c[0]]

    for date_col in date_columns:
        cursor.execute(f"""
            SELECT MIN({date_col}), MAX({date_col})
            FROM {table};
        """)
        min_date, max_date = cursor.fetchone()
        print(f"\nDate Range for {date_col}: {min_date} → {max_date}")

    # Sample rows
    print("\nFirst 3 Rows:")
    df_sample = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 3;", conn)
    print(df_sample)

    cursor.close()


def main():
    conn = create_connection()

    print("\n================ DATASET1 DATABASE INSPECTION ================\n")

    for table in DATASET1_TABLES:
        inspect_table(conn, table)

    conn.close()

    print("\n================ INSPECTION COMPLETE ================\n")


if __name__ == "__main__":
    main()