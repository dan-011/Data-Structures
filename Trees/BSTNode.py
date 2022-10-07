class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
    # classical iteration (bad)
    def __iter__(self): return BSTNode_Iterator(self)

    # generator based iteration (good)
    def in_order(self):
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        yield self.key        # return this key
        if self.right is not None: yield from self.right.in_order() # recursively go right

    # Freebie! This will help you print out useful info on nodes, if you want
    def __repr__(self):
        return f"BSTNode(key={self.key})"
  

    # TODO: implement the below methods
    def put(self, key):
        if self.key == key:
            return None
        elif key < self.key:
            if self.left:
                self.left.put(key)
            else: self.left = BSTNode(key)
        elif key > self.key:
            if self.right:
                self.right.put(key)
            else:
                self.right = BSTNode(key)
        return self

    def pre_order(self):
        yield self.key
        if self.left:
            yield from self.left.pre_order()
        if self.right:
            yield from self.right.pre_order()

    def post_order(self):
        if self.left:
            yield from self.left.post_order()
        if self.right:
            yield from self.right.post_order()
        yield self.key

    

# This technique is bad and slow, you shouldn't use it!
class BSTNode_Iterator:
    def __init__(self, node):
        self.queue = []
        self.in_order(node)
        self.counter = 0

    def in_order(self, node):
        if node.left is not None: self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None: self.in_order(node.right)

    def __next__(self):
        if self.counter < len(self.queue):
            self.counter += 1
            return self.queue[self.counter-1].key
        
        raise StopIteration
