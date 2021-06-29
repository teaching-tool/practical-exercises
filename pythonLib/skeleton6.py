from advalg.graph import Graph
from advalg.tests6 import test_fpt, test_sat
from advalg.cnf import CNF
from advalg.sat_solver import is_satisfiable, solve

def sat_experiment() -> None:
    """Perform the SAT experiment"""
    pass

def vc_sat(g: Graph, k: int) -> bool:
    """Does g have a vertex cover of size k? Implement using reduction to SAT"""
    pass

def vc_fpt(g: Graph, k: int) -> bool:
    """Does g have a vertex cover of size k? Implement FPT algorithm for vertex cover"""
    pass

# Test the implementation of the FPT algorithm for Vertex Cover
test_sat(vc_sat)
test_fpt(vc_fpt)