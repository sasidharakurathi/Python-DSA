

def binary_search(arr, target):
    low , high = 0 , len(arr)-1
    
    while low <= high:
        # mid = (low + high) // 2
        mid = low + (high - low) // 2   # -> (low + high//2 - low//2) -> (low//2 + high//2) -> (low+high)//2
        # we use this formula to overcome the interger overflow when the 'high' and 'low' values are very high. (for c,c++ and java)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    
    return -1

arr = [10,20,30,40,50]
print(binary_search(arr,50))    # Output: 4
print(binary_search(arr,30))    # Output: 2
print(binary_search(arr,20))    # Output: 1
print(binary_search(arr,90))    # Output: -1
