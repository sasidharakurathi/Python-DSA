

def bubble_sort(arr):
    '''
        - Compare arr[i] and arr[i+1]
        - Swap if arr[i] > arr[i+1]
        - Repeat for n-1 passes
    '''
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

arr = [20,60,10,30,40]
print(bubble_sort(arr))


