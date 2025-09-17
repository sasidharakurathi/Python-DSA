# Two Stacks in One Array (Implementing Two stacks in a single array or list)

class TwoStacks:
    
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top1 = -1
        self.top2 = size
    
    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.stack[self.top1] = data
        else:
            print("Stack Overflow for Stack 1")
    
    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.stack[self.top2] = data
        else:
            print("Stack Overflow for Stack 2")
            
    
    def pop1(self):
        if self.top1 >= 0:
            data = self.stack[self.top1]
            self.top1 -= 1
            return data
        print("Stack Underflow for Stack 1")
        return None
    
    def pop2(self):
        if self.top2 < self.size:
            data = self.stack[self.top2]
            self.top2 += 1
            return data
        
        print("Stack Underflow for Stack 2")
        return None

    def displayStack1(self):
        if self.top1 > -1:
            print(self.stack[:self.top1+1][::-1])   # reversing the list to display the top content of stack first
        else:
            print("Stack 1 is empty")
    
    def displayStack2(self):
        if self.top2 < self.size:
            print(self.stack[self.top2:])   # no need of reversing the list, since the data is already placed in reverse order
        else:
            print("Stack 2 is empty")
        
ts = TwoStacks(10)
ts.push1(1)
ts.push1(2)
ts.push1(3)
ts.push1(4)
ts.push1(5)
ts.push2(9)
ts.push2(8)
ts.push2(7)
ts.push2(6)
ts.push2(10)
print(ts.pop1())
print(ts.pop2())
ts.push1(11)
ts.push2(12)
ts.displayStack1()
ts.displayStack2()