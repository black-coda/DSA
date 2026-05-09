from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_front(self, data: int):
        new_node = Node(data=data)  # step 1: create node
        new_node.next = self.head  # step 2: point it to current head
        self.head = new_node  # step 3: move head to new node

        if self.tail is None:  # edge case: if list was empty
            self.tail = new_node

    def insert_at_end(self, data: int):
        new_node = Node(data=data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current_head = self.head
        while current_head is not None:
            print(current_head.data)
            current_head = current_head.next
            
    def delete_from_front(self):
        if self.head is None:   # is empty case
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
    
    def delete_from_end(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
     
        current_head = self.head
        while current_head.next and current_head.next != self.tail:
            # loops until it gets to the node before the tail
            current_head = current_head.next
        current_head.next = None
        self.tail = current_head
            

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_end(94)
    ll.insert_at_end(3)
    ll.insert_at_end(9)
    # ll.print_list()
    ll.delete_from_end()
    ll.print_list()
    print(ll.tail==ll.head)
