

class Queue:
    
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rare = -1
    
    def is_full(self):
        return self.rare == self.capacity-1
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue Overflow")
            return
        
        if self.is_empty():
            self.front = 0
        self.rare += 1
        self.queue[self.rare] = data
        
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        
        data = self.queue[self.front]
        self.front += 1
        
        if self.front > self.rare:
            self.front = self.rare = -1

        return data
        
    def get_front(self):
        return self.front
    
    def get_rear(self):
        return self.rare
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        print(f"Queue: {self.queue[self.front:self.rare+1]}")    
    
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)
queue.dequeue()
queue.enqueue(100)
queue.display()