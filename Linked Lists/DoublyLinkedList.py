class Node:
    def __init__(self, _item, _next = None, prev = None):
        self._item = _item
        self._next = _next
        self.prev = prev
        if _next is not None:
            self._next.prev = self
        if prev is not None:
            self.prev._next = self

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_first(self, item):
        node = Node(item)
        if self.len == 0:
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node._next = self.head
            self.head.prev = node
            self.len += 1
            self.head = node
    
    def add_last(self, item):
        node = Node(item)
        if self.len == 0:
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node.prev = self.tail
            self.tail._next = node
            self.tail = node
            self.len += 1
    def remove_first(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.head._item
            self.head = None
            self.tail = None
            self.len -= 1
            return item
        else:
            item = self.head._item
            self.head._next.prev = None
            self.head = self.head._next
            self.len -= 1
            return item
        
    def remove_last(self):
        if self.len == 0:
            raise RuntimeError
        elif self.len == 1:
            item = self.tail._item
            self.head = None
            self.tail = None
            self.len -= 1
            return item
        else:
            item = self.tail._item
            self.tail.prev._next = None
            self.tail = self.tail.prev
            self.len -= 1
            return item

    def __len__(self):
        return self.len

if __name__ == '__main__':
    dl1 = DoublyLinkedList()
    assert(dl1.head == None)

    #add_first()
    for i in range(10):
        dl1.add_first(i*3)
        assert(dl1.head._item == i*3)

    #remove_first()
    for i in range(9,-1,-1):
        assert(dl1.remove_first() == i*3)

    #add_last()
    dl1 = DoublyLinkedList()
    for i in range(10):
        dl1.add_last(i*2)

    for i in range(10):
        assert(dl1.remove_first() == i*2)

    #remove_last()
    dl1 = DoublyLinkedList()
    for i in range(10):
        dl1.add_first(i*7)

    for i in range(10):
        assert(dl1.remove_last() == i*7)

