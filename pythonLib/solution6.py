from advalg.graph import Graph
from advalg.tests6 import test_vc

#TODO find compatible SAT-solver
def cnf_experiment():
    pass

def vc_fpt(g, k):
    if g.edge_count() == 0: return True
    if k == 0: return False

    e = next(g.edges())
    return vc_fpt(g.minus_vertices([e.u]), k-1)\
           or vc_fpt(g.minus_vertices([e.v]), k-1)

def min_vc(g):
    n = g.vertex_count()
    return next(k for k in range(n+1) if vc_fpt(g, k))

#Testing
test_vc(vc_fpt)