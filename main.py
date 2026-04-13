#%%
from analysis import load_data, t10_winners
from database import save_to_db
from visualization import plot_t10

#%%
def main():
    df = load_data()
    save_to_db(df)

    top10 = t10_winners()

    print(f"The most winning driver in F1 history is: {top10['winner_name'].iloc[0]} with {top10['tVitorias'].iloc[0]} wins")

    plot_t10(top10)

#%%
if __name__ == "__main__":
    main()