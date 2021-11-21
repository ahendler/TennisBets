import pandas as pd

data2019 = pd.read_csv("../../data/external/mencsv/2019.csv")
confrontations2019 = pd.DataFrame(data2019[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2020 = pd.read_csv("../../data/external/mencsv/2020.csv")
confrontations2020 = pd.DataFrame(data2020[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2021 = pd.read_csv("../../data/external/mencsv/2021.csv")
confrontations2021 = pd.DataFrame(data2021[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2018 = pd.read_csv("../../data/external/mencsv/2018.csv")
confrontations2018 = pd.DataFrame(data2018[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2017 = pd.read_csv("../../data/external/mencsv/2017.csv")
confrontations2017 = pd.DataFrame(data2017[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2016 = pd.read_csv("../../data/external/mencsv/2016.csv")
confrontations2016 = pd.DataFrame(data2016[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2015 = pd.read_csv("../../data/external/mencsv/2015.csv")
confrontations2015 = pd.DataFrame(data2015[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2014 = pd.read_csv("../../data/external/mencsv/2014.csv")
confrontations2014 = pd.DataFrame(data2014[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2013 = pd.read_csv("../../data/external/mencsv/2013.csv")
confrontations2013 = pd.DataFrame(data2013[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2012 = pd.read_csv("../../data/external/mencsv/2012.csv")
confrontations2012 = pd.DataFrame(data2012[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2011 = pd.read_csv("../../data/external/mencsv/2011.csv")
confrontations2011 = pd.DataFrame(data2011[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])
data2010 = pd.read_csv("../../data/external/mencsv/2010.csv")
confrontations2010 = pd.DataFrame(data2010[['Tournament','Date','Winner','Loser','AvgW','AvgL','Round','Wsets','Lsets']])


confrontations_all = pd.concat([confrontations2019,confrontations2020,confrontations2021,
            confrontations2018,confrontations2017,confrontations2016,
            confrontations2015,confrontations2014,confrontations2013,
            confrontations2012,confrontations2011,confrontations2010], ignore_index=True)
confrontations_all.to_csv('../../data/processed/confrontations_since_2010.csv', index=False, encoding='utf-8')
print(confrontations_all)