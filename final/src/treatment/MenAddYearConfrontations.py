import pandas as pd

confrontations = pd.read_csv("../../data/processed/confrontations_since_2010.csv")
confrontations["Year"] = 9999
for ind in confrontations.index:
    confrontations["Year"][ind] = confrontations["Data"][ind][-4:]

print(confrontations)
confrontations.to_csv("../../data/processed/confrontations_since_2010.csv", index = False)