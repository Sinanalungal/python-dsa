# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.count = 1  # Add a count for duplicate elements

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self._insert(self.root, key)

#     def _insert(self, root, key):
#         if root is None:
#             return Node(key)
        
#         if key == root.key:
#             root.count += 1  # Increment count for duplicate element
#         elif key < root.key:
#             root.left = self._insert(root.left, key)
#         else:
#             root.right = self._insert(root.right, key)

#         return root

#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, root, key):
#         if root is None or root.key == key:
#             return root

#         if key < root.key:
#             return self._search(root.left, key)
#         else:
#             return self._search(root.right, key)

#     def inorder_traversal(self):
#         result = []
#         self._inorder_traversal(self.root, result)
#         return result

#     def _inorder_traversal(self, root, result):
#         if root:
#             self._inorder_traversal(root.left, result)
#             result.extend([root.key] * root.count)  # Append duplicate elements
#             self._inorder_traversal(root.right, result)

# # Example usage:
# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(4)
# bst.insert(6)
# bst.insert(8)
# bst.insert(7)  # Inserting a duplicate element

# print("In-order traversal:", bst.inorder_traversal())

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Binary search tree

# class Node:
#     def __init__(self,key):
#         self.key=key
#         self.left=None
#         self.right=None
#         self.count=1

# class BinarySearchTree:
#     def __init__(self):
#         self.root=None
#     def insert(self,key):
#         if self.root is None:
#             new_node=Node(key)
#             self.root=new_node
#         # if key=self.root

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< binary tree with queue >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #binary tree with queue

# from queue import Queue


# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.left=None
#         self.right=None

# class BinaryTree:
#     def __init__(self):
#         try:
#             root=int(input('enter the root value:'))
#         except:
#             raise ValueError ('enter a number')
#         new_node=Node(root)
#         self.root=new_node
#         self.queue=Queue()
#         self.queue.put(new_node)
#     def addingtothetree(self):
#         while not self.queue.empty():
#             p=self.queue.get()
#             try:
#                 leftchild=int(input('enter the value of left child of (if there is no left child enter -1):'))
#             except:
#                 raise ValueError ('enter a number')
            
#             if leftchild!=-1:
#                 new_node=Node(leftchild)
#                 p.left=new_node
#                 self.queue.put(new_node)
#             try:
#                 rightchild=int(input('enter the value of right child(if there is no right child enter -1):'))
#             except:
#                 raise ValueError ('enter a number')
            
#             if rightchild!=-1:
#                 new_node=Node(rightchild)
#                 p.right=new_node
#                 self.queue.put(new_node)
#     def preordertraversal(self, node =None):
#         if node is None:
#             node=self.root
#         print(node.data,'>>>>',end='')
#         if node.left is not None:
#             self.preordertraversal(node.left)
#         if node.right is not None:
#             self.preordertraversal(node.right)

        

# c=BinaryTree()
# c.addingtothetree()
# c.preordertraversal()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #binary search tree


# class TreeNode:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def insert(self,value):
#         if self.data is None:
#             self.data=TreeNode(value)
#         else:
#             if value<self.data:
#                 if self.left is None:
#                     self.left=TreeNode(value)
#                 else:
#                     self.left.insert(value)
#             elif value>self.data:
#                 if self.right is None:
#                     self.right=TreeNode(value)
#                 else:
#                     self.right.insert(value)
#     def preordertraversal(self, node=None):
#         if node is None:
#             node = self

#         if node is not None:
#             print(node.data, '>>>>', end='')
#             if node.left is not None:
#                 node.left.preordertraversal()
#             if node.right is not None:
#                 node.right.preordertraversal()



        
# c=TreeNode(9)
# # c.insert(2)
# # c.insert(10)
# # c.insert(11)
# c.preordertraversal()

