
# def has_path(graph , source , destination):
#     """ Using Recursive DFS """
#     if source == destination:
#         return True
    
#     for neighbour in graph[source]:
#         if hasPath(graph , neighbour , destination) == True:
#             return True
    
#     return False

def has_path(graph , source , destination):
    """ Using BFS """
    queue = [ source ]
    while len(queue) > 0:
        current = queue.pop()
        if current == destination:
            return True
        for neighbour in graph[current]:
            queue.insert(0 , neighbour)
    
    return False

graph = {
    'a': ['b' , 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],   
}

print(has_path(graph , 'b' , 'e'))