# def binary_search(arr,key,h,l=0):
#     if l<=h:
#         mid=(l+h)//2
#         if arr[mid]==key:
#             return f"the position of the key is {mid}"
#         elif key<arr[mid]:
#             return binary_search(arr,key,mid-1,l)
#         else:
#             return binary_search(arr,key,h,mid+1)
#     else:
#         return 'there is no key in this'
    
# print(binary_search([1,2,3,4,5],2,4,0))

# def insert_end(self,data):
#     if self.head is None:
#        return print('LL is emopty')
#     else:   
#         n=self.head
#         while n.next_ref is not None:
#             n=n.next_ref
#         new_node=Node(data)
#         new_node.previous_ref=n
#         new_node.next_ref=None
#         n.next_ref=new_node
d=dict([1,2,3,3,1])

print(d)
    

        
       


