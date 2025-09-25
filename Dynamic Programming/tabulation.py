

def fibo(n):
    if n == 0 or n == 1:
        return n
    
    # dp = [0] * (n+1)
    # dp[0] = 0
    # dp[1] = 1
    
    # for i in range(2,n+1):
    #     dp[i] = dp[i-2] + dp[i-1]
    
    # return dp[n]
    # # return dp[-1]
    # # return dp[i]
    
    
    # Space Complexity: O(1)
    a , b = 0, 1
    for i in range(2,n+1):
        a, b = b, a+b
    
    return b



if __name__ == "__main__":
    print(f"{fibo(5)}")                                                             # Output: 5
    print(f"{fibo(6)}")                                                             # Output: 8