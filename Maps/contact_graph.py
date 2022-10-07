class ContactGraph:
    def __init__(self, V, E):
        self.V = set(V)
        self.nbrs = dict()
        for pair in E:
            node, neighbor = pair
            if node in self.nbrs:
                self.nbrs[node].add(neighbor)
            else:
                self.nbrs[node] = {neighbor}
            #self.nbrs[neighbor] = set()
    def __iter__(self):
        return iter(self.V)

    def neighbors(self, v):
        if v in self.nbrs:
            yield from self.nbrs[v]

    def all_contacts(self, v):
        # go to the neighors of the node, yield them, then go to the neighbors of the neightbors and yield them, etc etc (i think this is BFS)
        tree = {}
        to_visit = [(None,v)]
        while to_visit:
            node, neighbor = to_visit.pop(0)
            if neighbor not in tree:
                tree[neighbor] = node
                #if neighbor in self.nbrs:
                #    for n in self.nbrs[neighbor]:
                for n in self.neighbors(neighbor): # this was added
                            to_visit.append((neighbor,n))
        return iter(tree.keys())
        # 4 1 3 6 2 5
    
    def group_contacts(self, V): # this may not work
        # V is a collection
        store = set()
        for node in V:
            for neighbor in self.neighbors(node):
                store.add(neighbor)
        yield from store
    

    # (1,0) (2,1) (3,2) (4,2) (6,3) (5,3)
    # 1<-->2<-->3
    #      |   /
    #      \  /
    #  6<-->4<-->5
    def contacts(self, v, d):
        tree = {}
        count = 0
        queue = [(None,(v,0))]
        while queue and count <= d:
            node, pair = queue.pop(0)
            neighbor, level = pair
            if neighbor not in tree and level <= d:
                tree[neighbor] = level
                #if neighbor in self.nbrs:
                #    for n in self.neighbors(neighbor):
                for n in self.neighbors(neighbor):
                        queue.append((neighbor, (n, level+1)))
        values = []
        for i in tree:
            values.append((i, tree[i]))
        yield from values
class MutualContactGraph(ContactGraph):
    def __init__(self, V, E):
        # super().__init__(V,E)
        self.V = V
        self.nbrs = {}
        for pair in E:
            node, neighbor = pair
            if node in self.nbrs:
                self.nbrs[node].add(neighbor)
            else:
                self.nbrs[node] = {neighbor}
            if neighbor in self.nbrs:
                self.nbrs[neighbor].add(node)
            else:
                self.nbrs[neighbor] = {node}
    
    
if __name__ == '__main__':
    V = [1, 2, 3, 4]
    E = [(1, 2), (2, 3),(4,2),(4,3),(4,5),(4,6)]
    G1 = ContactGraph(V, E)
    G2 = MutualContactGraph(V, E)
    # 1<-->2<-->3
    #      |   /
    #      \  /
    #  6<-->4<-->5

    print("Iterator")
    for v in G1: print(v, end=' ')
    print()
    for v in G2: print(v, end = ' ')
    print()
    print("Neighbors")
    for n in G1.neighbors(2): print(n, end=' ')
    print()
    for n in G2.neighbors(2): print(n, end=' ')
    print()
    print("all_contacts")
    for c in G1.all_contacts(2): print(c, end=' ')
    print()
    for c in G2.all_contacts(2): print(c, end=' ') # doesn't work
    print()
    #print(G1.nbrs)
    #print(G2.nbrs)
    print("group_contacts")
    for c in G1.group_contacts([2, 4]): print(c, end=' ')
    print()
    for c in G2.group_contacts([2, 5]): print(c, end=' ')
    print()
    print("contacts")
    for c in G1.contacts(1, 2): print(c, end=' ')
    print()
    for c in G2.contacts(1, 3): print(c, end=' ') # (1,0) (2,1) (3,2) (4,2) (6,3) (5,3)
    # 1<-->2<-->3
    #      |   /
    #      \  /
    #  6<-->4<-->5
    