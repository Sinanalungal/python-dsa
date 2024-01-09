#BINARY SEARCH TREE

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        self.root=self._insert(self.root,value)
    def _insert(self,node,value):
        if node is None:
            return Node(value)
        if value<node.value:
            node.left=self._insert(node.left,value)
        elif value>node.value:
            node.right=self._insert(node.right,value)
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
            node.value=self.minimum_value(node.right)
            node.right=self._delete(node.right,node.value)
    def minimum_value(node):
        check=node
        while node.left is not None:
            check=check.left
        return check.value
    def preordertraversal(self):
        result=[]
        self._preordertraversal(self.root,result)
        return result
    def _preordertraversal(self,node,result):
        if node:
            result.append(node.value)
            self._preordertraversal(node.left,result)
            self._preordertraversal(node.right,result)
    def postordertraversal(self):
        result=[]
        self._postordertraversal(self.root,result)
        return result
    def _postordertraversal(self,node,result):
        if node:
            self._postordertraversal(node.left,result)
            self._postordertraversal(node.right,result)
            result.append(node.value)
    def inordertraversal(self):
        result=[]
        self._inordertraversal(self.root,result)
        return result
    def _inordertraversal(self,node,result):
        if node:
            self._inordertraversal(node.left,result)
            result.append(node.value)
            self._inordertraversal(node.right,result)
    def contains(self,value):
        check=self.root
        while check is not None:
            if check.value==value:
                return True
            elif value<check.value:
                check=check.left
            else:
                check=check.right
        return False
    
c=BinarySearchTree()
c.insert(3)
c.insert(10)
c.insert(15)
c.insert(20)
c.insert(1)
c.insert(2)
# arr=c.preordertraversal()
arr=c.inordertraversal()
print(arr)
#MIN HEAP

class MinHeap:
    def __init__(self):
        self.root=[]
    def insert(self,value):
        self.root.append(value)
        self.heapifyup()
    def heapifyup(self):
        min=len(self.root)-1
        while min>0 and self.root[(min-1)//2]>self.root[min]:
            self.root[(min-1)//2],self.root[min]=self.root[min],self.root[(min-1)//2]
            min=(min-1)//2
    def delete(self):
        if len(self.root)==0:
            return self.root
        if len(self.root)==1:
            return self.root.pop()
        value=self.root[0]
        self.root[0]=self.root.pop()
        self.heapifydown()
        return value
    def heapifydown(self,index=0):
        minnode=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        if leftchild<len(self.root) and self.root[leftchild]<self.root[minnode]:
            minnode=leftchild
        if rightchild<len(self.root) and self.root[rightchild]<self.root[minnode]:
            minnode=rightchild
        if minnode!=index:
            self.root[minnode],self.root[index]=self.root[index],self.root[minnode]
            self.heapifydown(minnode)
    def build(self,arr):
        self.root=arr
        length=len(self.root)
        for i in range((length)//2,-1,-1):
            self.heapifydown(i)

p=MinHeap()
p.insert(10)
p.insert(20)
p.insert(6)
p.insert(4)
p.insert(23)
print(p.root)

#----------------------------------------------------------------------------------------------------------------

#MAX HEAP
            
# ----------------------------------------------------------------------------------------------------------------
            
#HEAP SORT

def heapifydown(arr,n,index):
    maximum=index
    leftchild=(2*index)+1
    rightchild=(2*index)+2
    if leftchild<n and arr[leftchild]>arr[maximum]:
        maximum=leftchild
    if rightchild<n and arr[rightchild]>arr[maximum]:
        maximum=rightchild
    if maximum!=index:
        arr[maximum],arr[index]=arr[index],arr[maximum]
        heapifydown(arr,n,maximum)
def heapsort(arr):
    length=len(arr)
    for i in range((length//2)-1,-1,-1):
        heapifydown(arr,length,i)
    for i in range(length-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapifydown(arr,i,0)
    return arr

arr=heapsort([3,65,5,6,50,8,9])
print(arr)


#GRAPH
from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def add_edges(self,vertex1,vertex2,bi=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if bi: 
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
    def display(self):
        for x,y in self.graph.items():
            print (f'{x}-{y}')
    def bfs(self,startvertex):
        visited=set()
        queue=deque([startvertex])
        while queue:
            vertex=queue.popleft()
            print(vertex, end= " ")
            
            for x in self.graph[vertex]:
                if x not in visited:
                    visited.add(x)
                    queue.append(x)
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        if start not in visited:
            print(start)
            visited.add(start)
            for i in self.graph[start]:
                self.dfs(i,visited)


m=Graph()
m.add_edges(3,4)
m.add_edges(5,6,True)
m.add_edges(6,1)
m.display()
m.bfs(6)

