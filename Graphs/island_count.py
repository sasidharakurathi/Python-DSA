#   https://structy.net/problems/island-count

def island_count(grid):
    visited = set()
    count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid , row , col , visited) == True:
                count += 1
    
    return count
    

def explore(grid , row , col , visited):
    row_in_bounds = 0 <= row < len(grid)
    col_in_bounds = 0 <= col < len(grid[0])
    
    if (not row_in_bounds) or (not col_in_bounds):
        return False
    
    if grid[row][col] == "W":
        return False
    
    node = (row , col)
    # node = f"{row},{col}"
    if node in visited:
        return False
    
    visited.add(node)
    
    explore(grid , row-1 , col , visited)
    explore(grid , row+1 , col , visited)
    explore(grid , row, col-1, visited)
    explore(grid , row, col+1 , visited)
    
    return True

    
    


# grid = [
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'L', 'W', 'W', 'W'],
#     ['W', 'W', 'W', 'L', 'W'],
#     ['W', 'W', 'L', 'L', 'W'],
#     ['L', 'W', 'W', 'L', 'L'],
#     ['L', 'L', 'W', 'W', 'W'],
# ]

grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

result = island_count(grid)
print(result)