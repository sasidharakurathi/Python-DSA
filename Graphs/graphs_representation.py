

def graph_repr():
    # graph = ./img/graph_repr.png
    
    n = 6   # number of nodes
    e = 7   # number of edges
    
    edges = [
        (0,1),
        (0,3),
        (0,4),
        (1,2),
        (1,5),
        (2,4),
        (3,4)
    ]
    
    return n, e, edges
    
def build_adjacency_list(n,e,edges):
    # lists all the adjacent nodes of a node.
    
    adj_list = [[] for i in range(n)]
    
    for edge in edges:
        x, y = edge[0], edge[1]
        adj_list[x].append(y)
        adj_list[y].append(x)

    # print(adj_list)                             #[[1, 3, 4], [0, 2, 5], [1, 4], [0, 4], [0, 2, 3], [1]]
    # for idx,ele in enumerate(adj_list):
    #     print(idx, " -> " , ele)
    
    return adj_list

def build_adjacency_matrix(n,e,edges):
    adj_matrix = [[-1 for i in range(n)] for i in range(n)]
    # [        0   1   2   3   4   5
    #     0  [-1, -1, -1, -1, -1, -1], 
    #     1  [-1, -1, -1, -1, -1, -1], 
    #     2  [-1, -1, -1, -1, -1, -1], 
    #     3  [-1, -1, -1, -1, -1, -1], 
    #     4  [-1, -1, -1, -1, -1, -1], 
    #     5  [-1, -1, -1, -1, -1, -1]
    # ]
    
    
    # print(adj_matrix)
    
    for edge in edges:
        x = edge[0]
        y = edge[1]
        
        adj_matrix[x][y] = 1
        adj_matrix[y][x] = 1
        
    # print(adj_matrix)
    # [        0   1   2   3   4   5
    #     0  [-1,  1, -1,  1,  1, -1], 
    #     1  [ 1, -1,  1, -1, -1,  1], 
    #     2  [-1,  1, -1, -1,  1, -1], 
    #     3  [ 1, -1, -1, -1,  1, -1], 
    #     4  [ 1, -1,  1,  1, -1, -1], 
    #     5  [-1,  1, -1, -1, -1, -1]
    # ]
    
    
    return adj_matrix


    


if __name__ == "__main__":
    # build_adjacency_list(6,7,graph_repr())
    build_adjacency_matrix(6,7,graph_repr())

