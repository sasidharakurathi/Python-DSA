
class Node:
    def __init__(self , val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self , val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._recursive_insert(self.root , val)
    
    def _recursive_insert(self , node , val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._recursive_insert(node.left , val)
        elif val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._recursive_insert(node.right , val)
    
    def search(self, val):
        return self._recursive_search(self.root,val)
    
    def _recursive_search(self,node , val):
        if node is None or node.val == val:
            return node
        else:
            if val < node.val:
                return self._recursive_search(node.left , val)
            return self._recursive_search(node.right , val)
    
    def in_order_traversal(self):
        self._in_order_traversal(self.root)
    
    def _in_order_traversal(self , node):
        if node:
            self._in_order_traversal(node.left)
            print(node.val , end=" ")
            self._in_order_traversal(node.right)

if __name__ == "__main__":
    
    l = [10, 5, 15, 3, 7, 13, 17]
    
    bst = BinarySearchTree()
    for i in l:
        bst.insert(i)
        
    print(f"Searching 15: {bst.search(15)}")
    print(f"Searching 155: {bst.search(155)}")
    
    bst.in_order_traversal()
            