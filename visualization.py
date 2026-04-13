#%%
import matplotlib.pyplot as plt

#%%
def plot_t10(df):
    plt.bar(df["winner_name"], df["tVitorias"])
    plt.xticks(rotation=45)
    plt.show()