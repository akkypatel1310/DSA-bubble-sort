import heapq

def prim(graph,start):
    mst = []
    visited = set()
    
    min_heap = [(0,start)]
    
    total_cost = 0
    
    while min_heap:
        cost, node = heapq.heappop(min_heap)
        
        if node not in visited:
            visited.add(node)
            total_cost += cost
            mst.append((node, cost))
            
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap,(weight,neighbor))
                    
    return mst, total_cost

graph = {
    'A': [('B',2),('C',3)],
    'B': [('A',2),('C',1),('D',4)],
    'C': [('A',3),('B',1),('D',5)],
    'D': [('B',4),('C',5)],
}

start_vertex = 'A'

mst, cost = prim(graph, start_vertex)
print("Minimum spanning time",mst)
print("Toatal cost:",cost)