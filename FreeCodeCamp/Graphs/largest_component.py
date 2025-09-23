#   https://structy.net/problems/largest-component

def largest_component(graph):
    visited = set()
    largest = 0
  
    for node in graph:
        size = explore(graph , node ,visited)
        largest = size if size > largest else largest
        
    return largest

def explore(graph , source , visited):
    if str(source) in visited:
        return 0
    
    visited.add(str(source))
    
    size = 1
    
    for neighbour in graph[source]:
        size += explore(graph , neighbour , visited)
    
    
    return size



print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4