# Projeto TennisBets

# Equipe VGAHDM - VGA
* Artur Abreu Hendler - 231713
* Guilherme Zeferino Rodrigues Dobins - 236129
* João Vitor Baptista Moreira - 237833

## Resumo do Projeto
 O projeto consiste em uma análise de dados referente a apostas esportivas em confrontos de tênis e como fatores intrínsecos a um jogador e a esperança que os apostadores depositam nele podem influenciar no resultado final. Os dados serão coletados a partir de tabelas disponíveis em sites de históricos esportivos. Alguns desses sites não possuem arquivos com os dados prontos. Dessa maneira, pretendemos realizar a obtenção dos dados com um web crawler, de modo que possamos construir nossas próprias tabelas com os dados que nos interessem. A princípio, construiremos 4 modelos relacionais, que contém dados dos jogadores, dos torneios, dos confrontos e dos históricos de jogos.

## Slides da Apresentação
> [Slides](slides/slides.pdf)

## Modelo Conceitual
- Relacional
 ![ER](assets/modelo_conceitual.png)   
##### Nota:  O atributo ranking da componente histórico representa a pontuacao do jogador de 2010 até 2020 como indicado no modelo lógico. Ela foi simplificada aqui para não poluir a imagem.

## Modelos Lógicos

- Relacional:   
~~~
Jogador(_nome_, pais, data_de_nascimento, altura, mao_dominante)
Torneio(_nome_torneio_,_ano_,local, pais, terreno)
Historico(_nome_, seguidores_2019, seguidores_2021, ranking_2010,ranking_2011,...,ranking_2021)
  nome chave estrangeira -> Jogador(nome)
Confronto(_nome_vencedor_, _nome_perdedor_,_data_,odd_vencedor,odd_perdedor,round,nome_torneiro, ano,sets_vencedor,sets_perdedor)  
  nome_vencedor chave estrangeira -> Jogador(nome)
  nome_perdedor chave estrangeira -> Jogador(nome)
  nome_torneio chave estrangeira -> Torneio(nome_torneio)
~~~
- Grafo:   

> Para o modelo de grafos de propriedades, utilize este
> [modelo de base](https://docs.google.com/presentation/d/10RN7bDKUka_Ro2_41WyEE76Wxm4AioiJOrsh6BRY3Kk/edit?usp=sharing) para construir o seu.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image`):
>
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

> Para o modelo de grafos de conhecimento, utilize a abordagem
> (recurso, propriedade, valor) para apresentar seu grafo exemplo.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image).

## Dataset Publicado

título do arquivo/base | link | breve descrição
----- | ----- | -----
Confrontations | [confrontations.csv](data/processed/confrontations.csv) | Corresponde ao componente "confrontos" do modelo conceitual 
History | [history.csv](data/processed/history.csv) | Corresponde ao componente "histórico" do modelo conceitual
Players | [players.csv](data/processed/players.csv) | corresponde ao componente "Jogador" do modelo conceitual
Tournaments | [tournaments.csv](data/processed/confrontations.csv) | corresponde ao componente "Torneio" do modelo conceitual
**???** | [repeated_confrontations.csv](data/processed/confrontations.csv) | **???????**

> Este é o conjunto mínimo de informações que deve constar na disponibilização do Dataset, mas a equipe pode enriquecer esta seção.

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
Men Instagram pages | [Instagram](https://instagram.com) | Arquivos HTML referente as páginas no Instagram dos jogadores (multiple HTMLs).
Women Instagram pages| [Instagram](https://instagram.com)  | Arquivos HTML referente as páginas no Instagram das jogadoras (multiple HTMLs).
Tennis Data UK | [tennis-data.co.uk](http://www.tennis-data.co.uk/) | Registros de jogos de homens e mulheres incluindo o resultado, as *odds*, local e outros dados sobre as partidas. Estão agrupados por ano e sexo (multiple CSVs).
Functional Tennis: Top 100 Instagram Tennis Players| [functionaltennis](https://www.functionaltennis.com/blogs/news/atp-wta-top-100-instagram-rankings) | Link para as páginas do Instagram dos jogadores e jogadoras assim como seu número de seguidores no momento da postagem (fev/2019) (CSV).
JeffSackmann - tennis_atp | [github/tennis_atp](https://github.com/JeffSackmann/tennis_atp) | Dados sobre jogadores como data de nascimento, nacionalidade, mão dominante e altura.
JeffSackmann - tennis_wta | [github/tennis_wta](https://github.com/JeffSackmann/tennis_wta) | Dados sobre jogadoras como data de nascimento, nacionalidade, mão dominante e altura.
World Cities | [kaggle/worldcities](https://www.kaggle.com/viswanathanc/world-cities-datasets) | Dataset contendo dados sobre cidades como o país a qual ela pertence e a sigla de três dígitos ISO desse país.


## Detalhamento do Projeto
> Apresente aqui detalhes do processo de construção do dataset e análise. Nesta seção ou na seção de Perguntas podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.

~~~python
df = pd.read_excel("/content/drive/My Drive/Colab Notebooks/dataset.xlsx");
sns.set(color_codes=True);
sns.distplot(df.Hemoglobin);
plt.show();
~~~

> Se usar Orange para alguma análise, você pode apresentar uma captura do workflow, como o exemplo a seguir e descrevê-lo:
![Workflow no Orange](images/orange-zombie-meals-prediction.png)

> Coloque um link para o arquivo do notebook, programas ou workflows que executam as operações que você apresentar.

> Aqui devem ser apresentadas as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src` (por exemplo, arquivos do Orange ou Cytoscape). Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Evolução do Projeto
> Relatório de evolução, descrevendo as evoluções na modelagem do projeto, dificuldades enfrentadas, mudanças de rumo, melhorias e lições aprendidas. Referências aos diagramas, modelos e recortes de mudanças são bem-vindos.
> Podem ser apresentados destaques na evolução dos modelos conceitual e lógico. O modelo inicial e intermediários (quando relevantes) e explicação de refinamentos, mudanças ou evolução do projeto que fundamentaram as decisões.
> Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada

> As respostas às perguntas podem devem ser ilustradas da forma mais rica possível com tabelas resultantes, grafos ou gráficos que apresentam os resultados. Os resultados podem ser analisados e comentados. Veja um exemplo de figura ilustrando uma comunidade detectada no Cytoscape:

> ![Comunidade no Cytoscape](images/cytoscape-comunidade.png)

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação sucinta da análise que será feita e conjunto de queries que
>     responde à pergunta.

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação em linhas gerais de como a base pode ser usada para responder esta pergunta e a sua relevância.

> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.