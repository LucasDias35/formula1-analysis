# %%
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("data/winners_f1_1950_2025_v2.csv")

# %%
con = sqlite3.connect('f1_winners.db')
df.to_sql('vencedores', con, if_exists='replace', index=False)
con.commit()
con.close()

# %%
con = sqlite3.connect('f1_winners.db')
df_top10 = pd.read_sql_query('SELECT winner_name, count(winner_name) AS tVitorias FROM vencedores GROUP BY winner_name ORDER BY tVitorias DESC LIMIT 10', con)


con.close()

# %%
df_top10.plot(x='winner_name', y='tVitorias', kind='bar')
plt.title("Top 10 Pilotos com mais vitorias")
plt.show()

# %%
print(f"Média de vitórias do top 10: {df_top10['tVitorias'].mean()}")

# %%
df_top10.to_csv('top10_pilotos.csv')

# %%
top1_winner = df_top10.head(1) 


# %%
print(f"O maior vencedor da historia da formula 1 é {top1_winner['winner_name'].values[0]}")