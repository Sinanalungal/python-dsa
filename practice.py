class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        self.root=self._insert(self.root,value)
    def _insert(self,root,value):
        if root is None:
            return TreeNode(value)
        if value<root:
            self.left=self._insert(self.left,value)
        elif value>root:
            self.right=self._insert(self.right,value)
        return root
    def delete(self,value):
        self.root=self._delete(self.root,value)
    def _delete(self,root,value):
        if root is None:
            return root
        if value<root.value:
            root.left= self._delete(root.left,value)
        elif value>root.value:
            root.right= self._delete(root.right,value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            root.value=self.minimum_node(root.right)
            root.right=self._delete(root.right,root.value)
    def minimum_node(root):
        m=root
        while m.left is not None:
            m=root.left
        return m.value  
    def contains(self,key):
        root=self.root
        while root is not None:
            if root.value==key:
                return True
            elif root.value<key:
                root=root.right
            else:
                root=root.left
        return False
    def preordertaversal(self):
        result=[]
        self._preordertraversal(self.root,result)
        return result
    def _preordertraversal(self,root,result):
        if root:
            result.append(root.key)
            self._preordertraversal(root.left,result)
            self._preordertraversal(root.right,result)

