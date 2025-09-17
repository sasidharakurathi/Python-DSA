
#   Input:  Sorted Rotated nums ->  [5, 6, 9, 0, 2, 3, 4]
#   Output: Minimum Number of times the sorted nums rotated -> 3

from jovian.pythondsa import evaluate_test_cases


def count_rotations(nums):
    if len(nums) == 0 or len(nums) == 1:
        return 0
    
    low , high = 0 , len(nums)-1
    
    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]
        
        if mid_number < nums[mid - 1]:
            return mid
        elif mid_number > nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    
    return 0
    



test_cases = [
        {
        "input": {
            "nums": [5, 6, 0, 1, 2, 3, 4],
        },
        "output": 2
    },
        {
        "input": {
            "nums": [0, 2, 3, 4,5, 6, 9],
        },
        "output": 0
    },
        {
        "input": {
            "nums": [2],
        },
        "output": 0
    },
        {
        "input": {
            "nums": [],
        },
        "output": 0
    },
        {
        "input": {
            "nums": [5, 4],
        },
        "output": 1
    },
]


evaluate_test_cases(count_rotations, test_cases)