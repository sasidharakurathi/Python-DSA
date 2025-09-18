
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
        
    
    def delete_node(self, value):
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next
        
        if temp is None:
            return
        
        # If node to delete is head
        if temp == self.head: # or temp.prev is None
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # If node to delete is tail
        if temp.next is None:
            temp.prev.next = None
            return
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
    
    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
    
    def print_backward(self):
        temp = self.head
        
        if temp is None:
            return
        
        while temp.next:
            temp = temp.next
        
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


dll = DoubleLinkedList()
dll.insert_at_head(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.print_forward()     # Output: 10 <-> 20 <-> 30 <-> None
dll.print_backward()    # Output: 30 <-> 20 <-> 10 <-> None
dll.delete_node(20)
dll.print_forward()     # Output: 10 <-> 30 <-> None
