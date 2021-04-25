from functools import reduce
from advalg.graph import Graph
from advalg.helpers import combinations, permutations

def test_matchings(perfect_matchings):
    """Tests the implementation of the inclusion-exclusion algorithm for perfect matchings"""
    for g,m in []: #TODO make graphs here
        actual = perfect_matchings(g)
        if actual == m: print("Test passed!")
        else: print(f"Test failed. Expected {m} actual {actual}")

def test_ham_cycles(hamiltonian_cycles):
    """Tests the implementation of inclusion-exclusion algorithm for hamiltonian cycles"""
    for g,hc in []: #TODO make graphs here
        actual = hamiltonian_cycles(g)
        if actual == m: print("Test passed!")
        else: print(f"Test failed. Expected {hc} actual {actual}")