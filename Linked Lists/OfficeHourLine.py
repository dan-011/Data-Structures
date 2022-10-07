from DoublyLinkedList import DoublyLinkedList

class OfficeHourLine:
    def __init__(self):
        self._DLL = DoublyLinkedList()
        
    def add_student(self, netID):
        return self._DLL.add_last(netID)
    
    def visit_next(self):
        if len(self) == 0: raise RuntimeError("Cannot visit an empty OfficeHourLine")
        return self._DLL.remove_first()
    
    def peek(self):
        if len(self) == 0: return "No students waiting"
        return self._DLL.peek()
    
    def __len__(self):
        return len(self._DLL)


import random, string
random.seed(658) # Change the seed to generate new sets of netIDS
my_lst = []
n = 1000
for i in range(n):
    new_chars = ''.join(random.choice(string.ascii_lowercase) for j in range(3))
    new_ints = ''.join(str(random.randint(0,9)) for j in range(4))
    new_netID = new_chars + new_ints
    my_lst.append(new_netID)
    

sl = OfficeHourLine()
for student in my_lst:
    sl.add_student(student)
    assert(sl.peek() == my_lst[0])
    
for i in range(len(my_lst)):
    assert(sl.visit_next() == my_lst[i])
    assert(len(sl) == n-1-i)

sl = OfficeHourLine()
assert(sl.peek() == "No students waiting")

try:
    sl.visit_next()
    raise AssertionError("visit_next from empty OFficeHourLine did not raise RuntimeError")
except RuntimeError:
    pass
    