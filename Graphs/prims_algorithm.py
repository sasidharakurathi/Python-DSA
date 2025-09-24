import heapq
from collections import defaultdict

def prims_heap_matrix(n, adj_matrix):
    '''
        Time Complexity: O(E*log(V))
    '''
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    total_cost = 0

    while min_heap:
        wt, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += wt

        for v in range(n):
            if not visited[v] and adj_matrix[u][v] != 0:
                heapq.heappush(min_heap, (adj_matrix[u][v], v))

    return total_cost

def prims_algorithm_matrix(n,adj_matrix):
    '''
        Time Complexity: O(E*(V^2))
    '''
    visited = [False] * n
    visited[0] = True
    
    ans = 0
    
    for _ in range(n-1):    # n-1 edges
        y = None
        mn = float("inf")
        for i in range(n): # i should be visited
            for j in range(n): # j should not be visited
                if adj_matrix[i][j] != 0 and visited[i] and not visited[j]:
                    if adj_matrix[i][j] < mn:
                        mn = adj_matrix[i][j]
                        y = j
        ans += mn
        visited[y] = True
                    
    return ans

def adj_matrix_to_adj_list(n,adj_matrix):
    
    adj_list = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != 0:
                adj_list[i].append((j,adj_matrix[i][j]))    # appending (dest_node, edge_weight)
    
    # print(adj_list)
    return adj_list

def prims_heap_adj_list(n,adj_list):
    visited = [False] * n
    min_heap = []
    start_node = list(adj_list.keys())[0]
    # print(start_node)
    heapq.heappush(min_heap, (0, start_node))
    total = 0
    
    while len(min_heap) > 0:
        current_weight, current_node = heapq.heappop(min_heap)
        if visited[current_node]:
            continue
        visited[current_node] = True
        
        total += current_weight
        
        for node, weight in adj_list[current_node]:
            if not visited[node]:
                heapq.heappush(min_heap, (weight,node))
    
    return total    

    
if __name__ == "__main__":
    
    n = 5
    # ./img/prims_algorithm.png
    adj_matrix = [
        [0 ,9 ,75,0 ,0 ],
        [9 ,0 ,95,19,42],
        [75,95,0 ,51,66],
        [0 ,19,51,0 ,31],
        [0 ,42,66,31,0 ]
    ]
    
    result = prims_algorithm_matrix(n,adj_matrix)
    print(f"{result = }")
    
    result = prims_heap_matrix(n,adj_matrix)
    print(f"{result = }")
    
    adj_list = adj_matrix_to_adj_list(n,adj_matrix)
    '''
        adj_list = {
            0: [(1, 9), (2, 75)], 
            1: [(0, 9), (2, 95), (3, 19), (4, 42)], 
            2: [(0, 75), (1, 95), (3, 51), (4, 66)], 
            3: [(1, 19), (2, 51), (4, 31)], 
            4: [(1, 42), (2, 66), (3, 31)]
        }
    '''
    
    result = prims_heap_adj_list(n, adj_list)
    print(f"{result = }")
    
    
    