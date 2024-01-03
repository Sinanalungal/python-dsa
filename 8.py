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

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
