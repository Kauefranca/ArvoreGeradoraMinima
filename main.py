import random
import heapq
import time
class Grafo:
    def __init__(self, V):
        self.V = V
        self.edges = [] 
        self.adj = [[] for _ in range(V)]  

    
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.edges.append((u, v, w))

    
    def prim_mst(self):
        pq = []  
        src = 0  

        key = [float('inf')] * self.V
        parent = [-1] * self.V
        in_mst = [False] * self.V

        heapq.heappush(pq, (0, src))
        key[src] = 0

        while pq:
            u = heapq.heappop(pq)[1]

            if in_mst[u]:
                continue

            in_mst[u] = True

            for v, weight in self.adj[u]:
                if not in_mst[v] and key[v] > weight:
                    key[v] = weight
                    heapq.heappush(pq, (key[v], v))
                    parent[v] = u

        
        mst_cost = 0
        for i in range(1, self.V):
            mst_cost += key[i]
            

        print(f"Custo Prim: {mst_cost}")

    
    def find_set(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    def union_sets(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    
    def kruskal_mst(self):
        result = []
        parent = []
        rank = []

        self.edges = sorted(self.edges, key=lambda item: item[2])

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        e = 0
        i = 0

        while e < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union_sets(parent, rank, x, y)

        mst_cost = sum([w for _, _, w in result])
        for u, v, weight in result:
            pass
            

        print(f"Custo Kruskal: {mst_cost}")


if __name__ == "__main__":
    # Mais rapido para o Kraskal
    V = 9
    g = Grafo(V)
    edges = [
        (7, 6, 1), (8, 2, 2), (6, 5, 2), (0, 1, 4), (2, 5, 4), (8, 6, 6), (2, 3, 7), (7, 8, 7), (0, 7, 8), (1, 2, 8), (3, 4, 9), (5, 4, 10), (1, 7, 11), (3, 5, 14)        
    ]

    # Mais rapido para o Prim
    # V = 10000
    # edges = []
    # for i in range(V):
    #     for j in range(i + 1, V):
    #         if random.random() < 0.1:  
    #             weight = random.randint(1, 100)
    #             edges.append((i, j, weight))

    g = Grafo(V)

    for u, v, w in edges:
        g.add_edge(u, v, w)

    start_time = time.time()
    g.prim_mst()
    end_time = time.time()
    print(f"Tempo de execução - Prim: {end_time - start_time:.8f} segundos")

    start_time = time.time()
    g.kruskal_mst()
    end_time = time.time()
    print(f"Tempo de execução - Kruskal {end_time - start_time:.8f} segundos")