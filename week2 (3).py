# #Explain how you would use a stack to check for balanced parentheses in an expression.

def is_balanced(expression):
    stack=[]
    new={'{':'}' ,'(':')','[':']'}
    for i in expression:
        if i in new:
            stack.append(i)
        elif i in new.values():
            if not stack or new[stack.pop()]!=i:
                return False
    return not stack
                
# print(is_balanced('{[}'))

#-----------------------------------------------------------------------------

#Write a function to reverse the order of the elements in a queue.

def reverse(stack):
    stack1=[]
    if not isinstance(stack,list):
        raise IndexError('enter a valid stack')
    else:
        
        for i in range(len(stack)):
            stack1.append(stack.pop())
        for i in stack1:
            stack.append(i)
            

# stack=[1,2,3]
# # m=reverse('[1,2,3]')
# reverse(stack)
# print(stack)

from queue import Queue
from collections import deque

def reverse_queue(queue):
    if not isinstance(queue, Queue):
        raise TypeError("Input must be a Queue object")

    # Use a stack to temporarily hold elements
    stack = deque()

    # Dequeue elements from the queue and push them onto the stack
    while not queue.empty():
        stack.append(queue.get())

    # Enqueue elements back into the queue in reverse order
    while stack:
        queue.put(stack.pop())

#-----------------------------------------------------------------------------------------------------
        
#Write a function to reverse a string using a stack.
        
from collections import deque
def string_reverse(string):
    stack=deque()
    reversedstring=''
    for i in string:
        stack.append(i)
    for i in range(len(stack)):
        reversedstring+=stack.pop()
    return reversedstring

# string='fuck'
# print(string_reverse(string))

#---------------------------------------------------------------------

#Implement a stack that supports push, pop, and minimum element retrieval in O(1) time.

class MinStack:
    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Auxiliary stack to store the minimum element at each step
        self.min_stack = []

    def push(self, value):
        # Push the element onto the main stack
        self.stack.append(value)
        # Update the auxiliary stack with the minimum element
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None  # Stack is empty
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def get_min(self):
        if not self.min_stack:
            return None  # Stack is empty
        return self.min_stack[-1]
    
#--------------------------------------------------------------------------------------------
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   CIRCULAR QUEUE     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class CircularQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=-1
        self.rear=-1
    def is_empty(self):
        return self.front==-1
    def is_full(self):
        return (self.rear+1)%self.capacity== self.front
    def enqueue(self,data):
        if self.is_full():
            print('the queue is full')
            return
        if self.is_empty():
            self.rear=self.front=0
        else:
            self.rear=(self.rear+1)% self.capacity
        self.queue[self.rear]=data
    def dequeue(self):
        if self.is_empty():
            print('the function is already empty')
            return
        
        value=self.queue[self.front]
        if self.rear==self.front:
            self.rear=self.front=-1
        else:
            self.front=(self.front+1)%self.capacity
        return value
    def peek(self):
        if self.is_empty():
            print('there is no element in this')
            return None
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Circular Queue:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front  # Make it circular
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Make it circular

        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        item = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Update circular connection

        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        print("Circular Queue (Front to Rear):")
        current = self.front
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.front:
                break
        print()

