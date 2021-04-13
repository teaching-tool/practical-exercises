from matrix import Matrix
from typing import Iterable, Iterator, List
from functools import reduce

class Edge:
    def __init__(self, u: int, v: int, w: float):
        self.u = u
        self.v = v
        self.w = w
    
    def other(self, v: int) -> int:
        assert(v == self.v or v == self.u)
        if v == self.v: return self.u
        return self.v

    def __iter__(self):
        return iter((self.u, self.v, self.w))

    def __str__(self):
        return "%d <--> %d (%.2f)" %(self.u, self.v, self.w)

    def __lt__(self, other: 'Edge'):
        return self.w < other.w

class AdjMatrix:
    def __init__(self, vertices: Iterable[int], edges: Iterable[Edge]):
        self._ident = {v:i for i,v in enumerate(vertices)}
        self._size = len(self._ident)
        self._m = Matrix(self._size, self._size)
    
        for (u,v,w) in edges:
            uid = self._ident[u]
            vid = self._ident[v]
            self._m[uid, vid] = w
            self._m[vid, uid] = w

    def power(self, k: int) -> None:
        self._m **= k

    def size(self) -> int:
        return self._size

    def get(self, r: int, c: int) -> int:
        return self._m[r,c]

class Graph:
    def __init__(self, n: int = 0):
        self._vertex_count = n
        self._edge_count = 0
        self._adj = {v:set() for v in range(n)}
        self._weight = {}

    def vertex_count(self) -> int:
        return self._vertex_count

    def edge_count(self) -> int:
        return self._edge_count

    def adjacent(self, v: int) -> List[int]:
        assert(self.has_vertex(v))
        return list(self._adj[v])

    def incident(self, v: int) -> List[Edge]:
        return [Edge(u,v,self.edge_weight(u,v)) for u in self.adjacent(v)]

    def has_vertex(self, v: int) -> bool:
        return v in self._adj

    def add_vertex(self, v: int) -> None:
        assert(not self.has_vertex(v))
        if v in self._adj: return
        self._adj[v] = set()
        self._vertex_count += 1

    def add_edge(self, u: int, v: int, weight: float = 1) -> bool:
        assert(self.has_vertex(u) and self.has_vertex(v))
        assert(not self.edge_exists(u,v))
        self._adj[u].add(v)
        self._adj[v].add(u)
        self._weight[(u,v)] = weight
        self._weight[(v,u)] = weight
        self._edge_count += 1

    def edges(self) -> Iterator[Edge]:
        for (u,v),w in self._weight.items():
            if u <= v: yield Edge(u,v,w)

    def vertices(self) -> Iterator[int]:
        for v in self._adj.keys():
            yield v

    def delete_vertex(self, v: int) -> None:
        assert(self.has_vertex(v))
        self.delete_incident(v)
        del self._adj[v]
        self._vertex_count -= 1

    def delete_vertices(self, vs: Iterable[int]) -> None:
        for v in vs:
            self.delete_vertex(v)

    def delete_incident(self, v: int) -> None:
        for u in self.adjacent(v):
            self.delete_edge(u,v)

    def delete_edge(self, u: int, v: int) -> None:
        assert(self.edge_exists(u,v))
        self._adj[u].remove(v)
        self._adj[v].remove(u)
        del self._weight[(u,v)]
        del self._weight[(v,u)]
        self._edge_count -= 1

    def edge_exists(self, u: int, v: int) -> bool:
        return u in self._adj and v in self._adj[u]

    def edge_weight(self, u: int, v: int) -> float:
        assert(self.edge_exists(u,v))
        return self._weight[(u,v)]

    def adj_matrix(self) -> AdjMatrix:
        return AdjMatrix(self.vertices(), self.edges())

    def minus_vertices(self, vs: Iterable[int]) -> 'Graph':
        _copy = self.copy()
        _copy.delete_vertices(vs)
        return _copy

    def copy(self) -> 'Graph':
        _copy = Graph()

        for v in self.vertices(): _copy.add_vertex(v)
        for (u,v,w) in self.edges(): _copy.add_edge(u,v,w)

        return _copy
