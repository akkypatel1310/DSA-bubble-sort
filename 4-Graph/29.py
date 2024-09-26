class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)
        
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootV] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

def kruskal(graph, vertices):
    edges = sorted(graph, key=lambda edge:edge[2])
    uf = UnionFind(vertices)
    mst = []
    total_cost = 0
    
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst.append((u,v,weight))
            total_cost += weight
    
    return mst, total_cost 

graph = [
    (0,1,4),
    (0,2,3),
    (1,2,1),
    (1,3,2),
    (2,3,4),
    (3,4,2),
    (4,5,6),
]

vertices = 6

mst, cost = kruskal(graph,vertices)
print("Minimum spanning: ",mst)
print("Total Cost Of MST: ",cost)
