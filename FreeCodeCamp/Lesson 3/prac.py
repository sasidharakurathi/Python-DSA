

nums = [4,2,6,3,4,6,2,1]

def bubble_sort(nums):
    nums = list(nums)
    
    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i] , nums[i+1] = nums[i+1] , nums[i]
                
    return nums

def merge_sort(nums):
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)
    
    sorted_nums = merge(left_sorted , right_sorted)
    
    return sorted_nums

def merge(nums1 , nums2):
    merged_list = []
    
    i , j = 0 , 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i += 1
        else:
            merged_list.append(nums2[j])
            j += 1
    
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    return merged_list + nums1_tail + nums2_tail


#   Test cases:

# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(merge_sort , tests)

