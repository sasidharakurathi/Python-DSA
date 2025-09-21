from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def build_tree(self, arr):
        for i in arr:
            self.root = self.insert(self.root,i)
    
    def insert(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        
        return node
    
    def pre_order_traversal(self):
        # root + left + right
        result = []
        self._pre_order_traversal(result, self.root)
        print(f'Preorder traversal : {result}')
    
    def _pre_order_traversal(self,result ,node):
        if node:
            result.append(node.data)
            self._pre_order_traversal(result, node.left)
            self._pre_order_traversal(result, node.right)
        
    
    def in_order_traversal(self):
        # left + root + right
        result = []
        self._in_order_traversal(result, self.root)
        print(f'Inorder traversal : {result}')
    
    def _in_order_traversal(self, result, node):
        if node:
            self._in_order_traversal(result, node.left)
            result.append(node.data)
            self._in_order_traversal(result, node.right)
    
    def post_order_traversal(self):
        # left + right + root
        result = []
        self._post_order_traversal(result, self.root)
        print(f'Postorder traversal : {result}')

    def _post_order_traversal(self, result, node):
        if node:
            self._post_order_traversal(result, node.left)
            self._post_order_traversal(result, node.right)
            result.append(node.data)

    def level_order_traversal(self):
        result = self._level_order_traversal()
        print(f'Levelorder traversal : {result}')
        

    def _level_order_traversal(self):
        
        if self.root is None:
            return []
        
        queue = deque()
        queue.append(self.root)
        # result = [[self.root.data]]
        result = []
        
        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left is not None:
                    queue.append(node.left)
                    # level.append(node.left.data)
                if node.right is not None:
                    queue.append(node.right)
                    # level.append(node.right.data)
            
            if level:
                result.append(level)
              
        return result
    
    
    def zig_zag_level_order_traversal(self):
        # Binary Tree Zigzag Level Order Traversal - LeetCode: 103
        ''' 
            Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
            (i.e., from left to right, then right to left for the next level and alternate between).
        '''
        result = self._zig_zag_level_order_traversal()
        print(f'ZigZag Levelorder traversal : {result}')
    
    def _zig_zag_level_order_traversal(self):
        result = []
        
        if self.root is None:
            return result
        
        queue = deque()
        queue.append(self.root)
        
        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
            if len(result) % 2 == 1:
                result.append(level[::-1])
            else:
                result.append(level)
        
        return result
        
        
    def level_order_bottom_traversal(self):
        # Binary Tree Level Order Traversal II - LeetCode: 107
        '''
            Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
            (i.e., from left to right, level by level from leaf to root).
        '''
        result = self._level_order_bottom_traversal()
        print(f'Levelorder bottom traversal : {result}')
        
    
    def _level_order_bottom_traversal(self):
        result = []
        
        if self.root is None:
            return result

        queue = deque()
        queue.append(self.root)
        
        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            result.append(level)
        
        return result[::-1]
        
    def right_side_view(self):
        # Binary Tree Right Side View - LeetCode: 199
        '''
            Given the root of a binary tree, imagine yourself standing on the right side of it, 
            return the values of the nodes you can see ordered from top to bottom.
        '''
        result = self._right_side_view()
        print(f'Right Side View : {result}')
        
    
    def _right_side_view(self):
        result = []
        
        if self.root is None:
            return result

        queue = deque()
        queue.append(self.root)
        
        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            result.append(level[-1])
    
    def left_side_view(self):
        # Binary Tree Left Side View
        '''
            Given the root of a binary tree, imagine yourself standing on the left side of it, 
            return the values of the nodes you can see ordered from top to bottom.
        '''
        result = self._left_side_view()
        print(f'Left Side View : {result}')
        
    def _left_side_view(self):
        result = []
        
        if self.root is None:
            return result

        queue = deque()
        queue.append(self.root)
        
        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.data)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            result.append(level[0])
        
        return result

    def max_height(self):
        height = self._max_height(self.root)
        print(f'Max height: {height}')
        
    def _max_height(self, node):
        if node is None:
            return 0
        
        left_height = self._max_height(node.left)
        right_height = self._max_height(node.right)
            
        return max(left_height,right_height) + 1
    
    def is_symmetric(self):
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            return node1.data == node2.data and is_mirror(node1.left,node2.right) and is_mirror(node1.right,node2.left)
        
        print(f'Is Symmetric: {is_mirror(self.root.left,self.root.right)}')
        
    def is_balanced(self):
        result = self._is_balanced(self.root)
        print(f'Is Balanced: {result if result == False else True}')
    
    def _is_balanced(self,node):
        if node is None:
            return 0
        
        left_height = self._is_balanced(node.left)
        right_height = self._is_balanced(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return max(left_height,right_height) + 1
        
        
        
# root = Node(5)
# root.left = Node(3)
# root.right = Node(1)
# root.left.right = Node(8)

# print(root.right.data)
# print(root.left.right.data)
arr = [6,4,5,1,2,8,0]
# arr = [6,4,5,1,8]
binary_tree = BinaryTree()
binary_tree.build_tree(arr)
'''
                                6
                        4               8
                1               5
            0       2
'''



binary_tree.pre_order_traversal()                           # Output: [6, 4, 1, 0, 2, 5, 8]
binary_tree.in_order_traversal()                            # Output: [0, 1, 2, 4, 5, 6, 8]
binary_tree.post_order_traversal()                          # Output: [0, 2, 1, 5, 4, 8, 6]
binary_tree.level_order_traversal()                         # Output: [[6], [4, 8], [1, 5], [0, 2]]
binary_tree.zig_zag_level_order_traversal()                 # Output: [[6], [8, 4], [1, 5], [2, 0]]
binary_tree.level_order_bottom_traversal()                  # Output: [[0, 2], [1, 5], [4, 8], [6]]
binary_tree.right_side_view()                               # Output: [6, 8, 5, 2]
binary_tree.max_height()                                    # Output: 4
binary_tree.is_symmetric()                                  # Output: False
binary_tree.is_balanced()                                   # Output: False