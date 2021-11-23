import pandas as pd

df = pd.read_csv("../../data/processed/confrontations_since_2010.csv")
df.drop(["Tournament", "Data", "AvgW", "AvgL", "Round", "Wsets", "Lsets"],axis=1, inplace=True)
dfcount = df.groupby(df.columns.tolist(),as_index=False).size()
dfcount.to_csv("../../data/processed/repeated_confrontations.csv")