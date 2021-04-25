from typing import List, Iterable
from advalg.graph import Graph, Edge
from advalg.helpers import combinations

def is_iset(g: Graph, s: Iterable[int]) -> bool:
    """Is s an independent set of graph g?"""
    return not any([e.u in s and e.v in s for e in g.edges()])

def is_perf_matching(g: Graph, m: List[Edge]) -> bool:
    """Is m a perfect matching in the graph g?"""
    if g.vertex_count() % 2 != 0 or len(m) != g.vertex_count() // 2: 
        return False

    vts = set(reduce(lambda vs,e: vs + [e.u, e.v], m, []))
    return len(vts) == g.vertex_count() and all([g.has_vertex(v) for v in vts])

def is_vc(g: Graph, vc: Iterable[int]) -> bool:
    """Is vc a vertex cover of the graph g?"""
    return all([e.u in vc or e.v in vc for e in g.edges()])

def is_hamcycle(g: Graph, tour: List[int]) -> bool:
    """Is the given tour a hamiltonian cycle in g?"""
    unique = len(set(tour)) == len(tour) - 1
    all_visited = all([v in tour for v in g.vertices()])
    is_cycle = tour[0] == tour[-1]
    legal_edges = all([g.edge_exists(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    return unique and all_visited and is_cycle and legal_edges

def make_grid(rows: int, cols: int) -> Graph:
    """Constructs a grid graph with the given rows and columns"""
    assert(rows >= 0 <= cols)
    g = Graph(rows * cols)
    
    for r in range(rows):
        for c in range(cols):
            v = r * cols + c
            if c > 0: g.add_edge(v, v-1)
            if r > 0: g.add_edge(v, v-cols)

    return g

def make_path(n: int) -> Graph:
    """Constructs a path with n vertices (n-1 edges)"""
    assert(n >= 0)

    g = Graph(n)
    for i in range(n-1):
        g.add_edge(i, i+1)
    
    return g

def make_cycle(n: int) -> Graph:
    """
    Constructs of cycle with n vertices.
    A cycle with 0 vertices is the empty graph.
    A cycle with 1 vertex is a loop.
    A cycle with 2 vertices is not permitted because of parallel edges.
    """
    assert(n >= 0 and n!=2)

    if n == 0: return Graph()
    g = make_path(n)
    g.add_edge(n-1, 0)
    return g

def make_clique(n: int) -> Graph:
    """Constructs a clique with n vertices"""
    assert(n >= 0)

    g = Graph(n)
    if n < 2: return g

    for (u,v) in combinations(range(n), 2):
        g.add_edge(u,v)
        
    return g