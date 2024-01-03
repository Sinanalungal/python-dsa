# # #SINGLY LINKED LIST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def print__LL(self):
#         if self.head is None:
#             print('Linked list is Empty')
#         else:
#             n=self.head
#             while n is not None:   #i want to stop if the reference is null .we giving reference to the n
#                 print(n.data,'--->',end=' ')
#                 n=n.ref
#     def reverse_ll(self):
#         print()
#         prev=None
#         current=self.head
#         while current is not None:
#             next_node=current.ref
#             current.ref=prev
#             prev=current
#             current=next_node
#         self.head=prev
    
#     def add_begin(self,data):      
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node
  
#     def add_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n=self.head
#             while n.ref is not None:
#                 n=n.ref                                                                                                             
#             n.ref=new_node
#     def add_after(self,data,x):
#         n=self.head
#         while n is not None:
#             if n.data==x:
#                 break
#             else:
#                 n=n.ref
#         if n is None:
#             print('node is not present in the LL')
#         else:
#             new_node=Node(data)
#             new_node.ref=n.ref
#             n.ref=new_node 
#     def add_before(self,data,x):
#         if self.head is None:
#             print('Linked List is Empty')
#             return
#         if self.head.data==x:
#             new_node=Node(data)
#             new_node.ref=self.head
#             self.head=new_node
#             return
#         else:
#             n=self.head
#             while n.ref is not None:
#                 if n.ref.data==x:
#                     break
#                 n=n.ref
#             if n.ref is None:
#                 print('Node is not found!')
#             else:
#                 new_node=Node(data)
#                 new_node.ref=n.ref
#                 n.ref=new_node
#     def insert_empty(self,data):
#         if self.head is None:
#             new_node=Node(data)
#             self.head=new_node
#         else:
#             print('linked list is not empty')
#     def delete_begin(self):
#         if self.head is None:
#             print('you cannot perform this operation')
#         else:
#             self.head=self.head.ref
#     def delete_end(self):
#         if self.head is None:
#             print('you cannot perform this operation')
#         elif self.head.ref is None:
#             self.head=None
#         else:
#             n=self.head
#             while n.ref.ref is not None:   
#                 n=n.ref
#             n.ref=None
#     def delete_by_value(self,x):
#         if self.head is None:
#             print('Cannot delete when Linked list is Empty')
#             return
#         if self.head.data==x:
#             self.head=self.head.ref
#             return
#         else:
#             n=self.head
#             while n.ref is not None:
#                 if n.ref.data==x:
#                     break
#                 n=n.ref
#             if n.ref is None:
#                 print('Nod is not present')
#             else:
#                 n.ref=n.ref.ref
# #REMOVE DUPLICATES FROM SORTED LINKED LIST
#     def remove_duplicates(self):
#         if self.head is None:
#             print('The linked list is empty')
#         else:
#             n=self.head
#             while n.ref is not None:
#                 if n.data == n.ref.data:
#                     n.ref=n.ref.ref
#                 else:
#                     n=n.ref
#     def appending(self,Linked):
#         if self.head is None:
#             self.head=Linked.self.head
#             Linked.self.head=None
#         else:
#             n=self.head
#             while n.ref is not None:
#                 n=n.ref
#             n.ref=Linked.self.head
#             Linked.self.head=None
#     def middle_node(self):
#         if self.head==None:
#             print('There is no node in this linked list')
#         else:
#             slow=self.head
#             fast=self.head
#             while fast is not None and fast.ref is not None:
#                 slow=slow.ref
#                 fast=fast.ref.ref
#             return print('middle node is ',slow.data)
#     def delete_value_by_index(self,*kwargs):
#         print()
#         if self.head is None:
#             print('The linked list is empty')
#         else:
#             count=0
#             while n.ref is not None:
#                 if (count+1) in kwargs:
#                     n.ref=n.ref.ref
#                 else:
#                     n=n.ref
#                 count+=1
#             if 0 in kwargs:
#                     self.head=self.head.ref
            
        
        

#ARRAY TO LINKED LIST

# def array_to_linked_list(arr):
#     L1=LinkedList()
#     for i in arr:
#         L1.add_end(i)
#     # L1.remove_duplicates()
#     # L1.middle_node()
#     L1.print__LL()
#     L1.delete_value_by_index(0,1,50,3)
#     L1.print__LL()



# array_to_linked_list([1,1,1,1,2,2,3,3,4,5,6,6])





# L1=LinkedList()
# L1.add_begin(10)
# L1.add_begin(20)
# L1.add_begin(30)
# L1.add_begin(40)
# L1.delete_by_value(20)
# L1.print__LL()
# L1.reverse_ll()
# L1.middle_node()
# L1.print__LL()

#------------------------------------------------------------------

# #DOUBLY LINKED LIST

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.pref=None
#         self.nref=None

