import random
class Entry:
    def __init__(self, pos, temp):
        self.pos = pos
        self.temp = temp
        self.min = temp
        self.max = temp

    
    def __lt__(self, other):
        return self.temp < other.temp

    def add_temp(self, temp):
        if self.min > temp:
            self.min = temp
        if self.max < temp:
            self.max = temp
    
    def __gt__(self, other):
        return self.temp > other.temp
    
    def __eq__(self, other):
        return self.rounded_position() == other.rounded_position()
    
    def __hash__(self):
        longit = round(self.pos[0],1)
        lat = round(self.pos[1], 1)
        return hash((longit, lat))

    def rounded_position(self):
        return (round(self.pos[0],1),round(self.pos[1],1))

    def __str__(self):
        return "Entry(pos = {}, temp = {})".format(self.pos, self.temp)

class TempMap:
    def __init__(self):
        self.buckets = 1
        self.len = 0
        self.L = [[] for i in range(self.buckets)]
    
    def hash(self, entry):
        if isinstance(entry, tuple):
            longit = round(entry[0],1)
            latit = round(entry[1],1)
            return hash((longit,latit)) % self.buckets
        else:
            return hash(entry) % self.buckets

    def __contains__(self, pos):
        bucket = self.L[self.hash(pos)]
        rounded_pos = (round(pos[0], 1), round(pos[1], 1))
        for item in bucket:
            if item.rounded_position() == rounded_pos: return True
        return False
    
    def __len__(self):
        return self.len

    def __getitem__(self, pos):
        bucket = self.L[self.hash(pos)]
        if pos not in self: raise KeyError("This position does not exist")
        else:
            location = self.hash(pos)
            rounded_pos = (round(pos[0], 1), round(pos[1],1))
            for entry in self.L[location]:
                if entry.rounded_position() == rounded_pos:
                    return (entry.min, entry.max)
    
    def add_report(self, pos, temp):
        entry = Entry(pos,temp)
        location = self.hash(entry)
        if pos not in self:
            self.L[self.hash(entry)].append(entry)
            self.len += 1
        else:
            for e in self.L[location]:
                if e == entry:
                    e.add_temp(temp)
        if len(self) > self.buckets*2: self.rehash()
    
    def remove_pos(self, pos):
        if pos not in self: raise KeyError("You can't remove a position that doesn't exist")
        else:
            location = self.hash(pos)
            rounded_pos = (round(pos[0], 1), round(pos[1],1))
            for entry in self.L[location]:
                if entry.rounded_position() == rounded_pos:
                    self.L[location].remove(entry)
                    self.len -= 1
                    break
            if len(self) < (self.buckets//2): self.rehash()

    def rehash(self):
        if len(self) > self.buckets*2:
            self.buckets = self.buckets*2
        else:
            self.buckets = self.buckets//2
        L = [[] for i in range(self.buckets)]
        for bucket in self.L:
            for entry in bucket:
                position = self.hash(entry)
                L[position].append(entry)
        self.L = L[:]
        

# returns a 3-tuple of (lat, long, temperature)
def generate_report():
    # Generate random coordinates
    lat =  random.randint(0, 89) + random.random()
    long = random.randint(0, 179) + random.random()

    # 50% chance of negating lat and long (N->S and E->W)
    if random.randint(0, 1) == 0: lat *= -1
    if random.randint(0, 1) == 0: long *= -1

    # Generate temperature (gaussian distribution about 25 Celcius)
    temp = random.gauss(25, 5)

    # Return 3-tuple with position and temperature
    return (lat, long, temp)

if __name__ == '__main__':
    # generate some reports
    n = 5
    reports = [generate_report() for i in range(n)]

    # print out (lat, long) and temp w/ some formatting
    for report in reports:
        print(f"(lat,long): ({report[0]}, {report[1]})\ttemp: {report[2]}")

    tm1 = TempMap()
    p1 = (36.4482, -105.0072)
    p2 = (36.44, -105.00) # rounds to the same as p1
    p3 = (36.45, -105.00) # rounds to different than p1
    # Examples: `in` and `add_report`
    assert p1 not in tm1

    tm1.add_report(p1, 25)
    assert p1 in tm1

    assert p2 in tm1
    assert p3 not in tm1

    # Examples: `get` and `add_report`
    assert tm1[p1] == (25, 25)
    tm1.add_report(p1, 25.7) # new high
    assert tm1[p1] == (25, 25.7)
    tm1.add_report(p1, 20) # new low
    assert tm1[p1] == (20, 25.7)
    try:
        tm1[p3]
        raise AssertionError
    except KeyError:
        pass
    tm1.remove_pos(p1)
    try:
        tm1[p1]
        raise AssertionError
    except KeyError:
        pass
    try:
        tm1.remove_pos(p1)
        raise AssertionError
    except KeyError:
        pass
