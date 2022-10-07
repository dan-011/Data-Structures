class Node:
    def __init__(self, _item, _next = None):
        self._item = _item
        self._next = _next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
        self.tail = None
    def __len__(self):
        return self.len

    def add_first(self, item):
        node = Node(item)
        if len(self) == 0:
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node._next = self.head
            self.head = node
            self.len += 1
    
    def add_last(self, item):
        node = Node(item)
        if len(self) == 0:
            self.add_first(item)
        else:
            self.tail._next = node
            self.tail = node
            self.len += 1

    def remove_first(self):
        if len(self) == 0:
            raise IndexError
        elif len(self) == 1:
            item = self.head._item
            self.tail = None
            self.head = None
            self.len -= 1
            return item
    
    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()
        else:
            second_to_last = self.head
            while second_to_last._next._next is not None:
                second_to_last = second_to_last._next
            item = second_to_last._next._item
            second_to_last._next = None
            self.tail = second_to_last
            return item