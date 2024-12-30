# class MyLinkedList(LinkedList):


#     def kth_to_last_elem(self, k):

#         if self.head is None:

#             return None

#         fast = self.head

#         slow = self.head


#         # Give fast a headstart, incrementing it

#         # once for k = 1, twice for k = 2, etc

#         for _ in range(k):

#             fast = fast.next

#             # If k >= num elements, return None

#             if fast is None:

#                 return None


#         # Increment both pointers until fast reaches the end

#         while fast.next is not None:

#             fast = fast.next

#             slow = slow.next

#         return slow.data


"""
algorithm

two ptrs fast and slow
give fast a headstart incrementing it once if k = 1, 
twice if k =2
increment both ptrs until fast reaches end
return value of slow
"""

class LL(object):

    def __init__(self, data, head, next=None,):
        self.data = data
        self.next = next
        

class myLL(LL):

    def __init__(self):
        self.head = None
        

    def kthToLast(self, k):
        if self.head is None:
            return None
        
        fast = self.head
        slow = self.head

        for _ in range(k):
            # Give fast a headstart, incrementing it
            fast = fast.next
            if fast is None:
                return None
        # Increment both pointers until fast reaches the end   
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        return slow.data
        