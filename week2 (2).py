#Stack-list

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
            self.items.append(data)
    def pop(self):
        if len(self.items)<1:
            raise IndexError('Trying to pop from an empty stack')
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items)<1:
            raise IndexError('Trying to access from an empty stack')
        else:
            return self.items[-1]
    def isEmpty(self):
        if len(self.items)<1:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)
    
# s=Stack()
# # print(s.isEmpty())
# # print(s.size())
# # s.push(10)
# # print(s.peek())



#and another one with list simple append and pop using,that not a correct one

#-------------------------------------------------------------------------------------------------------------------------------

# #stack-linked list

# class stacknode:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Stack:
#     def __init__(self):
#         self.top=None
    

# class StackNode:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         new_node=StackNode(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n=self.head
#             while n.next is not None:
#                 n=n.next
#             n.next=new_node
#     def pop(self):
#         if self.head is None:
#             return print('There is no element in the stack')
#         elif self.head.next is None:
#             self.head=None
#         else:
#             n=self.head
#             while n.next.next is not None:
#                 n=n.next
#             val=n.next.data
#             n.next=None
#             return print(val)
#     def peek(self):
#         if self.head is None:
#             return print('there is no element in the stack')
#         else:
#             n=self.head
#             while n.next is not None:
#                 n=n.next
#             return print(n.data)
#     def isEmpty(self):
#         if self.head is None:
#             return print(True)
#         else:
#             return print(False)
        
# s=Stack()
# # s.isEmpty()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# # s.isEmpty()
# s.pop()
# # s.peek()

#---------------------------------------------------------------------

# using modules-collection -deque

# from collections import deque

# stack=deque()
# stack.append(10)
# # print(stack.pop())
# print(not stack)   #it gives True when stack is empty else True

#---------------------------------------

# using modules-queue -lifoqueue
# from queue import LifoQueue

# stack=LifoQueue()
# stack.put(10)
# print(stack.get(timeout=1))


#-----------------------------------------------------------------------------


#Queue

# queue = []
# queue.append(1)  # enqueue
# queue.append(2)
# dequeued_element = queue.pop(0)  # dequeue

#-----------

# from collections import deque

# queue = deque()
# queue.append(1)  # enqueue
# queue.append(2)
# dequeued_element = queue.popleft()  # dequeue

#----------------------------


# from queue import Queue   #it able to use in multitreaded environment.because of it is a thread-safe queue implementation

# queue = Queue()
# queue.put(1)  # enqueue
# queue.put(2)
# dequeued_element = queue.get()  # dequeue

#-------------------------------------

#Queue using list

# class Queue:
#     def __init__(self):
#         self.items=[]
#     def enqueue(self,data):
#         self.items.append(data)
#     def dequeue(self):
#         if not self.items:
#             raise IndexError('there is no element in the queue')
#         else:
#             return print(self.items.pop(0))
#     def isEmpty(self):
#         return len(self.items)==0
#         # if not self.items:
#         #     return True
#         # else:
#         #     return False
#     def peek(self):
#         return print(self.items[0])
    
#---------------------------------------------------------------------------

#QUEUE IMPLEMENTATION USING LINKED LIST

# class QueueNode:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
    


#-----------------------------------------------------------
#HASH TABLE

# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None

