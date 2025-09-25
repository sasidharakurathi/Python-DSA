

def knapsack(i, W, n, values, weights):
    # 0/1 Knapsack
    
    if i == n:
        return 0
    
    take = 0
    if weights[i] <= W:
        take = values[i] + knapsack(i+1, W-weights[i], n, values, weights)
    
    not_take = knapsack(i+1,W,n,values,weights)
    
    return max(take, not_take)

def unbounded_knapsack(i, W, n, values, weights):
    # Unbouned 0/1 Knapsack
    
    if i == n:
        return 0
    
    take = 0
    if weights[i] <= W:
        take = values[i] + unbounded_knapsack(i,W-weights[i],n,values,weights)
    
    not_take = unbounded_knapsack(i+1,W,n,values,weights)
    
    return max(take, not_take)


if __name__ == "__main__":
    n = 5
    values = [10,5,8,5,3]
    weights = [3,2,4,6,4]
    W = 6
    
    print(f'{knapsack(0,W,n,values,weights) = }')                                   # Output: 15
    print(f'{unbounded_knapsack(0,W,n,values,weights) = }')                         # Output: 20