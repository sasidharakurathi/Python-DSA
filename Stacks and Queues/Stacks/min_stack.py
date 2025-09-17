
# A MinStack is basically a stack which maintains the minimum element of the stack at every level

class MinStack:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        
    def push(self,data):
        self.stack.append(data)
        
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)
        else:
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self):
        if self.stack:
            data = self.stack.pop()
            self.min_stack.pop()

            return data
        
        print("Stack is empty! Can not pop the stack.")
    
    def peek(self):
        return len(self.stack)
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def display(self):
        print(f"Stack Content: {self.stack[::-1]}")
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None
    
    
min_stack = MinStack()
min_stack.push(5)
min_stack.push(3)
min_stack.push(7)
print(min_stack.get_min())  # Output: 3
min_stack.pop()
print(min_stack.get_min())  # Output: 3
min_stack.pop()
print(min_stack.get_min())  # Output: 5