#   https://structy.net/problems/undirected-path

def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return has_path(graph , node_A , node_B , set())

def has_path(graph , source , destination , visited):
    if source == destination:
        return True
    
    if source in visited:
        return False
    
    visited.add(source)
    
    for neighbour in graph.get(source , []):
        if has_path(graph , neighbour , destination , visited):
            return True
    
    return False

def build_graph(edges):
    graph = {}
    for node1 , node2 in edges:
        # print(node1 , node2)
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)
            
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)
    
        # graph[node1] = [ node2 ] if node1 not in graph else graph[node1] + [ node2 ]
        # graph[node2] = [ node1 ] if node2 not in graph else graph[node2] + [ node1 ]
        
    return graph


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm'))
print(undirected_path(edges, 'm', 'j'))
print(undirected_path(edges, 'l', 'j'))
print(undirected_path(edges, 'k', 'o'))
print(undirected_path(edges, 'i', 'o'))
print(undirected_path(edges, 'a', 'b'))
print(undirected_path(edges, 'a', 'c'))
print(undirected_path(edges, 'r', 't'))
print(undirected_path(edges, 'r', 'b'))
print(undirected_path(edges, 'r', 't'))