import heapq
from collections import defaultdict

def build_graph(n,edges):
    # adjacency list using lists
    adj_list = [[] for _ in range(n)]     # [(node,edge_weight) ...]
    
    for edge in edges:
        node1, node2, weight = edge

        adj_list[node1].append((node2, weight))
        adj_list[node2].append((node1, weight))
    
    return adj_list

def dijkstra_algo(n,adj_list,start):
    # adjacency list using lists
    dist = [ float("inf") ] * n
    
    min_heap = []       # [(node, edge_weight)]
    
    dist[start] = 0
    heapq.heappush(min_heap, (start, dist[start]))  # (0,0)
    
    while len(min_heap) > 0:
        current_node , current_weight = heapq.heappop(min_heap)
        
        for node, weight in adj_list[current_node]:
            if current_weight + weight < dist[node]:
                dist[node] = current_weight + weight
                heapq.heappush(min_heap, (node,dist[node]))
    
    # print(f"{dist=}")
    return dist


def build_graph2(n,edges):
    # adjacency list using dict
    adj_list = defaultdict(list)
    
    for edge in edges:
        node1, node2, weight = edge
        adj_list[node1].append((node2, weight))
        adj_list[node2].append((node1, weight))
    
    return dict(adj_list)

def dijkstra_algo2(n,adj_list,start):
    # adjacency list using dict
    
    dist = defaultdict(lambda: float("inf"))
    min_heap = []
    dist[start] = 0
    heapq.heappush(min_heap, (start, dist[start]))
    
    while len(min_heap) > 0:
        current_node, current_weight = heapq.heappop(min_heap)
        
        for node, weight in adj_list[current_node]:
            if current_weight + weight < dist[node]:
                dist[node] = current_weight + weight
                heapq.heappush(min_heap, (node, dist[node]))
    
    # print(f"{dist.values()=}")
    return list(dist.values())


if __name__ == "__main__":
    # n , e = 6 , 8
    # # edge = (node1,node2,edge_weight)
    # edges = [
    #     (0,1,4),(0,2,4),
    #     (1,2,2),
    #     (2,3,3),(2,4,1),(2,5,6),
    #     (3,5,2),
    #     (4,5,3),
    # ]
    
    # adj_list = build_graph(n,edges)  # [(node,weight) ...]
    # '''
    #     adj_list = [
    #         [(1, 4), (2, 4)], 
    #         [(0, 4), (2, 2)], 
    #         [(0, 4), (1, 2), (3, 3), (4, 1), (5, 6)], 
    #         [(2, 3), (5, 2)], 
    #         [(2, 1), (5, 3)], 
    #         [(2, 6), (3, 2), (4, 3)]
    #     ]
    # '''
    
    # # print(f"{adj_list=}")
    # dist = dijkstra_algo(n,adj_list,0)
    # print(f"{dist = }")
    
    
    n , e = 6 , 8
    # edge = (node1,node2,edge_weight)
    edges = [
        ('a','b',4),('a','c',4),
        ('b','c',2),
        ('c','d',3),('c','e',1),('c','f',6),
        ('d','f',2),
        ('e','f',3),
    ]
    
    adj_list = build_graph2(n,edges)  # [(node,weight) ...]
    '''
        adj_list = {
            'a': [('b', 4), ('c', 4)], 
            'b': [('a', 4), ('c', 2)], 
            'c': [('a', 4), ('b', 2), ('d', 3), ('e', 1), ('f', 6)], 
            'd': [('c', 3), ('f', 2)], 
            'e': [('c', 1), ('f', 3)], 
            'f': [('c', 6), ('d', 2), ('e', 3)]
        }
    '''
    # print(f"{adj_list=}")
    
    dist = dijkstra_algo2(n,adj_list,'a')
    print(f"{dist = }")
    
    
    