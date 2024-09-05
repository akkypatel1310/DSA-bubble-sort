def dfs(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}
visited  = set()
print("DFS")
dfs(graph,'A',visited)
