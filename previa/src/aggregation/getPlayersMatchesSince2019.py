import pandas as pd
import numpy as np

matches2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
matches2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
matches2021 = pd.read_csv("../../data/external/mencsv/2021.csv")
players2019 = matches2019[['Winner','Loser']]
players2020 = matches2020[['Winner','Loser']]
players2021 = matches2021[['Winner','Loser']]

players_all = pd.concat([players2019,players2020,players2021], ignore_index=True)
players_all.rename(columns={'Winner':'Player1','Loser':'Player2'}, inplace=True)
players_all.to_csv('../../data/interim/players_since_2019.csv', index=False, encoding='utf-8')

print(players_all)
