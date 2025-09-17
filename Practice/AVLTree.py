

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def getHeight(self , node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self , node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rightRotate(self , z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left) , self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left) , self.getHeight(y.right))
        return y
    
    def leftRotate(self , z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left) , self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left) , self.getHeight(y.right))
        return y
    
    def _insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def in_order_traversal(self):
        self._in_order_traversal(self.root)
    
    def _in_order_traversal(self , node):
        if node:
            self._in_order_traversal(node.left)
            print(node.key , end=" ")
            self._in_order_traversal(node.right)
        
        
        
if __name__ == "__main__":
    l = [10, 5, 15, 3, 7, 13, 17]
    
    avltree = AVLTree()
    
    for i in l:
        avltree.insert(i)
        
    avltree.in_order_traversal()