# class HashTable:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         # self.size=0
#         self.table=[None]*capacity
#     def _hash(self,key):
#         return hash(key) % self.capacity
#     def insert(self,key,value):
#         hashed_value=self._hash(key)
#         new_node=Node(key,value)
#         if self.table[hashed_value] is None:
#             self.table[hashed_value]=new_node
#             # self.size+=1
#             return
#         else:
#             n=self.table[hashed_value]
#             while n is not None:
#                 if n.key==key:
#                     n.value=value
#                     return 
#                 if n.next is None:
#                     break
#                 n=n.next
#             n.next=new_node
#             # self.size+=1
#     def search(self,key):
#         hashed_value=self._hash(key)
#         n=self.table[hashed_value]
#         while n is not None:
#             if n.key==key:
#                 return n.value
#             n=n.next
#         raise KeyError(f'{key} is not available in this hash table')
#     def remove(self,key):
#         hashed_value=self._hash(key)
#         if self.table[hashed_value].key==key:
#             self.table[hashed_value]=self.table[hashed_value].next
#             self.size-=1
#             return
#         else:
#             n=self.table[hashed_value]
#             while n.next is not None:
#                 if n.next.key==key:
#                     n.next=n.next.next
#                     self.size-=1
#                     return 
#                 n=n.next
#             raise KeyError(f'{key} is not available in this hash table')
#     def __len__(self):
#         return self.size
#     def __contains__(self,key):
#         try:
#             self.search(key)
#             return True
#         except:
#             return False
#     def __str__(self):
#         elements=[]
#         for i in range(self.capacity):
#             n=self.table[i]
#             while n is not None:
#                 elements.append((n.key,n.value))
#                 n=n.next
#         return print(elements)
    

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.items=[None]*capacity
    def is_empty(self):
        flag=0
        i=0
        n=self.items[0]
        while i<self.capacity:
            if n==None:
                i=i+1
            else:
                flag=1
                break
        if flag==0:
            return True
        else:
            return False
    def _hash(self,key):
        return hash(key)%self.capacity
    def insert(self,key,value):
        hashed_index=self._hash(key)
        new_node=Node(key,value)
        if self.items[hashed_index] is None:
            self.items[hashed_index]=new_node
            return
        else:
            n=self.items[hashed_index]
            while n is not None:
                if n.key==key:
                    n.value=value
                    return
                if n.next is None:
                    break
                n=n.next
            n.next=new_node
    def remove(self,key):
        hashed_index=self._hash(key)
        if self.items[hashed_index] is None:
            print('there is no such value in this hash table')
            return
        elif self.items[hashed_index].key==key:
            self.items[hashed_index]=self.items[hashed_index].next
            return 
        else:
            n=self.items[hashed_index]
            while n.next is not None:
                if n.next.key==key:
                    n.next=n.next.next
                    return
                n=n.next
            raise f"there is no value key in this"
    def search(self,key):
        hashed_index=self._hash(key)
        n=self.items[hashed_index]
        while n is not None:
            if n.key==key:
                return n.value
            n=n.next
        raise f'there is no key in this'
                  
h=HashTable(3)
print(h.is_empty())
                

                

# h=HashTable(10)
# h.insert('first',1)
# h.insert('second',2)
# h.insert('third',3)
# h.insert('second',10)
# # h.remove('second')
# h.__str__()
# print(len(h))
# print('fourth' in h)
# # print(h.search('second'))

#-------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  STACK   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#FIXED

# class FixedSizeStack:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.items=[None]*capacity
#         self.top=-1
#     def is_empty(self):
#         return self.top==-1
#     def is_full(self):
#         return self.top == self.capacity-1
#     def push(self,data):
#         if not self.is_full():
#             self.top+=1
#             self.items[self.top]=data
#         else:
#             raise IndexError('the stack is already full')
#     def pop(self):
#         if not self.is_empty():
#             pop_value=self.items[self.top]
#             self.top-=1
#             return pop_value
#         else:
#             raise IndexError('the stack is Empty')
#     def peek(self):
#         if not self.is_empty:
#             value=self.items[self.top]
#             return value
#         else:
#             raise IndexError('the stack is empty')
#     def size(self):
#         return self.top+1

#DYNAMIC

# class DynamicSizedStack:
#     def __init__(self):
#         self.items=[]
#     def is_empty(self):
#         return len(self.items)==0
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         if not self.is_empty():
#             value=self.items.pop()
#             return value
#         else:
#             raise IndexError('stack is empty')
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError('stack is empty')
#     def size(self):
#         return len(self.items)

