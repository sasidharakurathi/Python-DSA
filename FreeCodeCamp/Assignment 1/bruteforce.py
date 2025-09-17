
#   Input:  Sorted Rotated nums ->  [5, 6, 9, 0, 2, 3, 4]
#   Output: Minimum Number of times the sorted nums rotated -> 3

from jovian.pythondsa import evaluate_test_cases


def count_rotations(sorted_nums):
    if len(sorted_nums) == 0 or len(sorted_nums) == 1:
        return 0
    
    index = 0
    while index < len(sorted_nums)-1:
        if sorted_nums[index] > sorted_nums[index+1]:
            return index+1
        index += 1
    
    return 0
    


test_cases = [
        {
        "input": {
            "sorted_nums": [5, 6, 9, 0, 2, 3, 4],
        },
        "output": 3
    },
        {
        "input": {
            "sorted_nums": [0, 2, 3, 4,5, 6, 9],
        },
        "output": 0
    },
        {
        "input": {
            "sorted_nums": [2],
        },
        "output": 0
    },
        {
        "input": {
            "sorted_nums": [],
        },
        "output": 0
    },
        {
        "input": {
            "sorted_nums": [5, 4],
        },
        "output": 1
    },
]

# for test_case in test_cases:
#     # print(**test_case["input"])
#     print(test_case["output"],count_rotations(**test_case["input"]))

evaluate_test_cases(count_rotations, test_cases)


