
# Given a sorted array and a target, return the index where the target should be inserted.
# If it exists, return its index. If not, return the index where it would go.

# This is also a lower bound binary search problem.

def search_insert_position(arr, target):
    low, high = 0, len(arr)-1
    
    while low<=high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low  # Insert position

arr = [1, 3, 5, 6]
target = 2
print(search_insert_position(arr, target))  # Output: 1
target = 3
print(search_insert_position(arr, target))  # Output: 1
target = 5
print(search_insert_position(arr, target))  # Output: 2


