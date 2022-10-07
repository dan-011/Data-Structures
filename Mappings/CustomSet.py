class CustomSet:
    def __init__(self):
        self.buckets = 100
        self.len = 0
        self.L = [[] for i in range(self.buckets)]
    def __contains__(self, item):
        location = self.L[hash(item) % self.buckets]
        return item in location

    def add(self, item):
        index = hash(item) % self.buckets
        for i in self.L[index]:
            if i == item:
                return None
        self.L[index].append(item)
        self.len += 1
        if len(self) > self.buckets: self.rehash()
    def rehash(self):
        self.buckets = self.buckets * 2
        L = [[] for i in range(self.buckets)]
        for b in self.L:
            for i in b:
                bucket = hash(i) % self.buckets
                L[bucket].append(i)
        self.L = L[:]
    def __len__(self):
        return self.len
    def remove(self, item):
        index = hash(item) % self.buckets
        for i in self.L[index]:
            if i == item:
                self.L[index].remove(item)
                self.len -= 1
                return
        raise ValueError()
    def remove(self, item):
        if item in self:
            index = hash(item) % self.buckets
            self.L[index].remove(item)
            self.len -= 1
        else:
            raise ValueError()

if __name__ == '__main__':
    s = CustomSet()
    s.add(3)
    assert 3 in s
    s.add(3)
    assert len(s) == 1
    s.remove(3)
    assert 3 not in s
    try:
        s.remove(3)
        raise AssertionError()
    except ValueError:
        pass