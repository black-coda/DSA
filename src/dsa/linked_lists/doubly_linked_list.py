from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insertHead(self, data: int):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
            return
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insertTail(self, data: int):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
