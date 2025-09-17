#   https://structy.net/problems/connected-components-count


def connected_components_count(graph):
    count = 0
    visited = set()
    
    for node in graph:
        if explore(graph , node , visited) == True:
            count += 1
    
    return count

def explore(graph , node , visited):
    if str(node) in visited:
        return False
    
    visited.add(str(node))
    
    for neighbour in graph[node]:
        explore(graph , neighbour , visited)
    
    return True
    


# print(connected_components_count({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# })) # -> 2

print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 1
