import pandas as pd

data = [pd.read_csv("../../data/external/mencsv/"+str(i)+".csv") for i in range(2010,2022)]
tournament = [pd.DataFrame(i[['Location','Surface','Date','Tournament']]) for i in data]

tournaments_all = pd.concat(tournament, ignore_index=True)
tournaments_all.drop_duplicates(inplace=True)
for ind in tournaments_all.index:
    tournaments_all["Date"][ind] = tournaments_all["Date"][ind][-4:]
tournaments_all.drop_duplicates(inplace=True)
tournaments_all = tournaments_all.rename(columns={"Date":"Year"})
tournaments_all.to_csv('../../data/processed/tournaments.csv', index=False, encoding='utf-8')
