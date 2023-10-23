# ============================================================
# A simple singly linked list
# ============================================================
from Node import Node

class Linked_list():
    head = None
    tail = None
    length = 0

    def __init__(self) -> None:
        # Initialize a new list
        self.head = Node(None)
        self.tail = Node(None)
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)
        self.length = 0
        pass

    def __iter__(self):
        self.n = self.head
        return self
    
    def __next__(self) -> Node:
        if self.n.get_next().get_element() != None:
            self.n = self.n.get_next()
            return self.n.get_element()
        else:
            raise StopIteration
        
    def print(self) -> None:
        print("PRINTING LIST: ")
        e = self.head.get_next()
        while e.get_element() != None:
            print(e.get_element())
            if e == e.get_next():
                print("Error, recursive Node")
                exit()
            e = e.get_next()
        
    def has_next(self) -> bool:
        return self.n.get_next().get_element() != None

    def add_first(self, element) -> Node:
        """
        Inserts a new element at the start of the linked list, 
        returns the old head
        """
        old_head = self.head.get_next()
        first_node = Node(element)

        first_node.set_next(old_head)
        old_head.set_prev(first_node)

        self.head.set_next(first_node)
        first_node.set_prev(self.head)
        
        self.length += 1
        return old_head

    # Add to the end of the list
    def add_last(self, element):
        old_tail = self.tail.get_prev()
        last_node = Node(element)

        last_node.set_prev(old_tail)
        self.tail.set_prev(last_node)

        old_tail.set_next(last_node)
        last_node.set_next(self.tail)

        self.length += 1
        return None
    
    # Remove the first element of the list
    def remove_first(self) -> Node:
        old_head = self.head
        if old_head.get_next().get_element() == None:
            raise ValueError("No elements to remove")
        
        old_first = old_head.get_next()

        new_first = old_first.get_next()

        self.head.set_next(new_first)
        new_first.set_prev(self.head)

        self.length -= 1
        return old_first.get_element()
    
    # Remove the last element of the list
    def remove_last(self):
        old_tail = self.tail
        if old_tail.get_prev().get_element() == None:
            raise ValueError("No elements to remove")
        
        old_last = old_tail.get_prev()

        new_last = old_last.get_prev()

        self.tail.set_prev(new_last)
        new_last.set_next(self.tail)

        self.length -= 1
        return old_last.get_element()
    
    # Get size of list
    def get_size(self):
        return self.length
    
    # Check if the list is empty
    def is_empty(self):
        return self.length == 0
    
    # Get the head of the list
    def get_first(self):
        if self.head.get_next().get_element() == None:
            raise ValueError("Head is None")
        return self.head.get_next().get_element()
    
    # Get the tain of the list
    def get_last(self):
        if self.tail.get_prev().get_element() == None:
            raise ValueError("Tail is None")
        return self.tail.get_prev().get_element()
