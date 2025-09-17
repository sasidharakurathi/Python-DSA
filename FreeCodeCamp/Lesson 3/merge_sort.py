def merge_sort(nums):
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)
    
    sorted_list = merge(left_sorted , right_sorted)
    
    return sorted_list
    

def merge(num1 , num2):
    
    merged_list = []
    
    i , j = 0 , 0
    
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged_list.append(num1[i])
            i += 1
        else:
            merged_list.append(num2[j])
            j += 1
    
    num1_tail = num1[i:]
    num2_tail = num2[j:]
    
    return merged_list + num1_tail + num2_tail



    