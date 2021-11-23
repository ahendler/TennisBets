import pandas as pd

players = pd.read_csv("../../data/processed/men_players.csv")
insta2019 = pd.read_csv("../../data/external/menInstagram2019.csv")
insta2021 = pd.read_csv("../../data/external/menInstagram2021.csv")
insta = pd.DataFrame(columns=["name","followers_2019","followers_2021"])
print(players.columns)
for ind in insta2019.index:
    breaked = False
    initial = insta2019["player"][ind].split(" ")[0][0] #pega a inicial do primeiro nome
    last_name = insta2019["player"][ind].split(" ")[1] #pega o segundo nome
    for ind2 in players.index:
        if(players["name"][ind2].split(" ")[0]==last_name and players["name"][ind2].split(" ")[-1][0] == initial):
            insta = insta.append({"name":players["name"][ind2],"followers_2019":insta2019["followers"][ind],"followers_2021":insta2021["followers"][ind]},ignore_index=True)
            breaked = True
            break
    if(not breaked):
        insta = insta.append({"name":insta2019["player"][ind],"followers_2019":0,"followers_2021":0},ignore_index=True)
        print("nao encontrado ",insta2019["player"][ind])
print(insta)
insta.to_csv("../../data/interim/men_instagram_matched.csv", index = False)