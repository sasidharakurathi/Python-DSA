# Stack with Middle Element Access in O(1) time complexity (We cam achieve this using DLL)

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class StackWithMiddle:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def push(self, data):
        new_node = DLLNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.count += 1

        if self.count == 1:
            self.mid = new_node
        else:
            if self.count % 2 != 0:
                self.mid = self.mid.prev

    def pop(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.count -= 1

        if self.count % 2 == 0 and self.mid:
            self.mid = self.mid.next

        return item

    def findMiddle(self):
        return self.mid.data if self.mid else None

    def deleteMiddle(self):
        if not self.mid:
            return None
        item = self.mid.data
        if self.mid.prev:
            self.mid.prev.next = self.mid.next
        if self.mid.next:
            self.mid.next.prev = self.mid.prev

        if self.count % 2 == 0:
            self.mid = self.mid.next
        else:
            self.mid = self.mid.prev

        self.count -= 1
        return item
    
    
s = StackWithMiddle()
s.push(1)
s.push(2)
s.push(3)
print(s.findMiddle())     # Output: 2
s.deleteMiddle()
print(s.findMiddle())     # Output: 3