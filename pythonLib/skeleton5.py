from advalg.graph import Graph
from advalg.helpers import subsets, choose
from advalg.tests5 import test_matchings, test_ham_cycles

# Enumerate all vertex subsets of g using subsets(g.vertices())
# Obtain the adjacency matrix of g using g.adj_matrix()

def perfect_matchings(g: Graph) -> int:
    """Returns the number of Perfect Matchings in G"""
    pass

def hamiltonian_cycles(graph: Graph) -> int:
    """Returns the number of Hamiltonian Cycles in G"""
    pass

#Test perfect matchings implementation
test_matchings(perfect_matchings)

#Test Hamiltonian Cycles implementation
test_ham_cycles(hamiltonian_cycles)