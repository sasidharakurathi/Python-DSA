
# Given a sorted array and a target, return the first and last index of the target.
# If the target isn’t found, return -1.


def first_occurrence(arr,target):
    low, high = 0, len(arr)-1
    
    while low<=high:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if low < len(arr) and arr[low] == target:
        return low
    return -1

def last_occurrence(arr,target):
    low, high = 0, len(arr)-1
    
    while low<=high:
        mid = low + (high-low)//2
        
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    
    if low-1 >= 0 and arr[low-1] == target:
        return low-1
    return -1 

arr = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(first_occurrence(arr, target))  # Output: 1
print(last_occurrence(arr, target))   # Output: 3


arr = [1, 3, 4, 5]
target = 2

print(first_occurrence(arr, target))  # Output: -1
print(last_occurrence(arr, target))    # Output: -1

