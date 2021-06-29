from advalg.graph_helpers import make_clique, make_cycle, make_path
import os
from advalg.graph import Graph
from typing import Callable

dirname = os.path.dirname(__file__)
graph_path = os.path.join(dirname, 'data/vc_graph_small.txt')

tests_fpt = [
    ("10-path", make_path(10), 5),
    ("15-path", make_path(15), 7),
    ("10-cycle", make_cycle(10), 5),
    ("15-cycle", make_cycle(15), 8),
    ("24-cycle", make_cycle(24), 12),
    ("10-clique", make_clique(10), 9),
    ("15-clique", make_clique(15), 14),
    ("vc_graph_small", Graph.from_file(graph_path), 12)
]

tests_sat = [
    ("10-path", make_path(10), 5),
    ("15-path", make_path(15), 7),
    ("10-cycle", make_cycle(10), 5),
    ("15-cycle", make_cycle(15), 8),
    ("10-clique", make_clique(10), 9),
]

def run_tests(vc, cases):
    for name, g, size in cases:
        n = g.vertex_count()
        res = next(k for k in range(n+1) if vc(g, k))
        if res != size:
            print(f"Test {name} failed. Expected {size} got {res}")
        else:
            print(f"Test {name} passed")

def test_fpt(vc: Callable[[Graph, int], bool]) -> None:
    """Tests the FPT algorithm for vertex cover"""
    print(f"Testing: {vc.__name__}...")
    run_tests(vc, tests_fpt)

def test_sat(vc: Callable[[Graph, int], bool]) -> None:
    """Tests the reduction from vertex cover to SAT"""
    print(f"Testing: {vc.__name__}...")
    run_tests(vc, tests_sat)
