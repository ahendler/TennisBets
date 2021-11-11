import pandas as pd
import numpy as np

matches2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
matches2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
matches2021 = pd.read_csv("../../data/external/mencsv/2021.csv")
odds2019 = matches2019['AvgW'].astype(str) + ':' + matches2019['AvgL'].astype(str)
odds2020 = matches2020['AvgW'].astype(str) + ':' + matches2020['AvgL'].astype(str)
odds2021 = matches2021['AvgW'].astype(str) + ':' + matches2021['AvgL'].astype(str)
players2019 = matches2019[['Winner','Loser']]
players2020 = matches2020[['Winner','Loser']]
players2021 = matches2021[['Winner','Loser']]
odds_all = pd.concat([odds2019,odds2020,odds2021], ignore_index=True)
odds_all.columns = ['Odds']
players_all = pd.concat([players2019,players2020,players2021], ignore_index=True)
players_all = pd.concat([players_all,odds_all], ignore_index=True, axis = 1)
players_all.columns=['Winner','Loser', 'Odds']
players_all.to_csv('../../data/interim/players_since_2019.csv', index=False, encoding='utf-8')

print(players_all)
