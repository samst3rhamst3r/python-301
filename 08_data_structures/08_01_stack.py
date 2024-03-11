# Build a custom `Stack` similar to the `Queue` you built

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def push(self, value):
        new_node = Node(value)
        if not self.is_empty():
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.length -= 1
            return popped_node.value