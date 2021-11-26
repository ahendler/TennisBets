## Utilizando o grafo criado em src/graphCreation.md, foram realizadas queries para analisar o poder da análise de redes em grafos



A primeira query criada foi para verificar qual o jogador, dentre os presentes no grafo, que possui o maior número de vitórias. 

~~~cypher
MATCH (player:Player) -[:Beat]-> (:Player)
WITH player, COUNT(*) AS vitorias ORDER BY vitorias DESC
RETURN player.name, vitorias
~~~
O resultado dessa query foi:
![JogadoresMaisVitoriosos](../assets/JogadoresMaisVitoriosos.png)

É importante notar, no entanto, que esse grafo contempla apenas confrontos ocorridos de 2019 a 2021.

Seguindo o caminho contrário, foram buscados os jogadores com mais derrotas

~~~cypher
MATCH (:Player) -[:Beat]-> (player:Player)
WITH player, COUNT(*) AS derrotas ORDER BY derrotas DESC
RETURN player.name, derrotas
~~~

Os jogadores em questão foram:
![JogadoresQueMaisPerderam](../assets/JogadoresMaisDerrotas.png)

Isso é simplesmente uma demonstração do que pode ser feito com o modelo de grafos, e esperamos conseguir análises mais profundas a partir dessa rede.