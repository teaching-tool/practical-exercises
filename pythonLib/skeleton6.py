from advalg.graph import Graph
from advalg.tests6 import test_vc
from advalg.cnf import CNF
from advalg.sat_solver import is_satisfiable, solve

def sat_experiment() -> None:
    """Perform the SAT experiment"""
    pass

# TODO add missing function here
def vc_sat(g: Graph, k: int) -> bool:
    """Does g have a vertex cover of size k? Implement using reduction to SAT"""
    pass

def vc_fpt(g: Graph, k: int) -> bool:
    """ Does g have a vertex cover of size k? Implement FPT algorithm for vertex cover. """
    pass

# Test the implementation of the FPT algorithm for Vertex Cover
test_vc(vc_sat)
test_vc(vc_fpt)

# TODO add missing test here