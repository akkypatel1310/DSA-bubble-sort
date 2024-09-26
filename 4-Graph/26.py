def bellman_ford(graph, v, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    for _ in range(v - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return "Negative weight cycle detected"

    return distances

graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('C', 3), ('D', 2), ('E', 2)],
    'C': [],
    'D': [('B', 1), ('C', 5)],
    'E': [('D', -3)]
}

v = 5  

start_node = 'A'

print("Shortest distances from A")

result = bellman_ford(graph, v, start_node)

print(result)
