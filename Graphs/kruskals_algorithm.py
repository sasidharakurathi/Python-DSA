
def find(parent, node):
    # Iteratively finding the node's parent. (If a node's parent is itself then we return that node)
    while parent[node] != node:
        node = parent[node]
    return node

def union(parent, node1, node2):
    node1_root = find(parent, node1)
    node2_root = find(parent, node2)
    if node1_root == node2_root:
        return False  # cycle
    parent[node2_root] = node1_root
    return True

def kruskal_algorithm(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = [i for i in range(n)]
    total_cost = 0

    for node1, node2, weight in edges:
        if union(parent, node1, node2):
            total_cost += weight

    return total_cost



if __name__ == "__main__":
    n = 6
    edges = [
        (0,1,4),(0,2,4),
        (1,2,2),
        (2,3,3),(2,4,1),(2,5,6),
        (3,5,2),
        (4,5,3),
    ]
    
    result = kruskal_algorithm(n,edges)
    print(f"{result = }")