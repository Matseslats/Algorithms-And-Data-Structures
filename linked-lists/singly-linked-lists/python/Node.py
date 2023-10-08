# ============================================================
# Node class has an element and a reference to the next Node.
# ============================================================
class Node:
    element = None
    next = None

    # Constructor sets the new head
    def __init__(self, element) -> None:
        self.element = element
        pass

    def set_next(self, element):
        self.next = element

    def get_next(self):
        return self.next
    
    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element
