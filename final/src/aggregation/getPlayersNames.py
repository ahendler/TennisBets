import pandas as pd
import numpy as np

matches = [pd.read_csv("../../data/external/mencsv/"+str(i)+".csv") for i in range(2010,2022)]
wins = [i['Winner'] for i in matches]
loss = [i['Loser'] for i in matches]

players_all = pd.concat(wins + loss, ignore_index=True)
players_all=pd.DataFrame(players_all)

players_all.columns=['PlayerName']

players_all['PlayerName'] = players_all['PlayerName'].str.strip()
players_all.drop_duplicates(inplace=True)
players_all = players_all.sort_values('PlayerName')
#print(players_all.duplicated())
players_all.to_csv('../../data/interim/players_names_non_duplicates.csv', index=False, encoding='utf-8')

