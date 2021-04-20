from advalg.graph import Graph
from advalg.helpers import subsets

max_tests = [
    (4,4,8),
    (6,6,18),
    (8,10,40),
    (30,10,150),
]

count_tests = [
    (4,4,1234),
    (6,6,5598861),
    (8,10,512615852515459),
    (12,12,162481813349792588536582997),
]

def test_max_iset(max_iset):
    """Tests the implementation of the DP for maximum independent set"""
    for r,c,m in max_tests:
        actual = max_iset(r,c)
        if actual != m: 
            print(f"Max iset {r}x{c} test failed. Expected {m} actual {actual}")
        else: 
            print(f"Max iset {r}x{c} test passed!")


def test_count_iset(count_iset):
    """Tests the implementation of the DP for counting independent sets"""
    for r,c,n in count_tests:
        actual = count_iset(r,c)
        if actual != n: 
            print(f"Count isets {r}x{c} test failed. Expected {n} actual {actual}")
        else:
            print(f"Count isets {r}x{c} test passed!")

def is_iset(g, s):
    """
    Is s an independent set of graph g?
    This might be moved to a different module"""
    return not any([e.u in s and e.v in s for e in g.edges()])

def brute_isets(g):
    """
    Uses brute force to construct all independent sets of g.
    Might be moved to a different module.
    """
    return [s for s in subsets(g.vertices()) if is_iset(g,s)]

#also in sheet8
def grid_graph(rows, cols):
    """Constructs a grid graph with the given rows and columns"""
    g = Graph(rows * cols)
    
    for r in range(rows):
        for c in range(cols):
            v = r * cols + c
            if c > 0: g.add_edge(v, v-1)
            if r > 0: g.add_edge(v, v-cols)

    return g