

# Index of first occurrence or insert pos
def lower_bound(arr,target):
    '''Returns first index where element ≥ target'''
    low, high = 0, len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


# Index of next greater element
def upper_bound(arr,target):
    '''Returns first index where element > target'''
    low, high = 0, len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    
    return mid

arr = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(lower_bound(arr, target))  # Output: 1
print(upper_bound(arr, target))  # Output: 4


# # Predefined Methods
# import bisect
# print(bisect.bisect_left(arr, target))  # Lower Bound
# print(bisect.bisect_right(arr, target)) # Upper Bound