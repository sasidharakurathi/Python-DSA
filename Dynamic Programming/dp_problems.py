import sys
sys.setrecursionlimit(10**6)


def house_robber_memoization(nums):
    
    '''
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed, 
        the only constraint stopping you from robbing each of them is that adjacent houses have 
        security systems connected and it will automatically contact the police if two adjacent houses were 
        broken into on the same night.

        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.
    '''
    
    def rec(i, nums, dp):
        
        if i >= len(nums):
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        take = nums[i] + rec(i+2, nums, dp)
        not_take = rec(i+1, nums, dp)
        
        dp[i] = max(take, not_take)

        return dp[i]
    
    
    dp = [-1] * len(nums)
    return rec(0, nums, dp)

def house_robber_tabulation(nums):
    # n = len(nums)
    
    # if n == 1:
    #     return nums[0]
    
    # dp = [0] * n
    # dp[0] = nums[0]
    # dp[1] = max(nums[0], nums[1])
    
    # for i in range(2,n):
    #     not_take = dp[i-1]
    #     take = nums[i] + dp[i-2]
        
    #     dp[i] = max(not_take, take)
    
    # return dp[n-1]
    
    
    # Space Complexity: O(1)
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    a = nums[0]
    b = max(nums[0], nums[1])
    
    for i in range(2,n):
        not_take = b
        take = nums[i] + a
        
        c = max(not_take, take)
        
        a, b = b, c
    
    return b

def house_robber_2(nums):
    '''
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
        That means the first house is the neighbor of the last one. 
        Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police 
        if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.
    '''

    def rec(i, n, nums, dp):
            if i>= n:
                return 0

            if dp[i] != -1:
                return dp[i]
            
            take = nums[i] + rec(i+2, n, nums,dp)
            not_take = rec(i+1, n, nums,dp)

            dp[i] = max(take, not_take)
            return dp[i]
    
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [-1] * n
    way1 = rec(0,n-1,nums,dp)
    dp = [-1] * n
    way2 = rec(1,n,nums,dp)

    return max(way1, way2)

