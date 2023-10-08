# ============================================================
# A simple singly linked list
# ============================================================
from Node import Node

class Simply_linked_list():
    head = None
    tail = None
    length = 0

    def __init__(self) -> None:
        # Initialize a new list
        self.head = None
        self.tail = None
        self.length = 0
        pass

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < self.length:
            self.element_n = self.head
            for i in range(self.n):
                self.element_n = self.element_n.get_next()
            self.n += 1
            return self.element_n.get_element()
        else:
            raise StopIteration
        
    def has_next(self):
        return self.n < self.length

    def add_first(self, element):
        """
        Inserts a new element at the start of the linked list, 
        returns the old head
        """
        old_head = self.head
        if self.head == None:
            # List is empty
            self.head = Node(element)
            self.tail = self.head
        else:
            # List has more than one element
            new_head = Node(element)
            new_head.set_next(self.head)
            self.head = new_head
        
        self.length += 1
        return old_head

    # Add to the end of the list
    def add_last(self, element):
        new_tail = Node(element)
        if self.tail == None:
            # List is empty, set head and tail
            self.tail = new_tail
            self.head = self.tail
        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail

        self.length += 1
        return None
    
    # Remove the first element of the list
    def remove_first(self):
        if self.head == None:
            raise ValueError("Head is None")
        
        self.old_head_value = self.head.get_element()
        self.head = self.head.get_next()
        self.length -= 1
        return self.old_head_value
    
    # Remove the last element of the list
    def remove_last(self):
        if self.tail == None:
            # Tail does not exist
            raise ValueError("Tail is None")
      
        # Save old tail value
        self.old_tail_value = self.tail.get_element()

        # Handle case where length == 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return self.old_tail_value


        # Loop through nodes to get the second to last node
        self.loop_element = self.head
        while self.loop_element.get_next().get_next() != None:
            self.loop_element = self.loop_element.get_next()
        
        # Set new tail
        self.tail = self.loop_element

        # Delete tail
        self.tail.set_next(None)
        
        self.length -= 1

        return self.old_tail_value
    
    # Get size of list
    def get_size(self):
        return self.length
    
    # Check if the list is empty
    def is_empty(self):
        return self.length == 0
    
    # Get the head of the list
    def get_first(self):
        if self.head == None:
            raise ValueError("Head is None")
        return self.head.get_element()
    
    # Get the tain of the list
    def get_last(self):
        if self.tail == None:
            raise ValueError("Tail is None")
        return self.tail.get_element()
