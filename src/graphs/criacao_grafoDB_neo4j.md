### Para criar o grafo da rede de jogadores, basta inserir os comandos descritos a seguir, um bloco por vez, no site https://neo4j.com/sandbox-v2/?ref=hcard#

~~~cypher
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/VGAHDM/TennisBets/main/final/data/processed/players.csv' AS line
CREATE (:Player {name: line.name})

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/VGAHDM/TennisBets/main/final/data/processed/graph_relations.csv' AS line
MATCH (win:Player {name:line.Winner})
MATCH (los:Player {name:line.Loser})
CREATE (win)-[:Beat {times: line.size}]->(los)


MATCH (j:Jogador)
RETURN j
~~~
Após isso, os nós e arestas do grafo estarão criados, e é possível passar para as análises.
As análises feitas no Neo4j foram a definição da centralidade e da comunidade de cada nó. Começando pela centralidade, foi utilizado o algoritmo pagerank para realizar tal operação. O
Os comandos a serem inseridos no Neo4j para tal são os seguintes:

~~~cypher
CALL gds.graph.create(
  'grafoCentralidade',
  'Player',
  'Beats'
)


CALL gds.pageRank.stream('grafoCentralidade')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS nome, score AS pagerank
~~~
Com isso, o Neo4j retornará uma tabela contendo os atributos. Você poderá baixar essa tabela como um arquivo csv para usá-la no Cytoscape. A análise das comunidade é realizada de forma semelhante, como visto a seguir:
~~~cypher
CALL gds.graph.create(
  'communityGraph',
  'Player',
  {
    Beats: {
      orientation: 'UNDIRECTED'
    }
  }
)

CALL gds.louvain.stream('communityGraph')
YIELD nodeId, communityId
RETURN gds.util.asNode(nodeId).name AS nome, communityId
~~~
Assim como na análise de centralidade, você poderá baixar a tabela retornada como csv para utilizar as informações no cytoscape.


Observação: Algumas das operações realizadas acima podem ser lentar na versão de navegador do Neo4j, portanto, para criar o banco de dados de grafos no Neo4j desktop, você deverá primeiramente instalar o software, criar um novo banco de dados, instalar o plugin "Graph Data Science Library", e então abrir o navegador do Neo4j desktop, que permite a realização de queries utilizando Cypher. Nessa parte, você deverá inserir os mesmos comandos usados na versão de navegador, no entanto, deverá baixar os arquivos men_players.csv e graph_relations.csv e adicioná-los no diretório do seu banco de dados do Neo4j (em seu computador), e então trocar os caminhos para os arquivos para 'file:///players.csv' e 'file:///graph_relations.csv'.


