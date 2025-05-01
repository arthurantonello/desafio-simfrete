# desafio-simfrete
 
 ## Como cheguei à solução:
    Iniciei tentando entender como implementaria esse desafio respeitando o Big O e tentando a melhor opção, a primeira solução que pensei foi uma busca por árvore binária por ter visto na cadeira de Estrutura de Dados e que era relativamente rápida para buscar em maiores quantidades, porém ao pesquisar novamente sobre li que para dados que se sobrepõe, nesse caso um cep dentro de outro mais abrangente (M,60000000,60000500 | N,60000125,60000375) poderia dar problema, portanto fui na mais simples porém para a quantidade considerada de CEPs foi uma boa solução, a busca sequencial.

    Quando estava implementando vi que, por ler em sequência, já que M vinha antes na ordem, ele estava desconsiderando que o N era um resultado melhor por ser mais específico nos intervalos, portanto uma solução foi ordenar os intervalos baseando-se no seu inicio, garantindo que o primeiro que apareceria seria o "melhor", fiz isso utilizando o sort, porém com x1 - x0 para priorizar intervalos menores. Um trade-off de eficiência para retornar um resultado mais específico.

    Fontes:
    https://hub.asimov.academy/tutorial/como-ler-a-partir-do-stdin-em-python/
    https://www.digitalocean.com/community/tutorials/read-stdin-python
    https://blogboard.io/blog/knowledge/python-sorted-lambda/
    https://www.freecodecamp.org/news/lambda-sort-list-in-python/
