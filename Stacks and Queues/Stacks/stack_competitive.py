# Stack Datastructure for competitive exams

stack = list()

while True:
    print("--- Stack Operations ---\n1. Push\n2. Pop\n3. Peek\n4. Top\n5. Display\n6. Exit")
    choice = input("Enter choice: ")
    
    match (choice):
        case "1":
            data = input("Enter data: ")
            stack.append(data)
            
        case "2":
            if len(stack) == 0: 
                print("List is empty can not pop the stack")
            else:
                data = stack.pop()
                print(f"{data} is poped from stack")
                
        case "3":
            peek = len(stack)
            print(f"Stack Peek: {peek}")
            
        case "4":
            if stack:
                print(f"Top: {stack[-1]}")
            else:
                print("Stack is empty")
        
        case "5":
            print("Stack Content: ")
            print(stack[::-1])
        
        case _:
            quit(0)