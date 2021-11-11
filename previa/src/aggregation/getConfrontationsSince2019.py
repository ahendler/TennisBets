import pandas as pd

data2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
confrontations2019 = pd.DataFrame(data2019[['Location','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
confrontations2020 = pd.DataFrame(data2020[['Location','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2021 = pd.read_csv("../../data/external/mencsv/2021.csv")
confrontations2021 = pd.DataFrame(data2021[['Location','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])

confrontations_all = pd.concat([confrontations2019,confrontations2020,confrontations2021], ignore_index=True)
confrontations_all.to_csv('../../data/interim/confrontations_since_2019.csv', index=False, encoding='utf-8')
print(confrontations_all)