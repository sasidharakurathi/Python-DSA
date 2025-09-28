
def selection_sort(arr):
    '''
        - For each position i, find the minimum element from i to n-1
        - Swap it with arr[i]
    '''
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


arr = [20,60,10,30,40]
print(selection_sort(arr))