import heapq

# Kth Largest Element in an Array
def kth_larget_element(arr, k):
    '''
        Given an integer array nums and an integer k, return the kth largest element in the array.

        Note that it is the kth largest element in the sorted order, not the kth distinct element.

        Can you solve it without sorting?
    '''
    heap = []
    
    for ele in arr:
        heapq.heappush(heap, ele)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]


def last_stone_weight(stones):
    '''
        You are given an array of integers stones where stones[i] is the weight of the ith stone.

        We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
        At the end of the game, there is at most one stone left.

        Return the weight of the last remaining stone. If there are no stones left, return 0.
        
        Example 1:
            Input: stones = [2,7,4,1,8,1]
            Output: 1
            Explanation: 
                We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
                we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
                we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
                we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
    '''
    
    '''
        here we need to use max_heap.
        
        In python to implement max heap using heapq module, 
        we convert the elements of array to their respective negative values and then heappush them. 
        
        And when we heappop, the poped value is converted back into postive value 
        before performing any further operations
    '''
    max_heap = []

    for stone in stones:
        heapq.heappush(max_heap, -stone)
    
    while len(max_heap) > 1:
        top1 = - heapq.heappop(max_heap)
        top2 = - heapq.heappop(max_heap)
        diff = (top1-top2)
        if  diff != 0:
            heapq.heappush(max_heap, -diff)
    
    if len(max_heap) == 1:
        return -heapq.heappop(max_heap)


if __name__ == "__main__":
    h = []
    heapq.heapify(h) # Default Min Heap is created

    heapq.heappush(h, 5)
    heapq.heappush(h, 1)
    heapq.heappush(h, 3)
    heapq.heappush(h, 7)

    print(h)                                                        # Output: [1, 5, 3, 7]
    print(heapq.heappop(h))                                         # Output: 1
    print(heapq.nlargest(2,h))                                      # Output: [7,5]s
    print(kth_larget_element([3,2,1,5,6,4], 2))                     # Output: 5
    print(kth_larget_element([3,2,3,1,2,4,5,5,6], 4))               # Output: 4
    print(last_stone_weight([2,7,4,1,8,1]))                         # Output: 1
    print(last_stone_weight([1]))                                   # Output: 1