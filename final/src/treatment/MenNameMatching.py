from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

men_players = pd.read_csv("../../data/raw/men_players.csv")
names = pd.read_csv("../../data/interim/players_names_non_duplicates.csv")
men_players_fix = open("../../data/processed/men_players.csv","w", newline='\n', encoding= 'utf-8')
men_players_fix.write("name,hand,date_of_birth,country,height\n")
meanheight = men_players["height"].mean()
height = meanheight
meandob = 19900101
for ind in names.index:
    breaked = 0
    seginicial = ''
    segsobrenome = ''
    nome = names["PlayerName"][ind].replace("-"," ").split(" ")
    inicial = nome[-1]
    if(len(inicial)==2):
        inicial = inicial[0]
    elif(len(inicial)>2):     #se o nome for composto 
        seginicial = inicial[2]
        inicial = inicial[0]
    else:
        print("inicial irregular: ", nome, ind)
        continue
    sobrenome = nome[0]
    if(len(nome)>2):
        segsobrenome = nome[1]
    
    for ind2 in men_players.index:
        seginicial2 = ''
        segsobrenome2 = ''
        primeiro = str(men_players["name_first"][ind2]).split(" ")
        inicial2 = primeiro[0][0]
        if(len(primeiro)>1 and len(primeiro[1])>1):
            seginicial2 = primeiro[1][0]
        sobrenome2 = str(men_players["name_last"][ind2]).split(" ")
        if(len(sobrenome2)>1):
            segsobrenome2 = sobrenome2[1]
            sobrenome2 = sobrenome2[0]
        else:
            sobrenome2 = sobrenome2[0]

        #if(sobrenome == sobrenome2 and segsobrenome == segsobrenome2 and inicial == inicial2 and seginicial == seginicial2):
        if((sobrenome == sobrenome2 or segsobrenome2 ==sobrenome) and inicial == inicial2):
            if(men_players["height"][ind2]>13):
                height = men_players["height"][ind2]
            men_players_fix.write(names["PlayerName"][ind]+","+men_players["hand"][ind2]+","+str(men_players["dob"][ind2])+","+men_players["ioc"][ind2]+","+str(int(height))+"\n")
            breaked = 1
            height = meanheight
            break
    if(breaked == 0):
        print("nao encontrado",nome, ind)
