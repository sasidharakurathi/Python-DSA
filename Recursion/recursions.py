

def print_n_natural_numbers(n,i=1):
    # base case
    if i > n:
        print()
        return
    
    print(i,end=" ")
    
    #recursion
    print_n_natural_numbers(n,i+1)
    
def fact(n):
    # base case
    if n == 0:
        return 1
    
    # recursion
    return n * fact(n-1)


def fibo(n):
    # base case
    if n == 0 or n == 1:
        return n
    
    # recursion
    return fibo(n-2) + fibo(n-1)

def tribonacci(n):    
    '''
        The Tribonacci sequence Tn is defined as follows: 

        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        Given n, return the value of Tn.
    '''
    # base cases
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    # recursion
    return  tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

def isPowerOfTwo(n):
    '''
        Given an integer n, return true if it is a power of two. Otherwise, return false.

        An integer n is a power of two, if there exists an integer x such that n == 2^x.
    '''
    
    # base cases
    if n <= 0: return False
    if n == 1: return True
    if n%2 != 0: return False
    
    # recursion
    return isPowerOfTwo(n//2)

def isPowerOfThree(n):    
    '''
        Given an integer n, return true if it is a power of three. Otherwise, return false.

        An integer n is a power of three, if there exists an integer x such that n == 3^x.
    '''
    
    # base cases
    if n <= 0: return False
    if n == 1: return True
    if n%3 != 0: return False
    
    # recursion
    return isPowerOfThree(n//3)

def GCD(a,b):
    '''
        Greated Common Divisor of the a and b
    '''
    # base case
    if b == 0:
        return a
    
    # recursion
    return GCD(b,a%b)

def LCM(a,b):
    return (a*b) // GCD(a,b)

def findPow(x,n):
    # base case
    if n == 0:
        return 1    # any number power 0 is always 1
    
    # recursion
    a = findPow(x,n//2) # find x ^ (n/2)
    if n%2 == 0:        
        return a*a      # if x ^ (n/2) is even, just multiple itself to get x ^ n
    else:
        return a*a*x    # if x ^ (n/2) is odd, multiple itself and multiple the result with x to get x ^ n
    
def myPow(x, n):
    '''
        Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
    '''
    
    if n >= 0:
        return findPow(x,n)     # if n is postive calculate the power
    return 1 / findPow(x,-n)    # if n is negative calculate the power of "x , +n" and return "1 / result"



if __name__ == "__main__":
    print_n_natural_numbers(5)                                      # Output: 1 2 3 4 5
    print(fact(4))                                                  # Output: 24
    print(fibo(10))                                                 # Output: 55
    print(tribonacci(25))                                           # Output: 1389537
    print(isPowerOfTwo(32))                                         # Output: True
    print(isPowerOfThree(81))                                       # Output: True
    print(GCD(15,50))                                               # Output: 5
    print(LCM(15,50))                                               # Output: 150
    print(myPow(2,10))                                              # Output: 1024
    print(myPow(2,-2))                                              # Output: 0.25
    