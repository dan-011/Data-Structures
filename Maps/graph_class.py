class Graph_ES:
    def __init__(self, V = set(), E = set()):
        self.V = V
        self.E = E

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v in self.V: self.V.remove(v)
        else: raise KeyError("Vertex {} is not in the graph".format(v))

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        a,b = e
        if e in self.E: self.E.remove(e)
        else: raise KeyError("Edge {} is not in the graph".format(e))

    def _neighbors(self, v):
        neighbors = set()
        for edge in self.E:
            a,b = edge
            if a == v: neighbors.add(b)
            elif b == v: neighbors.add(a)
            else: continue
        return neighbors

class Graph_AS:
    def __init__(self, V = set(), E = set()):
        self.V = V
        self.nbrs = dict()
        for edge in E:
            a,b = edge
            if a in self.nbrs:
                self.nbrs[a].add(b)
            else:
                self.nbrs[a] = {b}
            if b in self.nbrs:
                self.nbrs[b].add(a)
            else:
                self.nbrs[b] = {a}

    def __len__(self):
        return len(self.V)

    def __iter__(self):
        return iter(self.V)

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        if v in self.V: self.V.remove(v)
        else: raise KeyError()

    def add_edge(self, e):
        a,b = e
        if a in self.nbrs:
            self.nbrs[a].add(b)
        else:
            self.nbrs[a] = {b}

    def remove_edge(self, e):
        a,b = e
        if a not in self.nbrs or b not in self.nbrs[a]:
            raise KeyError()
        else:
            self.nbrs[a].remove(b)
            if len(self.nbrs[a])==0:
                self.nbrs.remove(a)
    
    def _neighbors(self, v):
        return self.nbrs[v]

if __name__ == '__main__':
    # 1 <==> 2 <==> 3
    vs = {1,2,3}
    es = {(1,2), (2,1), (2,3), (3,2)}
    g1 = Graph_ES(vs, es)
    assert len(g1) == 3
    g2 = Graph_ES()
    assert len(g2) == 0

    