def can_partition(nums):
    '''
        Given an integer array nums, return true if you can partition the array into two subsets 
        such that the sum of the elements in both subsets is equal or false otherwise.
    '''
    
    def rec(i,sum1,nums,total,dp):
        
        if sum1 == (total//2):
            return True
        
        if (sum1 > total//2) or (i == len(nums)):
            return False
        
        if dp[i][sum1] != -1:
            return dp[i][sum1]
        
        take = False
        if sum1+nums[i] <= (total//2):
            take = rec(i+1,sum1+nums[i],nums,total,dp)      # 0/1 knapsack (No repeated item selection)
        not_take = rec(i+1,sum1,nums,total,dp)
        
        dp[i][sum1] = take or not_take
        
        return dp[i][sum1]

    n = len(nums)
    if n == 1:
        return False
    
    total = sum(nums)
    if total%2 != 0:
        return False
    
    dp = [[-1 for j in range(total//2 + 1)] for i in range(len(nums))]
    return rec(0,0,nums,total,dp)

def coin_change(coins, amount):
    '''
        You are given an integer array coins representing coins of different denominations and 
        an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.
    '''
    
    def rec(i,sum1,coins,amount,dp):
        if sum1 == amount:
            return 0
        
        if sum1 > amount or i == len(coins):
            return float("inf")
        
        if dp[i][sum1] != -1:
            return dp[i][sum1]
        
        take = float("inf")
        if sum1 + coins[i] <= amount:
            take = 1 + rec(i,sum1+coins[i],coins,amount,dp)     # unbounded knapsack (Repeated item selection)
        not_take = rec(i+1,sum1,coins,amount,dp)
        
        dp[i][sum1] = min(take, not_take)
        
        return dp[i][sum1]
        
    
    if amount == 0:
        return 0
    
    dp = [[-1 for j in range(amount+1)] for i in range(len(coins))]
    result = rec(0,0,coins,amount,dp)
    return -1 if result == float("inf") else result
    
def longest_common_subsequence(text1, text2):
    '''
        Given two strings text1 and text2, return the length of their longest common subsequence. 
        If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string with some characters 
        (can be none) deleted without changing the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".
        A common subsequence of two strings is a subsequence that is common to both strings.
    '''
    
    def rec(i,j,text1,text2,dp):
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if text1[i] == text2[j]:
            return 1 + rec(i+1,j+1,text1,text2,dp)
        
        dp[i][j] = max(rec(i+1,j,text1,text2,dp) , rec(i,j+1,text1,text2,dp))
        
        return dp[i][j]
    
    dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
    return rec(0,0,text1,text2,dp)

def longest_palindrome_subseq(s):
    '''
        Given a string s, find the longest palindromic subsequence's length in s.

        A subsequence is a sequence that can be derived from another sequence by deleting some or 
        no elements without changing the order of the remaining elements.
    '''
    
    def rec(i,j,text1,text2,dp):
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if text1[i] == text2[j]:
            return 1 + rec(i+1,j+1,text1,text2,dp)
        
        dp[i][j] = max(rec(i+1,j,text1,text2,dp) , rec(i,j+1,text1,text2,dp))
        
        return dp[i][j]
    
    text1 = s
    text2 = s[::-1]
    dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
    return rec(0,0,text1,text2,dp)
    
    
    

if __name__ == "__main__":
    # House Robber
    nums = [1,2,3,1]
    print(f"{house_robber_memoization(nums) = }")                                           # Output: 4
    nums = [2,7,9,3,1]
    print(f"{house_robber_memoization(nums) = }")                                           # Output: 12
    
    # House Robber
    nums = [1,2,3,1]
    print(f"{house_robber_tabulation(nums) = }")                                            # Output: 4
    nums = [2,7,9,3,1]
    print(f"{house_robber_tabulation(nums) = }")                                            # Output: 12
    
    # House Robber II 
    nums = [2,3,2]
    print(f"{house_robber_2(nums) = }")                                                     # Output: 12
    nums = [1,2,3,1]
    print(f"{house_robber_2(nums) = }")                                                     # Output: 12
    nums = [1,2,3]
    print(f"{house_robber_2(nums) = }")                                                     # Output: 12
    
    # Partition Equal Subset Sum
    nums = [1,5,11,5]
    print(f"{can_partition(nums) = }")                                                      # Output: True
    nums = [1,2,3,5]
    print(f"{can_partition(nums) = }")                                                      # Output: False
    nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    print(f"{can_partition(nums) = }")                                                      # Output: False
    
    # Coin Change
    coins , amount = [1,2,5], 11
    print(f"{coin_change(coins,amount) = }")                                                # Output: 3
    coins , amount = [2], 3
    print(f"{coin_change(coins,amount) = }")                                                # Output: -1
    coins , amount = [1], 0
    print(f"{coin_change(coins,amount) = }")                                                # Output: 0
    coins , amount = [3,7,405,436], 8839
    print(f"{coin_change(coins,amount) = }")                                                # Output: 25
    
    # Longest Common Subsequence
    text1, text2 = "abcde", "ace" 
    print(f"{longest_common_subsequence(text1,text2) = }")                                  # Output: 3
    text1, text2 = "abc", "abc" 
    print(f"{longest_common_subsequence(text1,text2) = }")                                  # Output: 3
    text1, text2 = "abc", "def" 
    print(f"{longest_common_subsequence(text1,text2) = }")                                  # Output: 0
    text1, text2 = "pmjghexybyrgzczy", "hafcdqbgncrcbihkd" 
    print(f"{longest_common_subsequence(text1,text2) = }")                                  # Output: 4
    
    # Longest Common Subsequence
    s = "bbbab"
    print(f"{longest_palindrome_subseq(s) = }")                                             # Output: 4
    s = "cbbd" 
    print(f"{longest_palindrome_subseq(s) = }")                                             # Output: 2
    s = "pmjghexybyrgzczy"
    print(f"{longest_palindrome_subseq(s) = }")                                             # Output: 5
    
    