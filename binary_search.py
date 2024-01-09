class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTable:
    def __init__(self) -> None:
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
        if value<node.left:
            node.left=self._delete(node.left,value)
        elif value>node.right:
            node.right=self.delete(node.right,value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node.value=self.minvalue(node.right)
            node.right=self._delete(node.right,node.value)
        return node
    def minvalue(self,node):
        treenode=node
        while treenode.left is not None:
            treenode=treenode.left
        return treenode.value
    def preordertraversal(self):
        result=[]
        self._preordertraversal(self.root,result)
        return result
    def _preordertraversal(self,node,result):
        result.append(node.value)
        self._preordertraversal(node.left,result)
        self._preordertraversal(node.right,result)
    def closest_value_to_the_target(self, target):
        closest = self.root.value
        current = self.root
        while current:
            if abs(current.value - target) < abs(closest - target):
                closest = current.value
            if current.value == target:
                return target
            elif current.value > target:
                current = current.left
            else:
                current = current.right

        return closest

#node not finished

#max heap
class MaxHeap:
    def __init__(self) -> None:
        self.root=[]
    def insert(self,value):
        self.root.append(value)
        self.heapifyup()
    def heapifyup(self):
        max=len(self.root)-1
        while max>0 and self.root[(max-1)//2]<self.root[max]:
            self.root[(max-1)//2],self.root[max]=self.root[max],self.root[(max-1)//2]
            max=(max-1)//2
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
        maxnode=index
        childleft=(2*index)+1
        childright=(2*index)+2
        if childleft<len(self.root) and self.root[childleft]>self.root[maxnode]:
            maxnode=childleft
        if childright<len(self.root) and self.root[childright]>self.root[maxnode]:
            maxnode=childright
        if index!=maxnode:
            self.root[index],self.root[maxnode]=self.root[maxnode],self.root[index]
            self.heapifydown(maxnode)
    def build(self,arr):
        self.root=arr
        n=len(self.root)
        for i in range((n//2)-1,-1,-1):
            self.heapifydown(i)

# p=MaxHeap()
# p.insert(10)
# p.insert(20)
# p.insert(6)
# p.insert(4)
# p.insert(23)
# p.delete()
# p.build([78,2,4,6,86,104])
# print(p.root)


#min heap
            
class MinHeap:
    def __init__(self) -> None:
        self.root=[]
    def insert(self,value):
        self.root.append(value)
        self.heapifyup()
    def heapifyup(self):
        n=len(self.root)-1
        while n>0 and self.root[(n-1)//2]>self.root[n]:
            self.root[(n-1)//2],self.root[n]=self.root[n],self.root[(n-1)//2]
            n=(n-1)//2
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
        minindex=index
        leftchild=(2*index)+1
        rightchild=(2*index)+2
        if leftchild<len(self.root) and self.root[leftchild]<self.root[minindex]:
            minindex=leftchild
        if rightchild<len(self.root) and self.root[rightchild]<self.root[minindex]:
            minindex=rightchild
        if minindex!=index:
            self.root[index],self.root[minindex]=self.root[minindex],self.root[index]
            self.heapifydown(minindex)
    def build(self,arr):
        self.root=arr
        n=len(self.root)-1
        for i in range((n//2)-1,-1,-1):
            self.heapifydown(i)



# p=MinHeap()
# p.insert(10)
# p.insert(20)
# p.insert(6)
# p.insert(4)
# p.insert(23)
# p.delete()
# # p.build([78,2,4,6,86,104])
# print(p.root)
            
def heapifydown(arr,n,i):
    maxi=i
    childleft=(2*i)+1
    childright=(2*i)+2
    if childleft<n and arr[childleft]>arr[maxi]:
        maxi=childleft
    if childright<n and arr[childright]>arr[maxi]:
        maxi=childright
    if maxi!=i:
        arr[maxi],arr[i]=arr[i],arr[maxi]
        heapifydown(arr,n,maxi)

def heapsort(arr):
    length=len(arr)
    for i in range((length//2)-1,-1,-1):
        heapifydown(arr,length,i)
    for i in range(length-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifydown(arr,i,0)
    return arr

# arr=heapsort([3,65,5,6,50,8,9])
# print(arr)

#GRAPH

from collections import deque
class Graph:
    def __init__(self) -> None:
        self.graph={}
    def addvertex(self,value):
        if value not in self.graph:
            self.graph[value]=[]
    def add_edges(self,vertex1,vertex2,bi=False):
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
    def bfs(self,startvertex):
        vistited=set()
        queue=deque([startvertex])
        while queue:
            vertex=queue.popleft()
            print(vertex,end=' ')
            for x in self.graph[vertex]:
                if x not in vistited:
                    vistited.add(x)
                    queue.append(x)
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        if start not in visited:
            print(start)
            visited.add(start)
            for x in self.graph[start]:
                self.dfs(x,visited)
# m=Graph()
# m.add_edges(3,4)
# m.add_edges(5,6,True)
# m.add_edges(6,1)
# m.display()
# m.bfs(6)
                
class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self) -> None:
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
    
    