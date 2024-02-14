# -Busca-em-Profundidade
README

Busca em Profundidade para Ordenação Linear

Este repositório contém uma implementação em Python de um algoritmo de busca em profundidade para encontrar uma ordenação linear em um grafo direcionado acíclico (DAG - Directed Acyclic Graph).

Funcionamento:

O programa utiliza a técnica de busca em profundidade para encontrar uma ordenação linear dos vértices do grafo. A ordenação linear é uma ordem na qual para cada aresta direcionada xy, o vértice x aparece antes do vértice y. Esse tipo de ordenação é válido apenas para DAGs.

Implementação:

O código é composto por uma classe Grafo, que representa o grafo e contém os métodos necessários para realizar a ordenação linear:

    __init__(self, vertices): Inicializa o grafo com um número especificado de vértices.
    adic_aresta(self, x, y): Adiciona uma aresta direcionada de x para y no grafo.
    ord_lin(self): Executa a busca em profundidade para encontrar a ordenação linear do grafo.

Exemplo de Uso:

O código inclui exemplos de três grafos diferentes, para os quais a ordenação linear é calculada e impressa:

    Grafo com 10 vértices e múltiplas arestas.
    Grafo com 8 vértices e múltiplas arestas.
    Grafo com 6 vértices e múltiplas arestas.

Execução:

Para executar o código, basta rodar o arquivo Python. Os resultados das ordenações lineares dos grafos serão impressos no terminal.

Observações:

    O algoritmo de busca em profundidade é utilizado para encontrar a ordenação linear.
    A ordenação linear é determinada recursivamente para todos os vértices do grafo.
    A ordenação linear só é possível em DAGs.
    A ordenação linear é impressa em ordem reversa devido ao método utilizado na implementação.
