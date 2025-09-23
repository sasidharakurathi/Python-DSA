
# def depth_first_print(graph , source):
#     """DFS using Loops"""
#     stack = [source]
    
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current , end=" -> ")
        
#         for neighbour in graph[current]:
#             stack.append(neighbour)


def depth_first_print(graph , source):
    """DFS using Recursion"""
    print(source , end=" -> ")
    for neighbour in graph[source]:
        depth_first_print(graph , neighbour)        
        

graph = {
    'a': ['b' , 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],   
}

depth_first_print(graph , 'a')
