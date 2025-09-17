

def binary_search(items , e):
    low = 0
    high = len(items)-1
    
    while low <= high:
        mid = (low+high) // 2
        if items[mid] == e:
            return mid
        elif items[mid] < e:
            low = mid - 1
        elif items[mid] > e:
            high = mid+1
    
    return -1

print(binary_search([13, 11, 10, 7, 4, 3, 1, 0] , 7))