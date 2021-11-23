import pandas as pd

dados = pd.read_csv("../../data/interim/men_ranking_per_year.csv")
def get_year(periodo):
    periodo = str(periodo)
    ano = periodo[0:4] 
    return ano
dados['ranking_date'] = dados['ranking_date'].apply(get_year)
dados.to_csv('../../data/processed/men_ranking_per_year.csv', index=False, encoding='utf-8')