class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = []
    
    def enqueue(self, data):
        if len(self.queue) >= self.capacity:
            raise OverflowError("Queue is full")
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

# Example Usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())
print("Front:", q.peek())
print("Queue size:", q.size())


class Dequeue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.dequeue = []
    
    def add_front(self, data):
        if len(self.dequeue) >= self.capacity:
            raise OverflowError("Dequeue is full")
        self.dequeue.insert(0, data)

    def add_rear(self, data):
        if len(self.dequeue) >= self.capacity:
            raise OverflowError("Dequeue is full")
        self.dequeue.append(data)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        return self.dequeue.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        return self.dequeue.pop()
    
    def is_empty(self):
        return len(self.dequeue) == 0

    def size(self):
        return len(self.dequeue)

# Example Usage
dq = Dequeue(5)
dq.add_rear(10)
dq.add_rear(20)
dq.add_front(5)

print("Removed front:", dq.remove_front())
print("Removed rear:", dq.remove_rear())
