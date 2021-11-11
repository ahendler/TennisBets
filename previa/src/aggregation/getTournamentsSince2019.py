import pandas as pd

data2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
tournaments2019 = pd.DataFrame(data2019[['Location','Surface','Date','Tournament']])
data2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
tournaments2020 = pd.DataFrame(data2020[['Location','Surface','Date','Tournament']])
data2021 = pd.read_csv("../../data/external/mencsv/2021.csv")
tournaments2021 = pd.DataFrame(data2021[['Location','Surface','Date','Tournament']])

tournaments_all = pd.concat([tournaments2019,tournaments2020,tournaments2021], ignore_index=True)
tournaments_all.to_csv('../../data/interim/tournaments_since_2019.csv', index=False, encoding='utf-8')
print(tournaments_all)