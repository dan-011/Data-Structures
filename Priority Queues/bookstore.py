class Person:
    def __init__(self, name, phase, cat = None):
        self.name = name
        self.phase = phase
        self.cat = cat

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        if self.phase < other.phase:
            return True
        elif self.phase > other.phase:
            return False
        else:
            if self.cat == other.cat:
                return False
            elif self.cat is None:
                return False
            elif other.cat is None:
                return True
            else:
                if self.phase == 1:
                    if self.cat == "FR" and other.cat == "EL":
                        return True
                    else:
                        return False
                elif self.phase == 2:
                    if self.cat == "K12" and other.cat == "Uni":
                        return True
                    else:
                        return False
                else: # phase 3 only has 1 category
                    return False
    def __le__(self, other):
        return self < other or self.phase == other.phase and self.cat == other.cat
    
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return "({}, {}, {})".format(self.name, self.phase, self.cat)

class Line:
    def __init__(self, n_avail, people = None):
        self.n_avail = n_avail
        self.store = set()
        self.people = []
        if people is not None:
            for person in people:
                self.add_buyer(person)
    
    def upheap(self):
        i = len(self) - 1
        p = self.parent(i)
        
        while p is not None and self.people[i] < self.people[p]:
            self.people[p], self.people[i] = self.people[i], self.people[p]
            i = p
            p = self.parent(i)

    def downheap(self, i):
        c = self.smallest_child(i)
        while c is not None and self.people[c] < self.people[i]:
            # print("swapping {} with {}".format(self.people[c], self.people[i]))
            self.people[i], self.people[c] = self.people[c], self.people[i]
            i = c
            c = self.smallest_child(i)

    def smallest_child(self, i):
        l = (2*i) + 1
        r = (2*i) + 2
        bottom = len(self) - 1
        if l > bottom and r > bottom:
            return None
        elif l > bottom:
            return r
        elif r > bottom:
            return l
        else:
            if self.people[l] < self.people[r]:
                return l
            else:
                return r

    def parent(self, i):
        if i == 0: return None
        else: return (i-1)//2

    def heapify(self):
        n = len(self)
        for i in range(n-1, -1, -1):
            self.downheap(i)

    def __len__(self):
        return len(self.people)

    def add_buyer(self, person):
        if not isinstance(person, Person): raise TypeError("{} is not a person".format(person))
        if person in self.store: raise KeyError("{} is already in line".format(person.name))
        else:
            self.people.append(person)
            self.store.add(person)
            self.upheap()

    def sell_book(self):
        if self.n_avail < 1: raise ValueError("There are no more books")
        if len(self) == 0: raise IndexError("The line is empty")
        self.n_avail -= 1
        customer = self.people[0]
        if len(self) > 1:
            self.people[0] = self.people.pop()
            self.downheap(0)
        else:
            self.people.pop()
        return customer

    def add_copies(self, n):
        self.n_avail += n

    def print(self):
        for i in self.people:
            print(i)
    
if __name__ == '__main__':
    p1 = Person("Abhi", 1, "FR")
    p2 = Person("Steve", 1, "EL")
    p3 = Person("Anne", 1)
    p4 = Person("Jay", 2)
    p5 = Person("Rick", 2, "K12")
    p6 = Person("Peter", 3, "GP")
    

    assert p1 < p2
    assert p2 < p3
    assert p1 < p4
    assert p5 < p4
    assert p2 != p4
    assert p5 < p6
    assert p1 < p6

    people = [p6,p5,p4,p3,p2,p1]
    sorted_people = [p1,p2,p3,p4,p5,p6]
    line = Line(4, people)
    assert len(line) == 6

    line.add_buyer(Person("Jane", 2, "K12"))
    line.sell_book()
    try:
        line.add_buyer(Person("Steve", 2))
        raise AssertionError()
    except KeyError:
        pass
    try:
        line.add_buyer("Phil")
        raise AssertionError()
    except TypeError:
        pass
    
    line.add_copies(10)
    try:
        for i in range(10):
            line.sell_book()
    except IndexError:
        pass
    
    people = [p5,p4,p2,p6,p1,p3]
    line = Line(10, people)
    line.add_buyer(Person("Jill", 3, "GP"))
    line.add_buyer(Person("Ryan", 1, "EL"))
    line.print()