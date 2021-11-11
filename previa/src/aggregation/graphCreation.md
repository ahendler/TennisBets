# Para criar o grafo da rede de jogadores, basta inserir os comandos descritos a seguir, um bloco por vez, no site https://neo4j.com/sandbox-v2/?ref=hcard#

~~~cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/VGAHDM/TennisBets/main/previa/data/interim/players_names_non_duplicates.csv' AS line
CREATE (:Player {name: line.PlayerName})

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/VGAHDM/TennisBets/main/previa/data/interim/players_since_2019.csv' AS line
MATCH (win:Player {name:line.Winner})
MATCH (los:Player {name:line.Loser})
CREATE (win)-[:Beat {odds: line.Odds}]->(los)



MATCH (j:Jogador)
RETURN j
~~~