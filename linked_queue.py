from node import Node

class LinkedQueue:
    def __init__(self):
        self.front = None  # Dequeue from head
        self.rear = None   # Enqueue at tail

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty linked queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Queue became completely empty
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: No front element to peek.")
        return self.front.value