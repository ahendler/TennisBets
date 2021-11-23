import pandas as pd
import numpy as np

men_players = pd.read_csv("../../data/interim/men_players.csv")
ranking_per_year = pd.read_csv("../../data/processed/men_ranking_per_year.csv")
ranking_historico = pd.DataFrame(columns=['name','Id','2010','2011','2012','2013','2014','2015','2016',
                                            '2017','2018','2019','2020'])
ranking_historico['Id'] = men_players['player_id']
ranking_historico['name'] = men_players['name']
ranking_historico.fillna(0, inplace=True)
for index, player in ranking_per_year.iterrows():
    id_atual = player['player']
    coluna = int(player['ranking_date']) - 2008
    #indice = ranking_historico.index[ranking_historico.loc[ranking_historico['Id'] == id_atual]].to_list()
    #ranking_historico[coluna][indice[0]] = player['points']
    linha = np.where(ranking_historico['Id'] == id_atual)[0]
    if linha.size > 0:
        #print(coluna)
        #print(linha[0])
        ranking_historico.iloc[linha[0], coluna] = int(player['points'])
ranking_historico.drop(columns=['Id'],inplace=True)
ranking_historico.to_csv('../../data/interim/ranking_historico.csv', index=False, encoding='utf-8')
