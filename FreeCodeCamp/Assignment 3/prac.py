# --- Problem ---

# Multiply two polynomials with their coefficients represented by two lists to get the product 
# also represented by a list of coefficients.

# --- Input ---

# List of coefficients representing polynomial A.
# List of coefficients representing polynomial B.

# --- Output ---

# List of coefficients representing A x B.


# --- Solution ---

# [2, 1, 5, 7] and [3, 4, 2]

from jovian.pythondsa import evaluate_test_cases

def multiply_polynomial(poly1 , poly2):
    n , m = len(poly1) , len(poly2)
    
    if n == 0 or m == 0:
        return []
    
    if poly1 == [0] * n or poly2 == [0] * m:
        return [0]
    
    result = [0] * (n+m-1)
    
    for i in range(n):
        for j in range(m):
            result[i+j] += (poly1[i] * poly2[j])
            
    return result

if __name__ == "__main__":
    test0 = {
        'input': {
            'poly1': [2, 0, 5, 7],
            'poly2': [3, 4, 2]
        },
        'output': [6, 8, 19, 41, 38, 14]
    }
    test1 = {
        'input': {
            'poly1': [2, 0, 5, 7],
            'poly2': [2, 0, 5, 7]
        },
        'output': [4, 0, 20, 28, 25, 70, 49]
    }
    test2 = {
        'input': {
            'poly1': [],
            'poly2': []
        },
        'output': []
    }
    test3 = {
        'input': {
            'poly1': [3],
            'poly2': [3]
        },
        'output': [9]
    }
    test4 = {
        'input': {
            'poly1': [],
            'poly2': [3, 4, 2]
        },
        'output': []
    }
    test5 = {
        'input': {
            'poly1': [1, -2, 3, -4],
            'poly2': [5, -6, 7, -8]
        },
        'output': [5, -16, 34, -60, 61, -52, 32]
    }
    test6 = {
        'input': {
            'poly1': [0],
            'poly2': [3, 4, 2]
        },
        'output': [0]
    }
    test7 = {
        'input': {
            'poly1': [7],
            'poly2': [2, 3]
        },
        'output': [14, 21]
    }
    test8 = {
        'input': {
            'poly1': [2, 3],
            'poly2': [7]
        },
        'output': [14, 21]
    }
    test9 = {
        'input': {
            'poly1': [8],
            'poly2': [6, 5, 4, 3]
        },
        'output': [48, 40, 32, 24]
    }
    test10 = {
        'input': {
            'poly1': [6, 5, 4, 3],
            'poly2': [8]
        },
        'output': [48, 40, 32, 24]
    }
    
    tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9, test10]
    
    print(evaluate_test_cases(multiply_polynomial , tests))
    