#   https://structy.net/problems/shortest-path

def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set([node_A])
    queue = [(node_A , 0)]
    
    while len(queue) > 0:
        current_node , current_path_size = queue.pop()
        
        if current_node == node_B:
            return current_path_size
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.insert(0 , (neighbour , current_path_size + 1))
                visited.add(neighbour)
    
    return -1


        

def build_graph(edges):
    graph = {}
    
    for node1 , node2 in edges:
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
            
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)
    
    return graph

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2
print(shortest_path(edges, 'y', 'x')) # -> 1

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'b', 'g')) # -> -1
