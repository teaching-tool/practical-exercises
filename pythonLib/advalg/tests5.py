from functools import reduce
from graph import Graph
from helpers import combinations, permutations

def test_matchings(perfect_matchings):
    for g,m in []: #TODO make graphs here
        actual = perfect_matchings(g)
        if actual == m: print("Test passed!")
        else: print(f"Test failed. Expected {m} actual {actual}")

def test_ham_cycles(hamiltonian_cycles):
    for g,hc in []: #TODO make graphs here
        actual = hamiltonian_cycles(g)
        if actual == m: print("Test passed!")
        else: print(f"Test failed. Expected {hc} actual {actual}")

# Brute force
def is_perf_matching(g,m):
    if g.vertex_count() % 2 != 0 or len(m) != g.vertex_count() // 2: 
        return False

    vts = set(reduce(lambda vs,e: vs + [e.u, e.v], m, []))
    return len(vts) == g.vertex_count() and all([g.has_vertex(v) for v in vts])

def brute_perf_matchings(g):
    n = g.vertex_count()
    if n % 2 != 0: return 0
    return len([c for c in combinations(g.edges(), n//2) if is_perf_matching(g,c)])

# Also in tests4
def is_hamcycle(g, tour):
    unique = len(set(tour)) == len(tour) - 1
    all_visited = all([v in tour for v in g.vertices()])
    is_cycle = tour[0] == tour[-1]
    legal_edges = all([g.edge_exists(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    return unique and all_visited and is_cycle and legal_edges

def brute_ham_cycles(g):
    tours = [p + (p[0],) for p in permutations(g.vertices(), g.vertex_count())]
    ham_cycles = [t for t in tours if is_hamcycle(g,t)]
    return len(ham_cycles) // (2 * g.vertex_count())