class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Hashtable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.items=[None]*capacity
    def _hash(self,key):
        return hash(key)%self.capacity
    def insert(self,key,value):
        new_node=Node(key,value)
        hash_index=self._hash(key)
        if self.items[hash_index] is None:
            self.items[hash_index]=new_node
            return
        else:
            n=self.items[hash_index]
            while n is not None:
                if n.key==key:
                    n.value=value
                    return
                if n.next is None:
                    break
                n=n.next
            n.next=new_node
    # def remove(self,key):
    #     hash_index=self._hash(key)
    #     if self.items[hash_index].key==key:
    #         self.items[hash_index]=self.items[hash_index].next
    #         return
    #     else:
    #         n=self.items[hash_index]
    #         while n.next is 