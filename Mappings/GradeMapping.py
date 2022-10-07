class Entry:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        # Opt 1
        #return self.name == other.name and self.grade == other.grade

        # Opt 2 - Best because we don't want entries to be equivalent in the mapping
        return self.name == other.name

        # Opt 3
        #return self.grade == other.grade
    def __repr__(self):
        # should return a code-like string
        return "Entry(name = {}, grade = {}".format(self.name,self.grade)

class GradeMapping:
    def __init__(self):
        self.n_buckets = 10
        self._L = [[] for i in range(self.n_buckets)]
        self._len = 0

    def add_grade(self, name, grade):
        # Create a temporary entry
        new_entry = Entry(name, grade)

        # Find the bucket where it should go
        # bucket_index = hash(new_entry) % self.n_buckets
        # bucket_index = hash(name) % self.n_buckets works too, but this way hash a mapping to an entry in case we later want to change what equality means (what if there are 1,000,000 people named Cassie, we will need to change what makes an object unique)

        # bucket = self._L[bucket_index]

        #can also just say:
        bucket = self._L[hash(new_entry) % self.n_buckets]

        for entry in bucket:
            if new_entry == entry:
                entry.grade == grade
                return
        
        # key not found in bucket, add new Entry
        bucket.append(new_entry)
        self._len += 1

    def __contains__(self, name):
        bucket = self._L[hash(name) % self.n_buckets]

        if len(bucket) > 0: return True
        else: return False


if __name__ == '__main__':
    import random

    names = {"Ax","Cassie","Jake", "Marco","Rachel","Tobias"}

    gm = GradeMapping()
    for name in names:
        # assert name not in gm
        gm.add_grade(name, random.gauss(75, 10))
        assert name in gm # check that gm has this name
    


    x = (1,2,3)
    y = (1,2,3)
    assert hash(x) == hash(y)
