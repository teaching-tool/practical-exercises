from typing import Iterator, List
import numpy as np

class Edge:
    """Represents a weighted undirected edge"""
    def __init__(self, u: int, v: int, w: float):
        """Constructs an edge between vertices u and v with weight w"""
        self.u = u
        self.v = v
        self.w = w

    def has_endpoint(self, v: int):
        """Is vertex v an endpoint for this edge?"""
        return v == self.v or v == self.u
    
    def other(self, v: int) -> int:
        """Returns the end point that is not v"""
        assert(self.has_endpoint(v))
        if v == self.v: return self.u
        return self.v

    def __iter__(self):
        return iter((self.u, self.v, self.w))

    def __str__(self):
        return "%d <--> %d (%.2f)" %(self.u, self.v, self.w)

    def __lt__(self, other: 'Edge'):
        return self.w < other.w

class Graph:
    """
    Represents a weighted undirected graph.
    Vertices are integers in the range [0-n).
    Loops are permitted but parallel edges are not.
    """
    def __init__(self, n: int = 0):
        """Constructs a graph with vertices [0-n) and no edges"""
        self._vertex_count = n
        self._edge_count = 0
        self._adj = [set() for _ in range(n)]
        self._weight = {}

    def vertex_count(self) -> int:
        """Returns the number of vertices in the graph"""
        return self._vertex_count

    def edge_count(self) -> int:
        """Returns the number of edges in the graph"""
        return self._edge_count

    def adjacent(self, v: int) -> List[int]:
        """Returns a list of vertices adjacent to vertex v"""
        assert(self.has_vertex(v))
        return list(self._adj[v])

    def incident(self, v: int) -> List[Edge]:
        """Returns a list of edges incident to vertex v"""
        return [Edge(u,v,self.edge_weight(u,v)) for u in self.adjacent(v)]

    def has_vertex(self, v: int) -> bool:
        """Is v a vertex in this graph?"""
        return 0 <= v < self.vertex_count()

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        """Add an edge between vertices u and v with the given weight (1 by default)"""
        assert(self.has_vertex(u) and self.has_vertex(v))
        assert(not self.edge_exists(u,v))
        self._adj[u].add(v)
        self._adj[v].add(u)
        self._weight[(u,v)] = weight
        self._weight[(v,u)] = weight
        self._edge_count += 1

    def edges(self) -> Iterator[Edge]:
        """Returns all edges in the graph as a generator"""
        for (u,v),w in self._weight.items():
            if u <= v: yield Edge(u,v,w)

    def vertices(self) -> Iterator[int]:
        """Returns all vertices in the graph as a generator"""
        for v in range(self.vertex_count()):
            yield v

    def degree(self, v) -> int:
        """Returns the degree of vertex v"""
        assert(self.has_vertex(v))
        return len(self._adj[v])

    def delete_incident(self, v: int) -> None:
        """Delete all edges incident with vertex v"""
        for u in self.adjacent(v):
            self.delete_edge(u,v)

    def delete_edge(self, u: int, v: int) -> None:
        """Deletes the edge (u,v)"""
        assert(self.edge_exists(u,v))
        self._adj[u].remove(v)
        self._adj[v].remove(u)
        del self._weight[(u,v)]
        del self._weight[(v,u)]
        self._edge_count -= 1

    def edge_exists(self, u: int, v: int) -> bool:
        """Does the graph contain an edge (u,v)?"""
        return self.has_vertex(u) and v in self._adj[u]

    def edge_weight(self, u: int, v: int) -> float:
        """Returns the weight associated with the edge (u,v)"""
        assert(self.edge_exists(u,v))
        return self._weight[(u,v)]

    def adj_matrix(self) -> np.ndarray:
        """Returns the adjacency matrix of the graph"""
        n = self.vertex_count()
        m = np.zeros((n,n), dtype='int32')
        for e in self.edges():
            m[e.u, e.v] = e.w
            m[e.v, e.u] = e.w
        return m

    def copy(self) -> 'Graph':
        """Returns a deep copy of the graph"""
        _copy = Graph(self.vertex_count())

        for (u,v,w) in self.edges():
            _copy.add_edge(u,v,w)

        return _copy

    def __repr__(self) -> str:
        n = self.vertex_count()
        m = self.edge_count()
        rep = f"Graph object: {n} vertices, {m} edges"

        for e in self.edges():
            rep += f"\n{e.u} <--> {e.v} (weight: {e.w})"

        return rep
