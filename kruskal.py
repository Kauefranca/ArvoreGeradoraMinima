class Grafo:
    def __init__(self, vertices):
        self.v = vertices
        self.grafo = []

    def adicionar_aresta(self, u, v, peso):
        self.grafo.append([u, v, peso])

    def encontrar_conjunto(self, pai, i):
        if pai[i] != i: pai[i] = self.encontrar_conjunto(pai, pai[i])
        return pai[i]

    def unir_conjuntos(self, pai, rank, x, y):
        if rank[x] < rank[y]: pai[x] = y
        elif rank[x] > rank[y]: pai[y] = x
        else:
            pai[y] = x
            rank[x] += 1

    def agm_kruskal(self):
        resultado = []
        pai  = []
        rank = []

        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        for vertice in range(self.v):
            pai.append(vertice)
            rank.append(0)

        e = 0
        i = 0

        while e < self.v - 1:
            u, v, peso = self.grafo[i]
            i += 1
            x = self.encontrar_conjunto(pai, u)
            y = self.encontrar_conjunto(pai, v)

            if x != y:
                e += 1
                resultado.append([u, v, peso])
                self.unir_conjuntos(pai, rank, x, y)

        return resultado

grafo = Grafo(9)
grafo.adicionar_aresta(7, 6, 1)
grafo.adicionar_aresta(8, 2, 2)
grafo.adicionar_aresta(6, 5, 2)
grafo.adicionar_aresta(0, 1, 4)
grafo.adicionar_aresta(2, 5, 4)
grafo.adicionar_aresta(8, 6, 6)
grafo.adicionar_aresta(2, 3, 7)
grafo.adicionar_aresta(7, 8, 7)
grafo.adicionar_aresta(0, 7, 8)
grafo.adicionar_aresta(1, 2, 8)
grafo.adicionar_aresta(3, 4, 9)
grafo.adicionar_aresta(5, 4, 10)
grafo.adicionar_aresta(1, 7, 11)
grafo.adicionar_aresta(3, 5, 14)

resultadoKruskal = grafo.agm_kruskal()
custoKruskal = 0

for u, v, peso in resultadoKruskal:
    custoKruskal += peso 
    print("%d <-> %d = %d" % (u, v, peso))

print(f'Tamanho da árvore geradora mínima (Kruskal): {custoKruskal}')