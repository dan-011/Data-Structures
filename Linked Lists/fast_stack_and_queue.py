from LinkedList import LinkedList

class Stack_L:
    def __init__(self):
        self._L = list()        # Composition: the Stack_L class has a List
    
    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List

    def push(self, item):
        self._LL.add_first(item)
    
    def pop(self):
        return self._LL.remove_first()


class Queue_L:
    def __init__(self):
        self._L = list()

    def enqueue(self, item):
        self._L.append(item)
        
    def dequeue(self):
        return self._L.pop(0)

class Queue_LL:
    def __init__(self):
        self._LL = LinkedList()

    def enqueue(self, item):
        self._LL.add_last(item)
    
    def dequeue(self):
        return self._LL.remove_first()

if __name__ == '__main__':
    ##########Test Stack_L##########
    s1 = Stack_L()
    for i in range(10): s1.push(i*3)
    
    for i in range(9,-1,-1): assert(s1.pop() == i*3)


    ##########Test Stack_LL#########
    sLL = Stack_LL()
    for i in range(10): sLL.push(i*3)
    
    for i in range(9, -1, -1): assert sLL.pop() == i*3

    ##########Test Queue_L##########
    qL = Queue_L()
    for i in range(10): qL.enqueue(i*3)

    for i in range(10): assert qL.dequeue() == i*3


    ##########Test Queue_LL#########
    qLL = Queue_LL()
    for i in range(10): qLL.enqueue(i*3)

    for i in range(10): assert qLL.dequeue() == i*3