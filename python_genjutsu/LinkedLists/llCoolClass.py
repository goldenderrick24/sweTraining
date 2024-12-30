class Node:
    """Class representing a node in a linked list."""
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node


class LinkedList:
    """Class representing a singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Add a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty, set new node as the head
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node containing the specified data."""
        if not self.head:  # If the list is empty, do nothing
            return
        if self.head.data == data:  # If the head contains the data, remove it
            self.head = self.head.next
            return
        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:  # If found, skip the node
            current.next = current.next.next

    def display(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()  # Output: 10 -> 20 -> 30
    ll.prepend(5)
    ll.display()  # Output: 5 -> 10 -> 20 -> 30
    ll.delete(20)
    ll.display()  # Output: 5 -> 10 -> 30
