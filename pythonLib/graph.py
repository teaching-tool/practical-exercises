from matrix import Matrix

class Graph:
    def __init__(self, n=0):
        self._vertex_count = n
        self._edge_count = 0
        self._adj = {v:set() for v in range(n)}
        self._cost = {}

    def vertex_count(self):
        return self._vertex_count

    def edge_count(self):
        return self._edge_count

    def adjacent(self, v):
        return list(self._adj[v])

    def adjacent_edges(self, v):
        return [Edge(u,v,self.edge_weight(u,v)) for u in self.adjacent(v)]

    def has_vertex(self, v):
        return v in self._adj

    def add_vertex(self, v):
        assert(not self.has_vertex(v))
        if v in self._adj: return
        self._adj[v] = set()
        self._vertex_count += 1

    def add_edge(self, u, v, cost=1):
        assert(self.has_vertex(u) and self.has_vertex(v))
        assert(not self.edge_exists(u,v))
        self._adj[u].add(v)
        self._adj[v].add(u)
        self._cost[(u,v)] = cost
        self._cost[(v,u)] = cost
        self._edge_count += 1

    def edges(self):
        for u in self.vertices():
            for v in self._adj[u]:
                if u <= v: yield Edge(u,v,self.edge_weight(u,v))

    def vertices(self):
        for v in self._adj:
            yield v

    def delete_vertex(self, v):
        assert(self.has_vertex(v))
        self.delete_incident(v)
        del self._adj[v]
        self._vertex_count -= 1

    def delete_vertices(self, vs):
        for v in vs:
            self.delete_vertex(v)

    def delete_incident(self, v):
        for u in list(self._adj[v]):
            self.delete_edge(u,v)

    def delete_edge(self, u, v):
        assert(self.edge_exists(u,v))
        self._adj[u].remove(v)
        self._adj[v].remove(u)
        self._edge_count -= 1

    def edge_exists(self, u, v):
        return u in self._adj and v in self._adj[u]

    def edge_weight(self, u, v):
        assert(self.edge_exists(u,v))
        return self._cost[(u,v)]

    def adj_matrix(self):
        return AdjMatrix(self.vertices(), self.edges())

    def minus_vertices(self, vs):
        _copy = self.copy()
        _copy.delete_vertices(vs)
        return _copy

    def copy(self):
        _copy = Graph()

        for v in self.vertices(): _copy.add_vertex(v)
        for (u,v,w) in self.edges(): _copy.add_edge(u,v,w)

        return _copy

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    
    def other(self, v):
        assert(v == self.v or v == self.u)
        if v == self.v: return self.u
        return self.v

    def __iter__(self):
        return iter((self.u, self.v, self.w))

    def __str__(self):
        return "%d <--> %d (%.2f)" %(self.u, self.v, self.w)

    def __lt__(self, other):
        return self.w < other.w

class AdjMatrix:
    def __init__(self, vertices, edges):
        self._ident = {v:i for i,v in enumerate(vertices)}
        self._size = len(self._ident)
        self._m = Matrix(self._size, self._size)
    
        for (u,v,w) in edges:
            uid = self._ident[u]
            vid = self._ident[v]
            self._m[uid, vid] = w
            self._m[vid, uid] = w

    def power(self, k):
        self._m **= k

    def size(self):
        return self._size

    def get(self, r, c):
        return self._m[r,c]

