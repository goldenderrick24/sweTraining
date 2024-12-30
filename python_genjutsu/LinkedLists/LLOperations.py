class Node(object):


    def __init__(self, data, next=None):

        self.next = next

        self.data = data


    def __str__(self):

        return self.data



class LinkedList(object):



    def __init__(self, head=None):

        self.head = head


    def __len__(self):

        curr = self.head

        counter = 0

        while curr is not None:

            counter += 1

            curr = curr.next

        return counter



    
    def prepend(self,data):
        if data is None:
            return
        
        node = Node(data, self.head)
        self.head = node
        return node

    
    def append(self, data):
        if data is None:
            return
        
        node = Node(data)
        if self.head is None:
            self.head = Node(data)
            return node
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next =node


    def find(self, data):

        if data is None:

            return None

        curr_node = self.head

        while curr_node is not None:

            if curr_node.data == data:

                return curr_node

            curr_node = curr_node.next

        return None

    def lookup(self,data):
        if data is None:
            return
        currNode = self.head

        while currNode.next is not None:
            if currNode.data == data:
                return currNode
            
            currNode = currNode.next
        
        return None
    
    def remove(self,data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = None
            return
        prev = self.head
        curr = self.head.next

        while curr is not None:
            if curr.data == data:
                prev.next = curr.next
                return
            
            prev = curr
            curr = curr.next
    
    


    def delete_alt(self, data):

        if data is None:

            return

        if self.head is None:

            return

        curr_node = self.head

        if curr_node.data == data:

            curr_node = curr_node.next

            return

        while curr_node.next is not None:

            if curr_node.next.data == data:

                curr_node.next = curr_node.next.next

                return

            curr_node = curr_node.next


    def print_list(self):

        curr_node = self.head

        while curr_node is not None:

            print(curr_node.data)

            curr_node = curr_node.next


    def get_all_data(self):

        data = []

        curr_node = self.head

        while curr_node is not None:

            data.append(curr_node.data)

            curr_node = curr_node.next

        return data