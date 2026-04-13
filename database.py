import sqlite3

def save_to_db(df):
    conn = sqlite3.connect("f1_winners.db")
    df.to_sql("vencedores", conn, if_exists="replace", index=False)
    conn.close()
    print ("Data saved.")