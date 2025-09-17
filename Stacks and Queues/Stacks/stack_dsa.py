
# Stack Datastructure 
class Stack:
    def __init__(self):
        self.stack = list()
        self.top = None

    def push(self, data):
        self.stack.append(data)
        self.top = 1 if self.top is None else self.top + 1
        return self.top
    
    def pop(self):
        if self.top is None or self.top == 0:
            print("List is empty can not pop the stack")
            return
        self.top -= 1
        return self.stack.pop()
    
    def peek(self):
        if self.top is None:
            return 0
        
        return self.top

    def top(self):
        return self.stack[-1] if self.stack else None
    
    def display(self):
        if self.stack:
            print("Stack Content: ")
            for i in range(-1,-len(self.stack)-1,-1):
                print(self.stack[i] , end=" ")
            print()
            return
        
        print("Stack is Empty")
            
    

stack = Stack()
while True:
    print("--- Stack Operations ---\n1. Push\n2. Pop\n3. Peek\n4. Top\n5. Display\n6. Exit")
    choice = input("Enter choice: ")
    
    match (choice):
        case "1":
            data = input("Enter data: ")
            stack.push(data)
        case "2":
            data = stack.pop()
            if data: print(f"{data} is poped from stack")
        case "3":
            peek = stack.peek()
            print(f"Stack Peek: {peek}")
        case "4":
            top = stack.top()
            if top:
                print(f"Top: {top}")
            else:
                print("Stack is empty")
        
        case "5":
            stack.display()
        
        case _:
            quit(0)
    
    


