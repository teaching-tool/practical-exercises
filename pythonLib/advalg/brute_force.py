from advalg.helpers import combinations, n_tuples, permutations, subsets
import advalg.graph_helpers as gh
import math

def brute_perf_matchings(g):
    """Computes the number of perfect matchings in g using brute force."""
    n = g.vertex_count()
    if n % 2 != 0: return 0
    return len([c for c in combinations(g.edges(), n//2) if gh.is_perf_matching(g,c)])

def brute_cheapest_hamcycle(g):
    """
    Computes the weight of the cheapest hamiltonian cycle in g.
    Returns inf if no hamiltonian cycle exists.
    """
    tours = [p + (p[0],) for p in permutations(g.vertices(), g.vertex_count())]
    ham_cycles = [t for t in tours if gh.is_hamcycle(g,t)]
    if len(ham_cycles) == 0: return math.inf
    return min([gh.tour_cost(g, t) for t in ham_cycles])

def brute_hamcycles(g):
    """Constructs all hamiltonian cycles of g using brute force"""
    tours = (p + (p[0],) for p in permutations(g.vertices(), g.vertex_count()))
    return (t for t in tours if gh.is_hamcycle(g,t))

def brute_vc(g):
    """Computes the size of the minimum vertex cover of g using brute force"""
    return min([len(sub) for sub in subsets(g.vertices()) if gh.is_vc(g,sub)])

def brute_isets(g):
    """Uses brute force to construct all independent sets of g"""
    return [s for s in subsets(g.vertices()) if gh.is_iset(g,s)]

def brute_dnf_count(dnf):
    """Uses brute force to count number of satisfying assignments in the given dnf"""
    count = 0

    for tup in n_tuples([True, False], dnf.var_count()):
        asn = {(i+1):tup[i] for i in range(len(tup))}
        if dnf.is_satisfied(asn):
            count += 1
    
    return count