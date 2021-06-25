from typing import Iterable
from advalg.graph import Graph
from advalg.helpers import combinations, subsets
import advalg.prim as prim
from advalg.tests4 import test_tsp_dp, test_tsp_approx, test_vc_approx
from advalg.lp import *

# Check the documentation for Graph, prim and LP

# The test cases expects cycles to contain the starting vertex at the first and last index
# A hamiltonian cycle for a triangle could be [0,1,2,0]

def tsp_dp(start: int, g: Graph) -> List[int]:
    """Returns the optimal TSP tour of g where 'start' is the initial vertex"""
    pass

def tsp_approx(start: int, g: Graph) -> List[int]:
    """Returns a 2-approximation TSP tour of g where 'start' is the initial vertex"""
    pass

def vc_approx(g: Graph) -> Iterable[int]:
    """Returns a 2-approximation Vertex Cover of g using maximal matching"""
    pass

def vc_lp(g: Graph) -> Iterable[int]:
    """Returns a 2-approximation Vertex Cover of g using Linear Programming"""
    pass

# Test the TSP implementations
test_tsp_dp(tsp_dp)
test_tsp_approx(tsp_approx)

# Test the VC implementations
test_vc_approx(vc_approx)
test_vc_approx(vc_lp)
