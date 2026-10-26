from node import Node

class LinkedStack:
    def __init__(self):
        self.top = None  # Head of the list is the top of the stack

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty linked stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: No top element to peek.")
        return self.top.value