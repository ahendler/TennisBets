import pandas as pd

insta = pd.read_csv("../../data/interim/men_instagram_matched.csv")
ranking= pd.read_csv("../../data/interim/ranking_historico.csv")
history =  pd.DataFrame(columns=["name","followers_2019","followers_2021","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])
counter =0
breaked = False
for ind in ranking.index:
    breaked = False
    for ind2 in insta.index:
        if(ranking["name"][ind]==insta["name"][ind2]):
            history = history.append({"name":insta["name"][ind2],"followers_2019":insta["followers_2019"][ind2],
            "followers_2021":insta["followers_2021"][ind2],"2010":ranking["2010"][ind],"2011":ranking["2011"][ind],
            "2012":ranking["2012"][ind],"2013":ranking["2013"][ind],"2014":ranking["2014"][ind],"2015":ranking["2015"][ind],
            "2016":ranking["2016"][ind],"2017":ranking["2017"][ind],"2018":ranking["2018"][ind],"2019":ranking["2019"][ind],
            "2020":ranking["2020"][ind]},ignore_index=True)
            breaked = True
            counter +=1
            break
    if(not breaked):
        history = history.append({"name":ranking["name"][ind],"followers_2019":1000,
        "followers_2021":1001,"2010":ranking["2010"][ind],"2011":ranking["2011"][ind],
        "2012":ranking["2012"][ind],"2013":ranking["2013"][ind],"2014":ranking["2014"][ind],"2015":ranking["2015"][ind],
        "2016":ranking["2016"][ind],"2017":ranking["2017"][ind],"2018":ranking["2018"][ind],"2019":ranking["2019"][ind],
        "2020":ranking["2020"][ind]},ignore_index=True)
print(counter)
history.to_csv("../../data/processed/history.csv", index = False)
print(history)
