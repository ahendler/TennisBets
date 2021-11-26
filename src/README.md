## Conteudos:
* extraction: script usado para baixar e salvar páginas web
* aggregation: scripts usados para remoção da informação desejada dos arquivos html e estruturação em csv
* graphs: informações e código para gerar o banco de dados e realizar utilizá-lo para análise da rede.

## Instruções para o banco de dados de grafos:
- As instruções para a criação do banco de dados em Neo4j, assim como análises iniciais, podem ser encontradas [aqui](graphs/criacao_grafoDB_neo4j.md)
- Para as análises utilizando o Cytoscape, é necessário [baixar](https://cytoscape.org/download.html) e instalar o software. Após isso, será necessário instalar as ferramentas STRING e yFiles Layout Algorithms no Cytoscape, e então importar os dados para gerar o grafo. O passo a passo dessa configuração, assim como o setup para análise do grafo no Cytoscape, pode ser encontrado [aqui](graphs/analise_cytoscape.md)
