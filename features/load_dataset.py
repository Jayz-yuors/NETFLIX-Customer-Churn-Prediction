import pandas as pd
from database.db_config_1 import create_connection

def load_user_month_dataset():

    conn = create_connection()

    query = """
    SELECT *
    FROM ml_user_month_churn_dataset
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df