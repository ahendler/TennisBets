import pandas as pd
import numpy as np

matches2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
matches2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
matches2021 = pd.read_csv("../../data/external/mencsv/2021.csv")


win2019 = matches2019['Winner']
los2019 = matches2019['Loser']
win2020 = matches2020['Winner']
los2020 = matches2020['Loser']
win2021 = matches2021['Winner']
los2021 = matches2021['Loser']

players_all = pd.concat([win2019, win2020, win2021, los2019, los2020, los2021], ignore_index=True)
players_all=pd.DataFrame(players_all)

players_all.columns=['PlayerName']

players_all['PlayerName'] = players_all['PlayerName'].str.strip()
players_all.drop_duplicates(inplace=True)
print(players_all.duplicated())
players_all.to_csv('../../data/interim/players_names_non_duplicates.csv', index=False, encoding='utf-8')