#DEQUE

# from collections import deque

# class Stack:
#     def __init__(self):
#         self.stack=deque()
#     def is_empty(self):
#         return len(self.stack)==0
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         if not self.is_empty():
#             self.stack.pop()
#         else:
#             raise IndexError('stack is empty')
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             raise IndexError('stack is empty')


#LIFOQUEUE

# from queue import LifoQueue

# class Stack:
#     def __init__(self):
#         self.stack=LifoQueue()
#     def isempty(self):
#         return self.stack.empty()
#     def push(self,data):
#         self.stack.put(data)
#     def pop(self):
#         if not self.isempty():
#             return self.stack.get()
#         else:
#             raise IndexError('stack is empty')
#     def peek(self):
#         if not self.isempty():
#             data=self.stack.get()
#             self.stack.put(data)
#             return data
#         else:
#             raise IndexError('stack is empty')
#     def size(self):
#         return self.stack.qsize()


#LINKED LIST-dynamic stack:

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Stack:
#     def __init__(self):
#         self.top=None
#     def isEmpty(self):
#         return self.top==None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.top
#         self.top=new_node
#     def pop(self):
#         if not self.isEmpty():
#             data=self.top.data
#             self.top=self.top.next
#             return data
#         else:
#             raise IndexError('stack is empty')
#     def peek(self):
#         if not self.isEmpty():
#             return self.top.data
#         else:
#             raise IndexError('stack is empty')
#     def size(self):
#         n=self.top
#         count=0
#         while n is not None:
#             count+=1
#             n=n.next
#         return count

# #fixed stack

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class FixedSizeStack:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.head=None
#         self.size=0
#     def empty(self):
#         return self.size==0
#     def isfull(self):
#         return self.capacity==self.size
#     def push(self,data):
#         if not self.isfull():
#             new_node=Node(data)
#             new_node.next=self.head
#             self.head=new_node
#             self.size+=1
#         else:
#             raise IndexError('stack is full')
#     def pop(self):
#         if not self.empty():
#             data=self.head.data
#             self.head=self.head.next
#             self.size-=1
#             return data
#         else:
#             raise IndexError('stack is empty')
#     def peek(self):
#         if not self.empty():
#             return self.head.data
#         else:
#             return IndexError('stack is empty')
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< QUEUE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Queue:
#     def __init__(self):
#         self.items=[]
#         self.front=None
#         self.rear=None
#     def isempty(self):
#         return len(self.items)==0
#     def enqueue(self,data):
#         if self.isempty():
#             self.items.append(data)
#             self.front=data
#             self.rear=data
#         else:
#             self.items.append(data)
#             self.rear=data
#     def dequeue(self):
#         if not self.isempty():
#             value=self.items.pop(0)
#             if len(self.items)>0:
#                 self.front=self.items[0]
#             else:
#                 self.front=None
#             return value
#         else:
#             raise IndexError('stack is empty')
    
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue=deque()
#     def isempty(self):
#         return len(self.queue)==0
#     def enqueue(self,data):
#         self.queue.append(data)
#     def dequeue(self):
#         if not self.isempty():
#             return self.queue.popleft()
#         else:
#             raise IndexError('the stack is empty')
#     def peek(self):
#         if not self.isempty():
#             return self.queue[0]
#         else:
#             raise IndexError('the stack is empty')

# from queue import Queue

# class Queuee:
#     def __init__(self):
#         self.queue=Queue()
#     def isempty(self):
#         return self.queue.empty()
#     def enqueue(self,data):
#         self.queue.put(data)
#     def dequeue(self):
#         if not self.isempty():
#             return self.queue.get()
#         else:
#             raise IndexError('the stack is empty')
#     def peek(self):
#         if not self.isempty():
#             return self.queue.queue[0]
#         else:
#             raise IndexError('the stack is empty')