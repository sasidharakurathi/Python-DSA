class TreeNode:
    def __init__(self , key , value=None):
        self.left = None
        self.key = key
        self.value = value
        self.right = None
        self.parent = None
    
class BalancedBST:
    def __init__(self):
        self.root = None
    
    def __setitem__(self , key , value):
        node = self.find(key)
        
        if node is None:
            self.root = self.insert(key , value)
            self.balance_bst()
        else:
            self.update(key , value)
            
    def __getitem__(self , key):
        node = self.find(key)
        return (node.key , node.value) if node is not None else None
    
    def __len__(self):
        return self.tree_size()
    
    def __iter__(self):
        return (x for x in self.in_order_traversal())
    
    def tree_size(self, node="root"):
        if node == "root":
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.tree_size(node.left) + self.tree_size(node.right)  
    
    def display(self ,space='  ' , level=0 , node="root"):
        if node == "root":
            node = self.root
        
        if node is None:
            print(space * level + "X")
            return
        
        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return
        
        self.display(level=level+1 , node=node.right)
        print(space * level + str(node.key))
        self.display(level=level+1 , node=node.left)
    
    
    def balance_bst(self):
        self.root = self.make_balanced_bst(self.in_order_traversal())
    
    def in_order_traversal(self , node="root"):
        if node == "root":
            node = self.root
            
        if node is None:
            return []
        
        return self.in_order_traversal(node.left) + [(node.key , node.value)] + self.in_order_traversal(node.right)
    
    
    def make_balanced_bst(self, data ,low=0 , high=None , parent=None):
        
        if high is None:
            high = len(data) - 1
            
        if low > high:
            return None
        
        mid = (low + high) // 2
        
        key , value = data[mid]
        node = TreeNode(key , value)
        node.parent = parent
        node.left = self.make_balanced_bst(data , low , mid-1 , node)
        node.right = self.make_balanced_bst(data , mid+1 , high , node)
        
        return node
    
        
    def find(self , key , node="root"):
        if node == "root":
            node = self.root
        
        if node is None:
            return None
        
        if key == node.key:
            return node
        elif key < node.key:
            return self.find(key , node.left)
        elif key > node.key:
            return self.find(key , node.right)
        
    def insert(self , key , value , node="root"):
        if node =="root":
            node = self.root
        
        if node is None:
            return TreeNode(key , value)
        elif key < node.key:
            node.left = self.insert(key , value , node.left)
            node.left.parent = node
        elif key > node.key:
            node.right = self.insert(key , value , node.right)
            node.right.parent = node
        
        return node
    
    def update(self , key , value , node="root"):
        target = self.find(key)
        
        if target is not None:
            target.value = value
            return True
        
        return False
        
    

if __name__ == "__main__":
    tree = BalancedBST()
    l = [(1 , "ASH") , (2 , "SAM") , (3 , "LEO") , (4 , "BOB") , (5 , "DANNY")]
    
    for i in l:
        key , value = i
        tree[key] = value
        
    # print(tree.find(1))
    tree.display()
    tree[3] = "AAA"
    print(tree.in_order_traversal())
    print(len(tree))
    
    for i in tree:
        print(i)
    
    print(dict(tree))
    print(list(tree))
    print(tuple(tree))
    print(set(tree))
        
    # print(tree.in_order_traversal())
    # print(tree[1])
    # print(len(tree))
    
    # print(list(tree))
    
    # for i in tree:
    #     print(i)
    
    
    # tree.display()
    
    