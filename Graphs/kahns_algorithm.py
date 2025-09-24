from collections import deque

def build_adj_list_and_inorder(n, edges):
    indegree = [0] * n
    adj_list = [[] for _ in range(n)]
    
    for src, dest in edges:
        # src -> dest
        indegree[dest] += 1
        adj_list[src].append(dest)
    
    return adj_list, indegree

def kahns_algorithm(n, edges):
    adj_list, indegree = build_adj_list_and_inorder(n,edges)
    queue = deque()
    topological_order = []
    
    for src in range(n):
        if indegree[src] == 0:
            queue.append(src)
    
    while queue:
        front = queue.popleft()
        topological_order.append(front)
        
        for neighbour in adj_list[front]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    return topological_order
    



if __name__ == "__main__":
    
    # ./img/kahns_algorithm.png
    n = 5
    edges = [
        (0,1),
        (0,3),
        (0,4),
        (4,1),
        (3,2),
        (4,3),
    ]
    
    result = kahns_algorithm(n,edges)
    print(f'{result = }')