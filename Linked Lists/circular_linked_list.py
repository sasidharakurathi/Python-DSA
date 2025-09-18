
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None  # Points to the last node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def delete_node(self, key):
        if not self.last:
            return

        temp = self.last.next
        prev = self.last

        while temp.data != key:
            if temp == self.last:
                return  # Key not found
            prev = temp
            temp = temp.next

        if temp == self.last and temp.next == self.last:
            self.last = None
        elif temp == self.last:
            prev.next = temp.next
            self.last = prev
        else:
            prev.next = temp.next

    def print_list(self):
        if not self.last:
            print("List is empty")
            return
        temp = self.last.next
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.last.next:
                break
        print("(back to start)")


cll = CircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.print_list()         # Output: 10 -> 20 -> 30 -> (back to start)
cll.delete_node(20)
cll.print_list()         # Output: 10 -> 30 -> (back to start)