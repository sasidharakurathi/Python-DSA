
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,data):
        '''Insert at start of the LinkedList'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self,data):
        '''Insert at end of the LinkedList'''
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        
    
    def delete_by_value(self, value):
        temp = self.head
        
        if temp and temp.data == value:
            self.head = temp.next
            return
        
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        
        if temp is None:
            return
            
        prev.next = temp.next
        
    
    def search(self, value):
        temp = self.head
        
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        
        return False
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        
    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def check_cycle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True

        
        return False    
                    
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    

sll = SingleLinkedList()
sll.insert_at_head(10)
sll.insert_at_tail(20)
sll.insert_at_tail(30)
sll.insert_at_tail(40)
# sll.print()         # Output: 10 -> 20 -> 30 -> None
print(sll.find_middle())
print(sll.check_cycle())
sll.reverse()
# sll.print()         # Output: 30 -> 20 -> 10 -> None
# print(sll.search(20))    # Output: True
sll.delete_by_value(20)
# sll.print()         # Output: 30 -> 10 -> None
