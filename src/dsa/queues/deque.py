from typing import Any
# from collections import deque #(python implementation)

class Node:
    def __init__(self, val: Any):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, x: Any):
        node = Node(x)
        if not self.head:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_back(self, x: Any):
        node = Node(x)
        if not self.tail:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove_front(self):
        if not self.head:
            raise Exception("Empty deque")
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def remove_back(self):
        if not self.tail:
            raise Exception("Empty deque")
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val