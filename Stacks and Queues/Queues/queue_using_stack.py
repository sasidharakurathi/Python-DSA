

class QueueUsingStacks:
    
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
    
    def enqueue(self,data):
        self.stack1.append(data)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack:
            print("Queue underflow")
            return
    
        return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2[-1]

    
    def is_empty(self):
        return not self.stack1 and not self.stack2

