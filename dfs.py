# Implementação de Busca em Profundidade para encontrar uma ordenação linear
# O programa imprime a ordenaçao linear de um grafo usando o numero de arestas de entrada
# ordenação linear é feita de forma que para cada aresta direcionada xy, o vértice x vem antes do y
# a ordenação linear só ocorre se o grafo for DAG
# primeiro vértice na ordenação linear sempre é um vértice de grau de entrada 0
# para implementação é usada uma pilha temporária em que primeiro a ordenação linear foi chamada
# recursivamente para todos os seus vértices adjacentes e depois eles foram colocados numa pilha
# só depois o conteúdo da pilha é impresso
# obs: um vertice só é empurado para para pilha quando todos os seus vertices adjacentes já estão na pilha
from collections import defaultdict

# Classe para representar o grafo
class Grafo:
	def __init__(self, vertices):
		self.grafo = defaultdict(list) # dicionário onde está contido a lista de adjacencias
		self.Vert = vertices # numero de vertices

# Funcao para adcionar uma aresta no grafo
	def adic_aresta(self, x, y):
		self.grafo[x].append(y)

# Funcao recursiva usada por ord_line
	def ord_lin(self, n, vert_vis, pilha):

# Marca o vertice atual como visitado
		vert_vis[n] = True

# Recorre a todos os vértices adjacentes a este vértice
		for i in self.grafo[n]:
			if vert_vis[i] == False:
				self.ord_lin(i, vert_vis, pilha)

# Empurra o vértice atual para o empilhamento que armazena o resultado
		pilha.append(n)

# A função que faz a ordenação linear (ord_line) usa recursivamente ord_lin
	def ord_line(self):
# Marca todos os vértices como não visitados
		vert_vis = [False]*self.Vert
		pilha = []

# Chama a função auxiliar recursiva para armazenar linearmente
# Ordena a partir de todos os vértices um por um
		for i in range(self.Vert):
			if vert_vis[i] == False:
				self.ord_lin(i, vert_vis, pilha)

# Imprime o conteúdo da pilha
		print(pilha[::-1]) # retorna a lista na ordem inversa

teste_1 = Grafo(10)
teste_1.adic_aresta(0, 1);
teste_1.adic_aresta(0, 2);
teste_1.adic_aresta(0, 3);
teste_1.adic_aresta(0, 5);
teste_1.adic_aresta(1, 2);
teste_1.adic_aresta(2, 3);
teste_1.adic_aresta(2, 4);
teste_1.adic_aresta(4, 6);
teste_1.adic_aresta(5, 4);
teste_1.adic_aresta(5, 6);
teste_1.adic_aresta(6, 7);
teste_1.adic_aresta(6, 8);
teste_1.adic_aresta(7, 8);
teste_1.adic_aresta(9, 6);

teste_2 = Grafo(8)
teste_2.adic_aresta(0, 3);
teste_2.adic_aresta(0, 4);
teste_2.adic_aresta(1, 3);
teste_2.adic_aresta(2, 4);
teste_2.adic_aresta(2, 7);
teste_2.adic_aresta(3, 5);
teste_2.adic_aresta(3, 6);
teste_2.adic_aresta(3, 7);
teste_2.adic_aresta(4, 6);

teste_3 = Grafo(6)
teste_3.adic_aresta(5, 2);
teste_3.adic_aresta(5, 0);
teste_3.adic_aresta(4, 0);
teste_3.adic_aresta(4, 1);
teste_3.adic_aresta(2, 3);
teste_3.adic_aresta(3, 1);


print("A ordenação linear do grafo 1 é")
teste_1.ord_line() # chama a função
print("A ordenação linear do grafo 2 é")
teste_2.ord_line()
print("A ordenação linear do grafo 3 é")
teste_3.ord_line()


