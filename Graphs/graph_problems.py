from graphs_representation import *
import heapq
from collections import defaultdict

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

def network_delay_time(times, n, k):
    '''
        You are given a network of "n" nodes, labeled from 1 to "n". 
        You are also given times, a list of travel times as directed edges "times[i] = (ui, vi, wi)", 
        where "ui" is the source node, "vi" is the target node, 
        and "wi" is the time it takes for a signal to travel from source to target.

        We will send a signal from a given node "k". 
        Return the minimum time it takes for all the "n" nodes to receive the signal. 
        If it is impossible for all the "n" nodes to receive the signal, return -1.
        
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
        Image: "./Network_Delay_Time_example_1.png"
        
    '''
    def build_graph(edges):
        # adjacency list using dict
        adj_list = defaultdict(list)
        
        for edge in edges:
            source, dest, time = edge
            adj_list[source].append((dest, time))
        
        return adj_list
    
    adj_list = build_graph(times)
    min_heap = []
    min_times = defaultdict(lambda: float("inf"))
    
    min_times[k] = 0
    heapq.heappush(min_heap, (k, min_times[k]))     # (k,0)
    
    while len(min_heap) > 0:
        current_node, current_time = heapq.heappop(min_heap)
        
        for node, time in adj_list[current_node]:
            if current_time + time < min_times[node]:
                min_times[node] = current_time + time
                heapq.heappush(min_heap, (node, min_times[node]))
    
    if len(min_times) == n:
        return max(min_times.values())

    return -1
            
    


if __name__ == "__main__":
    
    # No Cyclic Graph Test cases
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, adj_list, visited))                          # Output: True
    
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, [[1],[0,2],[1]], visited))                   # Output: False
    
    # adj_list = ./no_cycle_graph.png
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, [[1,3],[0,2],[1],[0],[0]], visited))         # Output: False
    
    # Network Delay Time Test cases
    times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
    print(f"{network_delay_time(times, n, k)}")                                     # Output: 2
    times, n, k = [[1,2,1]], 2, 1
    print(f"{network_delay_time(times, n, k)}")                                     # Output: 1
    times, n, k = [[1,2,1]], 2, 2
    print(f"{network_delay_time(times, n, k)}")                                     # Output: -1
    times, n, k = [[1,2,1],[2,3,2],[1,3,1]], 3, 2
    print(f"{network_delay_time(times, n, k)}")                                     # Output: -1