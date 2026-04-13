#%%
from analysis import load_data, t10_winners
from database import save_to_db
from visualization import plot_t10

#%%
def main():
    df = load_data()
    save_to_db(df)

    top10 = t10_winners()

    print(f"O maior vencedor da historia da formula 1 é o piloto {top10['winner_name'].iloc[0]}")

    plot_t10(top10)

#%%
if __name__ == "__main__":
    main()