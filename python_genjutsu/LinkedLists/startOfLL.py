class MyLinkedList(LinkedList):


   

    def findLoop(self):
        if self.head is None or self.head.next is None:
            return
        
        slow, fast = self.head, self.head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break

        slow = self.head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        
        return slow