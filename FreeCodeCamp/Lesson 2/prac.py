class TreeNode:
    def __init__(self,key):
        self.left = None
        self.key = key
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def parse_tuple(self , data):
        self.root = self._parse_tuple(data)
        
    def tree_to_tuple(self) -> tuple:
        return self._tree_to_tuple(self.root)
    
    def in_order_traversal(self) -> list:
        return self._in_order_traversal(self.root)
    
    def pre_order_traversal(self) -> list:
        return self._pre_order_traversal(self.root)
    
    def post_order_traversal(self) -> list:
        return self._post_order_traversal(self.root)
    
    def display(self):
        self._display(self.root , '  ' , 0)
    
    def is_bst(self):
        return self._is_bst(self.root)
    
    def insert(self , key):
        self.root = self._insert(self.root , key)
        
    def find(self , key) -> TreeNode | None:
        return self._find(self.root , key)
    
    def update(self , key , new_key):
        self._update(self.root , key , new_key)
    
    def list_all(self) -> list:
        """List all the nodes in sorted order"""
        return self._in_order_traversal(self.root)
    
    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)[0]
    
    def make_balanced_bst(self , data):
        """Make balanced BST using Sorted List"""
        self.root = self._make_balanced_bst(data)
        
    def balance_bst(self):
        self.root = self._make_balanced_bst(self.list_all())
        
    
    
    
    
    def _make_balanced_bst(self , data , low=0 , high=None) -> TreeNode | None:
        """Make balanced BST using Sorted List"""
        if high is None:
            high = len(data) - 1
        
        if low > high:
            return None
        
        mid = (low + high) // 2
        node = TreeNode(data[mid])
        node.left = self._make_balanced_bst(data , low , mid-1)
        node.right = self._make_balanced_bst(data , mid+1 , high)
        
        return node
        
        
        
        
    
    
    def _is_balanced(self , node: TreeNode | None) -> tuple[bool,int]:
        if node is None:
            return True , 0
        
        balanced_l , height_l = self._is_balanced(node.left)
        balanced_r , height_r = self._is_balanced(node.right)
        
        balanced = (balanced_l and balanced_r and abs(height_l - height_r) <= 1)
        height = 1 + max(height_l , height_r)
        
        return balanced , height
    
    def _update(self,root: TreeNode , key , new_key) -> bool:
        target = self._find(root , key)
        if target is not None:
            target.key = new_key
            return True
        
        return False
    
    
    def _find(self , node: TreeNode | None , key) -> TreeNode | None:
        if node is None:
            return None
        
        if node.key == key:
            return node
        elif key < node.key:
            return self._find(node.left ,key)
        elif key > node.key:
            return self._find(node.right , key)
        
    
    def _insert(self, node: TreeNode | None , key) -> TreeNode:
        if node is None:
            node = TreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left , key)
        elif key > node.key:
            node.right = self._insert(node.right , key)
        
        return node    
    
    def _is_bst(self , node: TreeNode | None):
        if node is None:
            return True , None , None
        
        is_bst_l , min_l , max_l = self._is_bst(node.left)
        is_bst_r , min_r , max_r = self._is_bst(node.right)
        
        is_bst_node = (is_bst_l and is_bst_r and 
                       (max_l is None or node.key > max_l) and
                       (min_r is None or node.key < min_r))
        
        min_key = min(self._remove_none([min_l , node.key , min_r]))
        max_key = max(self._remove_none([max_l , node.key , max_r]))
        
        return is_bst_node , min_key , max_key
        
    def _remove_none(self , nums: list) -> list:
        return [x for x in nums if x is not None] 
            
        
    def _display(self, node: TreeNode | None, space, level):
        if node is None:
            print(space * level + 'X')
            return
        
        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return
        
        self._display(node.right , space , level+1)
        print(space*level + str(node.key))
        self._display(node.left , space , level+1)
    
    def _parse_tuple(self,data:tuple) -> TreeNode:
        
        if isinstance(data , tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = self._parse_tuple(data[0])
            node.right = self._parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        
        return node
    
    
    def _tree_to_tuple(self , node: TreeNode | None):
        if node.left is None and node.right is None:
            return node.key
        elif node.left is None:
            return (None , node.key , self._tree_to_tuple(node.right))
        elif node.right is None:
            return (self._tree_to_tuple(node.left) , node.key , None)
        else:
            return (self._tree_to_tuple(node.left) , node.key , self._tree_to_tuple(node.right))
    
    
    def _in_order_traversal(self,node: TreeNode | None) -> list:
        if node is None:
            return []
        
        return self._in_order_traversal(node.left) + [node.key] + self._in_order_traversal(node.right)
    
    
    def _pre_order_traversal(self,node: TreeNode | None) -> list:
        if node is None:
            return []
        
        return [node.key] + self._pre_order_traversal(node.left) + self._pre_order_traversal(node.right)
    
    
    def _post_order_traversal(self , node: TreeNode | None) -> list:
        if node is None:
            return []
        
        return self._post_order_traversal(node.left) + self._post_order_traversal(node.right) + [node.key]
    
    
def main():
    # tree_tuple = ((1 , 3 , None) , 2 , ((None , 3 , 4) , 5 , (6 , 7 , 8)))
    # # tree_tuple = (('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal'))
    # binary_tree = BinarySearchTree()
    # binary_tree.parse_tuple(tree_tuple)
    # pre_order_traversal = binary_tree.pre_order_traversal()
    # in_order_traversal = binary_tree.in_order_traversal()
    # post_order_traversal = binary_tree.post_order_traversal()
    # print(f"Tree Tuple: {binary_tree.tree_to_tuple()}")
    # print(f"Preorder Traversal {pre_order_traversal}")
    # print(f"Inorder Traversal {in_order_traversal}")
    # print(f"Postorder Traversal {post_order_traversal}")
    # binary_tree.display()
    # print(f"Is BST: {binary_tree.is_bst()}")
    
    bst = BinarySearchTree()
    # tree_tuple = ((1 , 3 , None) , 2 , ((None , 3 , 4) , 5 , (6 , 7 , 8)))
    # bst.parse_tuple(tree_tuple)
    
    
    data = [2, 1, 3, 4, 5, 6, 7, 8]
    for i in data:
        bst.insert(i)
    
    # print(f"Finding 6: {bst.find(6)}")
    # bst.update(6 , 6.5)
    # bst.display()
    # print(f"List all in sorted order: {bst.list_all()}")
    # print(f"Is Balanced: {bst.is_balanced()}")
    
    # data = [1,2,3,4,5,6,7,8,9]
    # bst.make_balanced_bst(data)
    
    
    print(f"Is Balanced: {bst.is_balanced()}")
    bst.balance_bst()
    bst.display()
    print(f"Is Balanced: {bst.is_balanced()}")
    
    
if __name__ == "__main__":
    main()