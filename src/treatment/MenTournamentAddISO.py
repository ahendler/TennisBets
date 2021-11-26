import pandas as pd

tournaments = pd.read_csv("../../data/processed/tournaments.csv")
cities = pd.read_csv("../../data/raw/worldcities.csv")

tournaments["country"] = "UUU"

for ind in tournaments.index:
    breaked = False
    for ind2 in cities.index:
        if(cities["city"][ind2]==tournaments["Location"][ind]):
            tournaments["country"][ind]=cities["iso3"][ind2]
            break

tournaments.to_csv("../../data/processed/tournaments.csv", index = False)

