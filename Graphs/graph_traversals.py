from graphs_representation import *
from collections import deque

# graph = ./img/graph_repr.png
n, e, edges = graph_repr()
adj_list = build_adjacency_list(n, e, edges)

def breadth_first_search(adj_list):
    queue = deque()
    visited = [False] * len(adj_list)
    ans = []
    # print(visited)                    # [False, False, False, False, False, False]
    
    queue.append(0)
    visited[0] = True
    
    while queue:
        front = queue.popleft()
        ans.append(front)
        for node in adj_list[front]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
    
    return ans
    
    

def depth_first_search_using_stack(adj_list):
    stack = list()
    visited = [False] * len(adj_list)
    ans = list()
    
    stack.append(0)
    visited[0] = True
    
    while stack:
        top = stack.pop()
        ans.append(top)
        for node in adj_list[top]:
            if visited[node] == False:
                stack.append(node)
                visited[node] = True
    
    return ans

def depth_first_search(node, adj_list, visited, ans):
    visited[node] = True
    ans.append(node)
    for x in adj_list[node]:
        if visited[x] == False:
            depth_first_search(x, adj_list, visited, ans)
    
    
    


if __name__ == "__main__":
    print(breadth_first_search(adj_list))                               # Output: [0, 1, 3, 4, 2, 5]
    print(depth_first_search_using_stack(adj_list))                     # Output: [0, 4, 2, 3, 1, 5]
    
    visited = [False] * n
    ans = []
    depth_first_search(0,adj_list,visited, ans)
    print(ans)                                                          # Output: [0, 1, 2, 4, 3, 5]
    
    