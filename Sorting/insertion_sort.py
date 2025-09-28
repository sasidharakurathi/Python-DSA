

def insertion_sort(arr):
    '''
        - Start from index 1
        - Compare with elements to its left
        - Shift larger elements right
        - Insert current element at correct spot
    '''
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
    return arr


arr = [20,60,10,30,40]
print(insertion_sort(arr))
