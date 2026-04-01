from typing import List, Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class Queue:
    """
    First In First Out
    """

    def __init__(self, head: Optional[Node] = None, tail: Optional[Node]= None) -> None:
        self.head = head
        self.tail = tail

    def enqueue(self, data: int):
        new_node = Node(data=data)
        if self.head is None and self.tail is None:
            self.head, self.tail = new_node, new_node
            return

        # else we just update the tail
        self.tail.next = new_node  # link new node at back
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next  # move head forward
        if self.head is None:  # queue is now empty
            self.tail = None
        return removed
    
    def __repr__(self) -> str:
        values: List[str] = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " → ".join(values)
        
    


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(90)
    q.enqueue(32)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(35)
    q.enqueue(999)
    q.dequeue()
    print(q)
    