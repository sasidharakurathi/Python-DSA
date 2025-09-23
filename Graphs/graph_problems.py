from graphs_representation import *

n, e, edges = graph_repr()
adj_list = build_adjacency_list(n, e, edges)


# Detect Cycle In an undirected graph.
def detect_cycle_in_graph(node, parent, adj_list, visited):
    # using depth first search
    visited[node] = True
    
    for x in adj_list[node]:
        if x == parent:
            continue
        
        if visited[x] == True:
            return True

        if detect_cycle_in_graph(x, node, adj_list, visited):
            return True
    
    return False


if __name__ == "__main__":
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, adj_list, visited))              # Output: True
    
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, [[1],[0,2],[1]], visited))       # Output: False
    
    # adj_list = ./no_cycle_graph.png
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, [[1,3],[0,2],[1],[0],[0]], visited))       # Output: False
    