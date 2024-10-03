# Busca em Profundidade 🔗

Este repositório contém uma implementação em Python de um algoritmo de busca em profundidade para encontrar uma ordenação linear em um grafo direcionado acíclico (DAG - Directed Acyclic Graph).

## 📁 Estrutura do Projeto

O código é composto pelo arquivo principal:

- **dfs.py**: Implementação do algoritmo de busca em profundidade, incluindo a lógica de ordenação linear e manipulação de grafos.

## Funcionamento

O programa utiliza a técnica de busca em profundidade para encontrar uma ordenação linear dos vértices do grafo. A ordenação linear é uma ordem na qual, para cada aresta direcionada \(xy\), o vértice \(x\) aparece antes do vértice \(y\). Esse tipo de ordenação é válido apenas para DAGs.

### Detalhes do Algoritmo

1. Inicializa a estrutura do grafo e o estado dos vértices.
2. Realiza a busca em profundidade a partir de cada vértice não visitado.
3. Adiciona o vértice à lista de ordenação após explorar todos os seus vizinhos.
4. Retorna a lista de ordenação linear após a execução completa da busca.

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabigam/busca-em-profundidade.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd busca-em-profundidade
   ```
3. Execute o arquivo Python:
   ```bash
   python dfs.py
   ```

Os resultados das ordenações lineares dos grafos serão impressos no terminal.
```

