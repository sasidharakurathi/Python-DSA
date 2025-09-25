


def fibo(n, dp):
    if n == 0 or n == 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo(n-2, dp) + fibo(n-1, dp)
    
    return dp[n]

if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)   # memoization
    print(f"{fibo(5)}")                                                             # Output: 5
    n = 6
    dp = [-1] * (n+1)   # memoization
    print(f"{fibo(6)}")                                                             # Output: 8