# class DoublyLL:
#     def __init__(self):
#         self.head=None
#     def print_LL(self):
#         if self.head is None:
#             print('Linked List is Empty')
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data,'---->',end='')
#                 n=n.nref
#     def print_LL_reverse(self):
#         print()
#         if self.head is None:
#             print('Linked List is Empty')
#         else:
#             n=self.head
#             while n.nref is not None:
#                 n=n.nref
#             while n is not None:
#                 print(n.data,'---->',end='')
#                 n=n.pref
#     def insert_empty(self,data):
#         if self.head is None:
#             new_node=Node(data)
#             self.head=new_node
#         else:
#             print('linked List is not empty')
#     def add_begin(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             new_node.nref=self.head
#             self.head.pref=new_node
#             self.head=new_node
#     def add_end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             n=self.head
#             while n.nref is not None:
#                 n=n.nref
#             new_node.pref=n
#             n.nref=new_node
#     def add_after(self,data,x):
#         if self.head is None:
#             print('Linked List is empty')
#         else:
#             n=self.head
#             while n is not None:
#                 if n.data==x:
#                     break
#                 n=n.nref
#             if n is None:
#                 print("Give node is node present in LL")
#             else:
#                 new_node=Node(data)
#                 new_node.nref=n.nref
#                 new_node.pref=n
#                 if n.nref is not None:
#                     n.nref.pref=new_node
#                 n.nref=new_node
#     def add_before(self,data,x):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n=self.head
#             while n is not None:
#                 if n.data==x:
#                     break
#                 n=n.nref
#             if n is None:
#                 print('Given node is not in the linked list')
#             else:
#                 new_node=Node(data)
#                 new_node.nref=n
#                 new_node.pref=n.pref
#                 if n.pref is not None:
#                     n.pref.nref=new_node
#                 else:
#                     self.head=new_node
#                 n.pref=new_node
#     def delete_begin(self):
#         if self.head is None:
#             print("DLL is empty can't delete")
#             return
#         if self.head.nref is None:
#             self.head=None
#             print('linked list is empty after deleting the node')
#         else:
#             self.head=self.head.nref
#             self.head.pref=None
#     def delete_end(self):
#         if self.head is None:
#             print("DLL is empty can't delete")
#             return
#         if self.head.nref is None:
#             self.head=None
#         else:
#             n=self.head
#             while n.nref is not None:
#                 n=n.nref
#             n.pref.nref=None
#     def delete_by_value(self,data,x):
#         if self.head is None:
#             print('Linked List is empty')
#             return
#         if self.head.nref is None:
#             if self.head.data == x:
#                 self.head = None
#             else:
#                 print('x is not present the DLL')
#             return 
#         if self.head.data==x:
#             self.head=self.head.nref
#             self.head.pref=None
#             return 
#         n=self.head
#         while n.nref is not None:
#             if n.data==x:
#                 break
#             n=n.nref
#         if n.nref is not None:
#             n.pref.nref=n.nref
#             n.nref.pref=n.pref
#         else:
#             if n.data==x:
#                 n.pref.nref=None
#             else:
#                 print('x is not present in the DLL')

# #REVERSING OF DOUBLY LINKED LIST    
#     def reverse_list(self):
#         print()
#         if self.head is None:
#             print('the ll is empty')
#             return
        
#         current=self.head
#         while current is not None:
#             prev=current
#             nextone=current.nref
#             current.nref,current.pref=current.pref,current.nref
#             current=nextone
#         self.head=prev






            

# dl1=DoublyLL()
# # dl1.insert_empty(10)
# dl1.add_begin(4)
# dl1.add_end(100)
# dl1.add_end(1000)
# dl1.add_before(20,4)
# # dl1.delete_end()
# # dl1.delete_begin()
# dl1.print_LL()
# dl1.reverse_list()
# dl1.print_LL()

# dl1.print_LL_reverse()

#---------------------------------------------------------------------------------

# #CIRCULAR SINGLY LINKED LIST

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class circular__LL:
    def __init__(self):
        self.head=None
    def print__ll(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n.ref:
                print(n.data,'----->',end='')
                n=n.ref
                if self.head==n:
                    break
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.ref=new_node
            return
        if self.head is not None:
            new_node.ref=self.head
            n=self.head
            while n.ref:
                if n.ref == self.head:
                    break
                else:
                    n=n.ref
            n.ref=new_node
            self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=new_node
            self.head=new_node
            return
        if self.head is not None:
            n=self.head
            while n.ref:
                if n.ref==self.head:
                    break
                else:
                    n=n.ref
            new_node.ref=self.head
            n.ref=new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            new_node.ref=new_node
            self.head=new_node
        else:
            print('circular LL is not empty')
    def add_before(self,data,x):
        if self.head is None:
            print('Circular LL is empty')
            return
        if self.head.data==x:
            if self.head.data==x:
                new_node=Node(data)
                new_node.ref=self.head
                n=self.head
                while n.ref:
                    if n.ref==self.head:
                        break
                    else:
                        n=n.ref
                n.ref=new_node
                self.head=new_node
            
        else:
            n=self.head
            while n.ref is not self.head:
                if n.ref.data ==x:
                    new_node=Node(data)
                    new_node.ref=n.ref
                    n.ref=new_node
                    break
                
                n=n.ref
            if n.ref==self.head:
                print('there is no node in this LL')
                return
                
    def add_after(self,data,x):
        if self.head is None:
            print('The linked list is empy')
        else:
            n=self.head
            while n:
                if n.data==x:
                    new_node=Node(data)
                    new_node.ref,n.ref=n.ref,new_node 
                if n.ref==self.head:
                    break
                n=n.ref
    def delete_begin(self):
        if self.head is None:
            print('linked list is Empty')
        else:
            n=self.head
            while n:
                if n.ref==self.head:
                    n.ref=self.head.ref
                    break
                else:
                    n=n.ref
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print('linked list is Empty')
        if self.head.ref ==self.head:
            self.head=None
        else:
            n=self.head
            while n:
                if n.ref.ref == self.head:
                    n.ref=self.head
                    break
                else:
                    n=n.ref

            
                




c1=circular__LL()
c1.add_end(10)
c1.add_end(20)
c1.add_end(30)


c1.add_before(25,10)
c1.add_after(100,20)
# c1.delete_begin()
# c1.delete_begin()
# c1.delete_end()
# c1.delete_end()


# c1.add_end(20)
# c1.add_begin(5)
# c1.add_end(30)
# c1.insert_empty(100)

c1.print__ll()

#---------------------------------------------------------------------------------------------------