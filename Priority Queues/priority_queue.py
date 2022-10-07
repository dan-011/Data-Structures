class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
    def __eq__(self, other):
        return self.item == other.item and self.priority == other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority

class PQ_UL:
    def __init__(self):
        self.L = []
    
    def __len__(self):
        return len(self.L)

    def insert(self, item, priority):
        entry = Entry(item, priority)
        self.L.append(entry)
    
    def find_min(self):
        smallest = 0
        for i in range(len(self)):
            if self.L[i] < self.L[smallest]:
                smallest  = i
        return self.L[smallest]

    def remove_min(self):
        smallest = 0
        for i in range(len(self)):
            if self.L[i] < self.L[smallest]:
                smallest  = i
        item = self.L[smallest]
        del self.L[smallest]
        return item

class PQ_OL:
    def __init__(self):
        self.L = []
    
    def __len__(self):
        return len(self.L)

    def find_min(self):
        return self.L[-1]

    def remove_min(self):
        return self.L.pop()

    def insert(self, item, priority):
        self.L.append(Entry(item, priority))
        n = len(self)
        for i in range(n-1, 0, -1):
            if self.L[i-1] < self.L[i]:
                self.L[i-1], self.L[i] = self.L[i], self.L[i-1]
    
if __name__ == '__main__':
    s = PQ_OL()
    u = PQ_UL()

    for i in range(10):
        s.insert(str(i), i)
        u.insert(str(i), i)
    
    assert s.find_min().item == str(0)
    assert s.remove_min().item == str(0)
    assert s.find_min().item == str(1)

    assert u.find_min().item == str(0)
    assert u.remove_min().item == str(0)
    assert u.find_min().item == str(1)

    assert len(s) == 9
    assert len(u) == 9

    e1 = Entry("Hello", 1)
    e2 = Entry("Hello", 1)
    e3 = Entry("World", 1)
    assert e1 == e2
    assert e1 != e3

    pq = PQ_UL()
    n = 100
    for i in range(n):
        assert len(pq) == i
        pq.insert(str(i), i)
    old = pq.remove_min()
    for i in range(1, n):
        peak = pq.find_min()
        new = pq.remove_min()
        assert new == peak
        assert old.priority <= new.priority
        assert len(pq) == n - i - 1
        old = new