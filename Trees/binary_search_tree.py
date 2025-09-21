
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def build_tree(self, arr):
        for i in arr:
            self.insert(i)
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return
        
        temp = self.root
        while temp:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right
                    
    def search(self, data):
        result = self._search(data)
        if result:
            print(f'Node found: {result}')
        else:
            print(f'Node not found')
            
    
    def _search(self, data):
        if self.root is None:
            return None
        
        temp = self.root
        while temp:
            if temp.data == data:
                return temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        return None
    
    def delete(self, data):
        self.root = self._delete(self.root,data)
    
    def _delete(self, node, data):
        # If the node is None, the data is not found, return None
        if node is None:
            return None
        # If the data is less than the node's data, go left
        if data < node.data:
            node.left = self._delete(node.left, data)
        # If the data is greater than the node's data, go right
        elif data > node.data:
            node.right = self._delete(node.right, data)
        # If data is matched with the node's data
        else:
            # Node with only one child or no child
            if node.left is None:
                # Replace node with its right child
                return node.right
            elif node.right is None:
                # Replace node with its left child
                return node.left
            else:
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                min_node = self._find_min(node.right)
                # Copy the inorder successor's data to this node
                node.data = min_node.data
                # Delete the inorder successor
                node.right = self._delete(node.right, min_node.data)
        
        return node
    
    def _find_min(self,node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp
    
    def in_order_traversal(self):
        result = [] 
        self._in_order_traversal(result,self.root)
        print(f'In Order Traversal: {result}')
        
    def _in_order_traversal(self,result, node):
        if node:
            self._in_order_traversal(result,node.left)
            result.append(node.data)
            self._in_order_traversal(result,node.right)
            
    def post_order_traversal(self):
        result = [] 
        self._post_order_traversal(result,self.root)
        print(f'Post Order Traversal: {result}')
        
    def _post_order_traversal(self,result, node):
        if node:
            self._post_order_traversal(result,node.left)
            self._post_order_traversal(result,node.right)
            result.append(node.data)
            

bst = BinarySearchTree()
bst.build_tree([1,2,1.5,3,4,5,6])
bst.in_order_traversal()
bst.search(5)
bst.delete(2)
bst.in_order_traversal()