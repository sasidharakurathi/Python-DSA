

def merge_sort(arr):
    '''
        - Divide the array into two halves
        - Recursively sort each half
        - Merge the two sorted halves
    '''
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    return result + left[i:] + right[j:]


arr = [20,60,10,30,40]
print(merge_sort(arr))

            