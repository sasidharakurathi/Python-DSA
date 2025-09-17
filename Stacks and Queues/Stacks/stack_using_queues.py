
# Stack using queue is an implementation of LIFO using the FIFO data structure.

class StackUsingQueue:
    
    def __init__(self):
        self.queue = list()
    
    def push(self,data):
        self.queue.append(data)
        for i in range(len(self.queue) - 1):    # Rotating the queue to restructure into stack
            self.queue.append(self.queue.pop(0))
    
    def pop(self):
        return self.queue.pop(0) if self.queue else None
    
    def top(self):
        return self.queue[0] if self.queue else None
    
    def display(self):
        print(self.queue)
        
s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.top())  # Output: 50
s.pop()
print(s.top())  # Output: 40
s.display()