from graphs_representation import *
import heapq
from collections import defaultdict
from collections import deque

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
        Image: "./img/Network_Delay_Time_example_1.png"
        
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
            
def can_finish(num_courses, prerequisites):
    '''
        There are a total of num_courses courses you have to take, labeled from 0 to num_courses - 1.
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return true if you can finish all courses. Otherwise, return false.
    ''' 
    
    indegree = [0] * num_courses
    adj_list = [[] for _ in range(num_courses)]
    queue = deque()
    topological_order = []
    
    for a, b in prerequisites:
        # b -> a
        indegree[a] += 1
        adj_list[b].append(a)
    
    for src in range(num_courses):
        if indegree[src] == 0:
            queue.append(src)
    
    while queue:
        front = queue.popleft()
        topological_order.append(front)
        
        for neighbour in adj_list[front]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    return len(topological_order) == num_courses

def find_order(num_courses, prerequisites):
    
    '''
        There are a total of num_courses courses you have to take, labeled from 0 to num_courses - 1. 
        You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return the ordering of courses you should take to finish all courses. 
        If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
    '''
    
    indegree = [0] * num_courses
    adj_list = [[] for _ in range(num_courses)]
    queue = deque()
    topological_order = []
    
    for a, b in prerequisites:
        # b -> a
        indegree[a] += 1
        adj_list[b].append(a)
    
    for src in range(num_courses):
        if indegree[src] == 0:
            queue.append(src)
    
    while queue:
        front = queue.popleft()
        topological_order.append(front)
        
        for neighbour in adj_list[front]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    if len(topological_order) == num_courses:
        return topological_order
    
    return []


if __name__ == "__main__":
    
    # No Cyclic Graph Test cases
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, adj_list, visited))                          # Output: True
    
    visited = [False] * n
    print(detect_cycle_in_graph(0, -1, [[1],[0,2],[1]], visited))                   # Output: False
    
    # adj_list = ./img/no_cycle_graph.png
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
    
    # Course Schedule
    num_courses, prerequisites = 2, [[1,0]]
    print(f"{can_finish(num_courses, prerequisites)}")                               # Output: True
    num_courses, prerequisites = 2, [[1,0],[0,1]]
    print(f"{can_finish(num_courses, prerequisites)}")                               # Output: False
    
    num_courses, prerequisites = 2, [[1,0]]
    print(f"{find_order(num_courses, prerequisites)}")                               # Output: [0,1]
    num_courses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
    print(f"{find_order(num_courses, prerequisites)}")                               # Output: [0,2,1,3] or [0,1,2,3]
    num_courses, prerequisites = 1, []
    print(f"{find_order(num_courses, prerequisites)}")                               # Output: [0]