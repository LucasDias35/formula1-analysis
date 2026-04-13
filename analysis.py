#%%
import pandas as pd
import sqlite3

#%%
def load_data():
    df = pd.read_csv("data/winners_f1_1950_2025_v2.csv")
    return df

#%%
def t10_winners():
    conn = sqlite3.connect("f1_winners.db")

    query = """
    SELECT winner_name, COUNT(winner_name) as tVitorias
    FROM vencedores
    GROUP BY winner_name
    ORDER BY tVitorias DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    conn.close()
    return df
