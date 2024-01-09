class TreeNode:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None
    def insert(self,value):
        self.root=self._insert(self.root,value)
    def _insert(self,node,value):
        if node is None:
            return TreeNode(value)
        if value<node.value:
            node.left=self._insert(node.left,value)
        elif value>node.value:
            node.right=node._insert(node.right,value)
        return node
    def delete(self,value):
        self.root=self._delete(self.root,value)
    def _delete(self,node,value):
        if node is None:
            return node
        if value<node.value:
            node.left=self._delete(node.left,value)
        elif value>node.value:
            node.right=self._delete(node.right,value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node.value=self.successor(node.right)
            node.right=self._delete(node.right,node.value)
            return node
    def successor(self,node):
        start=node
        while start.left is not None:
            start=start.left
        return node.value
    def preordertraversal(self):
        result=[]
        self._preordertraversal(self.root,result)
        return result
    def _preordertraversal(self,node,result):
        if node:
            result.append(node.value)
            self._preordertraversal(node.left,result)
            self._preordertraversal(node.right,result)
    def closestvalue(self,target):
        closest=self.root.value
        current=self.root
        while current:
            if abs(current.value-target)<abs(closest-target):
                closest=current.value
            if current.value==target:
                return target
            elif current.value>target:
                current=current.left
            else:
                current=current.right
        return closest
    def validate(self,root):
        result=[]
        def inordertraversal(node):
            if node:
                inordertraversal(node.left)
                result.append(node.value)
                inordertraversal(node.right)
        inordertraversal(root)
        for i in range(1,len(result)):
            if result[i]<result[i-1]:
                return False
        return True
    
class MaxHeap:
    def __init__(self) -> None:
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapifyup()
    def heapifyup(self):
        n=len(self.heap)-1
        while n>0 and self.heap[(n-1)//2]<self.heap[n]:
            self.heap[(n-1)//2],self.heap[n]=self.heap[n],self.heap[(n-1)//2]
            n=(n-1)//2
    def delete(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        value=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapifydown()
        return value
    def heapifydown(self,index=0):
        maxi=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        if leftchild<len(self.heap) and self.heap[leftchild]>self.heap[maxi]:
            maxi=leftchild
        if rightchild<len(self.heap) and self.heap[rightchild]>self.heap[maxi]:
            maxi=rightchild
        if index!=maxi:
            self.heap[index],self.heap[maxi]=self.heap[maxi],self.heap[index]
            self.heapifydown(maxi)
    def build(self,arr):
        self.heap=arr
        n=len(arr)
        for i in range((n//2)-1,-1,-1):
            self.heapifydown(i)

#heap sort
            
def heapifydown(arr,n,i):
    maxi=i
    leftchild=(2*i)+1
    rightchild=(2*i)+2
    if leftchild<n and arr[leftchild]>arr[maxi]:
        maxi=leftchild
    if rightchild<n and arr[rightchild]>arr[maxi]:
        maxi=rightchild
    if maxi!=i:
        arr[maxi],arr[i]=arr[i],arr[maxi]
        heapifydown(arr,n,maxi)
def heapsort(arr):
    n=len(arr)
    for i in range((n//2)-1,-1,-1):
        heapifydown(arr,i,0)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapifydown(arr,i,0)
    return arr
# arr=heapsort([10,40,30,2,4,6,7])
# print(arr)

#trie
class TrieNode:
    def __init__(self) -> None:
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
    # def prefixsearch(self,prefix):
    #     node=self.root
    #     for i in prefix:
    #         if i not in node.children:
    #             return []
    #         node=node.children[i]
    #     result=[]
    #     self.collectedwords(node,result,prefix)

    # def collectedwords(self,node,result,currentword):
    #     if node.is_end:
    #         result.append(currentword)
    #     for x,y in node.children.items():
    #         self.collectedwords(y,result,currentword+x)
    def prefixsearch(self,prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return []
            node=node.children[i]
        result=[]
        self.collectedwords(node,result,prefix)
        return result
    def collectedwords(self,node,result,currentword):
        if node.is_end:
            result.append(currentword)
        for x,y in node.children.items():
            self.collectedwords(y,result,currentword+x)


#Graph

from collections import deque       
class Graph:
    def __init__(self) -> None:
        self.graph={}
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def addedges(self,vertex1,vertex2,bi=False):
        self.addvertex(vertex1)
        self.addvertex(vertex2)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if bi:
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
    def display(self):
        for x,y in self.graph.items():
            print(f'{x}-{y}')
    # def bfs(self,startvertex):
    #     visited=set()
    #     queue=deque([startvertex])
    #     while queue:
    #         vertex=deque.popleft()
    #         print(vertex,end='  ')
    #         for i in self.graph[vertex]:
    #             if i not in visited:
    #                 visited.add(i)
    #                 queue.append(i)
    # def dfs(self,start,visited=None):
    #     if visited==None:
    #         visited=set()
    #     if start not in visited:
    #         print(start)
    #         visited.add(start)
    #         for i in self.graph[start]:
    #             self.dfs(i,visited)
    def bfs(self,startvertex):
        visited=set()
        queue=deque([startvertex])
        while queue:
            vertex=queue.popleft()
            print(vertex,'  ')
            for i in self.graph[vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
    def dfs(self,start,visted=None):
        if visted is None:
            visted=set()
        if start not in visted:
            print(start,'  ')
            visted.add(start)
            for i in self.graph[start]:
                self.dfs(i,visted)

