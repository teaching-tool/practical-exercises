from advalg.helpers import subsets, choose
from advalg.tests5 import test_matchings, test_ham_cycles
import numpy as np

def perfect_matchings(graph):
    if graph.vertex_count() % 2 != 0: 
        return 0
        
    count = 0

    for subset in subsets(graph.vertices()):
        count += (-1) ** len(subset) * edge_sets(graph, subset)

    return int(count)

def edge_sets(graph, removed):
    edge_count = 0
    for e in graph.edges():
        if e.u in removed or e.v in removed:
            continue
        edge_count += 1

    return choose(edge_count, graph.vertex_count()/2)

def hamiltonian_cycles(graph):
    count = 0

    for subset in subsets(graph.vertices()):
        count += (-1) ** len(subset) * closed_walks(graph, subset)

    return int(count / (2 * graph.vertex_count()))

def closed_walks(graph, removed):
    k = graph.vertex_count()
    adj_matrix = graph.adj_matrix()
    
    for v in removed:
        adj_matrix[v,:] = 0
        adj_matrix[:,v] = 0

    pow_matrix = np.linalg.matrix_power(adj_matrix, k)
    return np.trace(pow_matrix)

#Test
test_matchings(perfect_matchings)
test_ham_cycles(hamiltonian_cycles)