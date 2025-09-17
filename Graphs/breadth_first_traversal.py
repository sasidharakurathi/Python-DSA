
def breadth_first_print(graph , source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        print(current , end=" -> ")
        for neighbour in graph[current]:
            queue.insert(0 , neighbour)


graph = {
    'a': ['b' , 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],   
}

breadth_first_print(graph , 'a')
