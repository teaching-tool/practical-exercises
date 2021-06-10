from advalg.graph_helpers import *

matchings_cases = [
    ("3-cycle", make_cycle(3), 0),
    ("4-cycle", make_cycle(4), 2),
    ("10-cycle", make_cycle(10), 2),
    ("20-cycle", make_cycle(20), 2),
    ("3x3 grid", make_grid(3,3), 0),
    ("4x4 grid", make_grid(4,4), 36),
    ("6x3 grid", make_grid(6,3), 41),
    ("10x2 grid", make_grid(10,2), 89),
    ("4-clique", make_clique(4), 3),
    ("5-clique", make_clique(5), 0),
    ("8-clique", make_clique(8), 105),
    ("10-clique", make_clique(10), 945)
]

hamcycle_cases = [
    ("10-path", make_path(10), 0),
    ("10-cycle", make_cycle(10), 1),
    ("4-clique", make_clique(4), 3),
    ("5-clique", make_clique(5), 12),
    ("6-clique", make_clique(6), 60),
    ("7-clique", make_clique(7), 360),
    ("8-clique", make_clique(8), 2520),
    ("9-clique", make_clique(9), 20160),
    ("10-clique", make_clique(10), 181440)
]

def test_matchings(perfect_matchings):
    """Tests the implementation of the inclusion-exclusion algorithm for perfect matchings"""
    for name,g,m in matchings_cases:
        actual = perfect_matchings(g)
        if actual == m: print(f"Perfect matchings test ({name}) passed!")
        else: print(f"Perfect matchings test ({name}) failed. Expected {m} actual {actual}")


def test_ham_cycles(hamiltonian_cycles):
    """Tests the implementation of inclusion-exclusion algorithm for hamiltonian cycles"""
    for name,g,h in hamcycle_cases:
        actual = hamiltonian_cycles(g)
        if actual == h: print(f"Ham-cycle test ({name}) passed!")
        else: print(f"Ham-cycle test failed. Expected {h} actual {actual}")