# Desafio-simfrete
 ## Como executar o programa:
   Esse script espera dados pela entrada padrão. Para usar os arquivo com exemplos de entrada, localizados na pasta data/, insira no terminal:
 ``` python
   type data/lista_de_ceps.txt | python achar_cep.py
 ```
 ou
  ``` python
   type data/lista_de_caminhos.txt | python main.py
 ```

## Desafios propostos
### Parte 1
Crie um programa que lê de um arquivo uma lista de cidades e as faixas de CEP que as compõe,
e responde a qual cidade um CEP pertence.

O arquivo de entrada é composto por linhas com um nome de cidade, um CEP inicial, e
um CEP final separados por vírgula, então uma linha com dois traços "--" e por fim
um CEP. O seu programa então deve responder o nome da cidade ao qual esse CEP pertence.

### Parte 2
Crie um programa que lê de um arquivo uma lista de nomes de cidades
adjacentes e o custo de transporte entre elas, e calcula o
menor custo entre duas cidades não adjacentes.

O arquivo de entrada é composto por linhas com um nome de cidade, um CEP inicial, e
um CEP final separados por vírgula, então uma linha com dois traços "--".
Seguidos de linhas com dois nomes de cidade e um número representando o custo
de transportar uma mercadoria da primeira cidade até a segunda, então uma linha com
dois traços "--". Finalmente deve receber uma linha com dois CEPs.
O seu program deve então responder com a rota mais barata para transportar
uma mercadoria entre o primeiro e o segundo CEP dá ultima linha da entrada, e
o custo total desta rota.

## Como cheguei à solução:
   Iniciei tentando entender como implementaria esse desafio respeitando o Big O e tentando a melhor opção, a primeira solução que pensei foi uma busca por árvore binária por ter visto na cadeira de Estrutura de Dados e que era relativamente rápida para buscar em maiores quantidades, porém ao pesquisar novamente sobre li que para dados que se sobrepõe, nesse caso um cep dentro de outro mais abrangente (M,60000000,60000500 | N,60000125,60000375) poderia dar problema, portanto fui na mais simples porém para a quantidade considerada de CEPs foi uma boa solução, a busca sequencial.

   Quando estava implementando vi que, por ler em sequência, já que M vinha antes na ordem, ele estava desconsiderando que o N era um resultado melhor por ser mais específico nos intervalos, portanto uma solução foi ordenar os intervalos baseando-se no seu inicio, garantindo que o primeiro que apareceria seria o "melhor", fiz isso utilizando o sort, porém com x1 - x0 para priorizar intervalos menores. Um trade-off de eficiência para retornar um resultado mais específico.


### Segunda parte do desafio
   Para a segunda parte, aproveitar para montar utilizando o que ja havia feito na primeira parte de achar os ceps e baseado nisso fiz as próximas partes, utilizei bibliotecas como subprocess para "simular" uma execução do achar_cep.py na lista de endereços, utilizando o esquema de parser como sendo um script externo. 
   Encapsulei o programa em funções para melhor organização, a função de separar os blocos separa a lista entre cidades, conexões e ceps, após isso constrói intervalos com as cidades, constrói um grafo com as conexões de cada cidade e as atribui origem, destino (nao direcionado) e custo.
   Após isso, finalmente é aplicado o algoritmo de Dijkstra para encontrar o caminho de menor custo utilizando o que já montamos até aqui. Nele é utilizado o grafo, a cidade de origem e destino, utiliza-se também a biblioteca Heap para escolher sempre o caminho de menor custo primeiro.

   A execução fica a cabo do main, que importa as funções do utils_cep, espera o redirecionamento para um arquivo contendo os dados (entrada.txt por ex) e separa-os em blocos. Após isso é criado o mapa de conexões com o grafo, lido os dois ceps informados no final do arquivo de entrada de dados, vincula-os em cidades e executa o Dijkstra, buscando o caminho mais barato entre as duas cidades.

   Fontes:
   https://hub.asimov.academy/tutorial/como-ler-a-partir-do-stdin-em-python/
   https://www.digitalocean.com/community/tutorials/read-stdin-python
   https://blogboard.io/blog/knowledge/python-sorted-lambda/
   https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index?utm_source=chatgpt.com
   https://www.freecodecamp.org/news/lambda-sort-list-in-python/
   https://elemarjr.com/clube-de-estudos/artigos/algoritmo-de-dijkstra-entendendo-o-caminho-minimo-em-grafos-ponderados/
   https://www.freecodecamp.org/portuguese/news/algoritmo-de-caminho-de-custo-minimo-de-dijkstra-uma-introducao-detalhada-e-visual/
   https://docs.python.org/pt-br/3/library/subprocess.html
   https://medium.com/@robertocoliver/subprocess-no-python-937a3c3bd518
