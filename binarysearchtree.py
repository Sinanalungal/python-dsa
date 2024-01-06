# class TreeNode:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None

# class BinarySearchTree:
#     def __init__(self):
#         self.root=None
#     def insert(self,value):
#         self.root=self._insert(self.root,value)
#     def _insert(self,root,value):
#         if root is None:
#             return TreeNode(value)
#         if value<root.value:
#             root.left=self._insert(root.left,value)
#         elif value>root.value:
#             root.right=self._insert(root.right,value)
#         return root
#     def contains(self,value):
#         return self._contain(self.root,value)
#     def _contains(self,root,value):
#         if root is None:
#             return False
#         if value==root.value:
#             return True
#         elif value<root.value:
#             return self._contains(root.left,value)
#         else:
#             return self._contains(root.right,value)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):  
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=TreeNode(value)
            return
        t=self.root
        while t is not None:
            r=t
            if value==t.value: 
                return
            elif value<r.value:
                t=t.left
            else:
                t=t.right
        new_node=TreeNode(value)
        if new_node.value<r.value:
            r.left=new_node
        else:
            r.right=new_node
    def contains(self,value):
        t=self.root
        while t is not None:
            if value==t.value:
                return True
            elif value<t.value:
                t=t.left
            else:
                t=t.right
        return False
    def delete(self,value):
        self.root=self._delete(self.root,value)
    def _delete(self,root,value):
        if root is None:
            return root
        if value<root.value:
            root.left=self._delete(root.left,value)
        elif value>root.value:
            root.right=self._delete(root.right,value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.value=self.min_value_right(root.right)
            root.right=self._delete(root.right,root.value)
        return root
        
    def min_value_right(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current.value
    def postordertraversal(self):
        result=[]
        self._postordertraverasl(self.root,result)
        return result
    def _postordertraverasl(self,root,result):
        if root:
            self._postordertraverasl(root.left,result)
            self._postordertraverasl(root.right,result)
            result.append(root.value)
    def preordertraversal(self):
        result=[]
        self._preordertraversal(self.root,result)
        return result
    def _preordertraversal(self,root,result):
        if root:
            result.append(root.value)
            self._preordertraversal(root.left,result)
            self._preordertraversal(root.right,result)
    def inordertraversal(self):
        result=[]
        self._inordertraversal(self.root,result)
        return result
    def _inordertraversal(self,root,result):
        if root:
            self._inordertraversal(root.left,result)
            result.append(root.value)
            self._inordertraversal(root.right,result)
        
        


# c=BinarySearchTree()
# c.insert(10)
# c.insert(20)
# c.insert(5)
# c.insert(4)
# c.insert(6)
# c.insert(30)
# c.insert(40)
# print(c.contains(30))
# c.preordertraversal()
            
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
#max heap 
            
class MaxHeap:
    def __init__(self):
        self.items=[]
    def heapifyup(self):
        index=len(self.items)-1
        while index>0 and self.items[(index-1)//2]<self.items[index]:
            self.items[(index-1)//2],self.items[index]=self.items[index],self.items[(index-1)//2]
            index=(index-1)//2
    def insert(self,value):
        self.items.append(value)
        self.heapifyup()
    def heapifydown(self,index=0):
        maximum=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        if leftchild<len(self.items) and self.items[leftchild]>self.items[maximum]:
            maximum=leftchild
        if rightchild<len(self.items) and self.items[rightchild]>self.items[maximum]:
            maximum=rightchild
        if maximum!=index:
            self.items[maximum],self.items[index]=self.items[index],self.items[maximum]
            self.heapifydown(maximum)
    def delete(self):
        if len(self.items)==0:
            return None
        if len(self.items)==1:
            return self.items.pop()
        value=self.items.pop()
        self.items[0]=self.items.pop()
        self.heapifydown()
        return value
    def buildheap(self,arr):
        self.items=arr
        n=len(self.items)
        for i in range((n//2)-1,-1,-1):
            self.heapifydown(i)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#min heap
            
class MinHeap:
    def __init__(self):
        self.items=[]
    def heapifyup(self):
        index=len(self.items)-1
        while index>0 and self.items[(index-1)//2]>self.items[index]:
            self.items[(index-1)//2],self.items[index]=self.items[index],self.items[(index-1)//2]
            index=(index-1)//2
    def insert(self,value):
        self.items.append(value)
        self.heapifyup()
    def delete(self):
        if len(self.items)==0:
            return None
        if len(self.items)==1:
            return self.items.pop()
        value=self.items.pop()
        self.items[0]=value
        self.heapifydown()
        return value
    def heapifydown(self,index=0):
        minimum=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        if leftchild<len(self.items) and self.items[leftchild]<self.items[minimum]:
            minimum=leftchild
        if rightchild<len(self.items) and self.items[rightchild]<self.items[minimum]:
            minimum=rightchild
        if index!=minimum:
            self.items[index],self.items[minimum]=self.items[minimum],self.items[index]
            self.heapifydown(minimum)
    def buildheap(self,arr):
        self.items=arr
        n=len(self.items)
        for i in range((n//2)-1,-1,-1):
            self.heapifydown(i)
c=MinHeap()
c.insert(10)
c.insert(9)
c.insert(11)
c.insert(5)
c.buildheap([8,3,4,75,32,1])
print(c.items)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  heap sort   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#heap sort

def heapify(arr,n,index):
    maxi=index
    leftchild=(2*index)+1
    rightchild=(2*index)+2
    if leftchild<n and arr[leftchild]>arr[maxi]:
        maxi=leftchild
    if rightchild<n and arr[rightchild]>arr[maxi]:
        maxi=rightchild
    if index!=maxi:
        arr[index],arr[maxi]=arr[maxi],arr[index]
        heapify(arr,n,maxi)

def heapsort(arr):
    n=len(arr)
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    return arr

arr=heapsort([3,65,5,6,50,8,9])
print(arr)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Trie Implementation   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,value):
        node=self.root
        for i in value:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.is_end=True    
    def search(self,value):
        node=self.root
        for i in value:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.is_end
    def prefix_search(self,prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return []
            node=node.children[i]
        result=[]
        self.collected_words(node,result,prefix)
        return result

    def collected_words(self,node,result,currentword):
        if node.is_end:
            result.append(currentword)
        for x,y in node.children.items():
            self.collected_words(y,result,currentword+x)
    