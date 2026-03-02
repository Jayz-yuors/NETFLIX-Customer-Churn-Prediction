import os
import pandas as pd
from db_config_1 import create_connection

PROJECT_ROOT = os.getcwd()
DATA_FOLDER = "Netflix 2025 User Behavior Dataset (210k+ records)"
BASE_PATH = os.path.join(PROJECT_ROOT, DATA_FOLDER)


# ---------------- CLEANING FUNCTIONS ---------------- #

def clean_users(df):
    df = df.copy()
    df = df.drop_duplicates(subset=["user_id"])
    df = df[(df["age"] >= 13) & (df["age"] <= 90)]
    df["monthly_spend"] = df["monthly_spend"].fillna(df["monthly_spend"].median())
    df["household_size"] = df["household_size"].fillna(df["household_size"].median())
    df["gender"] = df["gender"].fillna("Unknown")
    return df


def clean_watch_history(df):
    df = df.copy()
    df = df.drop_duplicates(subset=["session_id"])
    df["watch_duration_minutes"] = df["watch_duration_minutes"].fillna(0)
    df["progress_percentage"] = df["progress_percentage"].fillna(0)
    return df


def clean_movies(df):
    df = df.copy()
    df = df.drop_duplicates(subset=["movie_id"])
    df["genre_secondary"] = df["genre_secondary"].fillna("Unknown")
    return df


def clean_generic(df):
    return df.drop_duplicates().copy()


# ---------------- LOAD + ALIGN ---------------- #

def load_and_clean():

    if not os.path.exists(BASE_PATH):
        raise FileNotFoundError(f"Dataset folder not found:\n{BASE_PATH}")

    users = pd.read_csv(os.path.join(BASE_PATH, "users.csv"))
    movies = pd.read_csv(os.path.join(BASE_PATH, "movies.csv"))
    watch = pd.read_csv(os.path.join(BASE_PATH, "watch_history.csv"))
    recommend = pd.read_csv(os.path.join(BASE_PATH, "recommendation_logs.csv"))
    search = pd.read_csv(os.path.join(BASE_PATH, "search_logs.csv"))
    reviews = pd.read_csv(os.path.join(BASE_PATH, "reviews.csv"))

    # -------- recommendation_logs -------- #

    recommend = recommend.rename(columns={
        "recommendation_date": "recommendation_timestamp",
        "was_clicked": "clicked",
        "position_in_list": "rank_position"
    })

    recommend["watch_after_recommendation"] = None
    recommend["location_country"] = None

    recommend = recommend[[
        "user_id",
        "movie_id",
        "recommendation_timestamp",
        "clicked",
        "watch_after_recommendation",
        "recommendation_type",
        "device_type",
        "rank_position",
        "recommendation_score",
        "location_country"
    ]]

    # -------- search_logs -------- #

    search = search.rename(columns={
        "search_date": "search_timestamp",
        "results_returned": "results_count"
    })

    search["clicked_result"] = search["clicked_result_position"].notna()
    search["search_category"] = None
    search["was_successful"] = search["clicked_result"]

    search = search[[
        "user_id",
        "search_query",
        "search_timestamp",
        "clicked_result",
        "results_count",
        "device_type",
        "search_category",
        "location_country",
        "search_duration_seconds",
        "was_successful"
    ]]

    # -------- reviews -------- #

    reviews = reviews.rename(columns={
        "review_date": "review_timestamp"
    })

    reviews["contains_spoilers"] = False
    reviews["review_length"] = reviews["review_text"].astype(str).apply(len)
    reviews["location_country"] = None

    reviews = reviews[[
        "user_id",
        "movie_id",
        "review_text",
        "sentiment_score",
        "rating",
        "review_timestamp",
        "device_type",
        "contains_spoilers",
        "review_length",
        "location_country",
        "helpful_votes"
    ]]

    # -------- CLEAN -------- #

    users = clean_users(users)
    movies = clean_movies(movies)
    watch = clean_watch_history(watch)
    recommend = clean_generic(recommend)
    search = clean_generic(search)
    reviews = clean_generic(reviews)

    return users, movies, watch, recommend, search, reviews


# ---------------- INSERT ---------------- #

def insert_table(cursor, table_name, df):

    if df.empty:
        print(f"{table_name} skipped.")
        return

    cols = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))

    query = f"""
        INSERT INTO {table_name} ({cols})
        VALUES ({placeholders})
        ON CONFLICT DO NOTHING
    """

    for row in df.itertuples(index=False, name=None):
        cursor.execute(query, row)


# ---------------- MAIN ---------------- #

def push_to_db():

    conn = create_connection()
    cursor = conn.cursor()

    users, movies, watch, recommend, search, reviews = load_and_clean()

    print("\nInserting users1...")
    insert_table(cursor, "users1", users)
    conn.commit()

    print("Inserting movies...")
    insert_table(cursor, "movies", movies)
    conn.commit()

    cursor.execute("SELECT user_id FROM users1")
    valid_users = set(row[0] for row in cursor.fetchall())

    cursor.execute("SELECT movie_id FROM movies")
    valid_movies = set(row[0] for row in cursor.fetchall())

    watch = watch[(watch["user_id"].isin(valid_users)) &
                  (watch["movie_id"].isin(valid_movies))]

    recommend = recommend[(recommend["user_id"].isin(valid_users)) &
                          (recommend["movie_id"].isin(valid_movies))]

    search = search[search["user_id"].isin(valid_users)]

    reviews = reviews[(reviews["user_id"].isin(valid_users)) &
                      (reviews["movie_id"].isin(valid_movies))]

    tables = [
        ("users1", users),
        ("movies", movies),
        ("watch_history", watch),
        ("recommendation_logs", recommend),
        ("search_logs", search),
        ("reviews", reviews)
    ]

    for table_name, df in tables:
        print(f"\nInserting into {table_name}...")
        insert_table(cursor, table_name, df)
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        print(f"{table_name} row count:", cursor.fetchone()[0])

    cursor.close()
    conn.close()

    print("\n✅ Data insertion complete into DemoDb.")


if __name__ == "__main__":
    push_to_db()