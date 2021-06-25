from math import inf
from advalg.helpers import combinations, subsets
import advalg.prim as prim
from advalg.tests4 import test_tsp_dp, test_tsp_approx, test_vc_approx
from advalg.lp import *

def tsp_dp(start, g):
    vts = frozenset(g.vertices())
    table = {frozenset(sub):{v:inf for v in vts} for sub in subsets(vts)}
    table[frozenset([start])][start] = 0

    for k in range(1, g.vertex_count()+1):
        for subset in map(frozenset, combinations(vts, k)):
            for v in subset:
                reduced = subset - frozenset([v])
                for u in filter(lambda u: g.edge_exists(u,v), vts):
                    table[subset][v] = min(table[subset][v], table[reduced][u] + g.edge_weight(u,v))

    cycle = [start]

    while len(vts) > 0:
        u = cycle[-1]
        v = min(g.adjacent(u), key = lambda v: table[vts][v] + g.edge_weight(v,u))
        cycle.append(v)
        vts -= {v}

    return cycle

def tsp_approx(start, g):
    mst = prim.mst(g)
    marked = {v:False for v in mst.vertices()}
    tour = []
    
    def dfs(v):
        tour.append(v)
        marked[v] = True
        for u in mst.adjacent(v):
            if not marked[u]:
                dfs(u)

    dfs(start)
    return tour + [start]

def vc_approx(g):
    vc = set()

    for e in g.edges():
        if e.u in vc or e.v in vc: continue
        vc.update([e.u, e.v])
    
    return vc

def vc_lp(g):
    x = variables(g.vertex_count())
    obj = Minimize(LinearFunc.sum(x))
 
    lp = LP(x, obj)
    for e in g.edges():
        lp.add_constraint(x[e.u] + x[e.v] >= 1)

    asn = lp.solve().variables
    return {x for x in asn if asn[x] >= 0.5}

#Test
test_tsp_dp(tsp_dp)
test_tsp_approx(tsp_approx)
test_vc_approx(vc_approx)
test_vc_approx(vc_lp)
