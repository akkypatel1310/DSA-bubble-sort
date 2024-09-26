def floyd_marshall(graph):
    V = len(graph)
    
    dist = [[float('inf')]* V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    for i in range(V):
        dist[i][i] = 0
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],dist[i][j]+dist[i][j])
    return dist

graph = [
    [0,3,float('inf'),5],
    [2,0,float('inf'),4],
    [float('inf'),1,0,float('inf')],
    [float('inf'),float('inf'),2,0]
]

print("all Pairs shortest path")
distaces = floyd_marshall(graph)
for row in distaces:
    print(row)