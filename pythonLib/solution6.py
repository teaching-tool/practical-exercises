from advalg.tests6 import test_fpt, test_sat
from advalg.cnf import CNF
from advalg.sat_solver import is_satisfiable
from advalg.helpers import combinations

def vc_fpt(g, k):
    if g.edge_count() == 0: return True
    if k == 0: return False

    e = next(g.edges())
    return vc_fpt(rem(g, e.u), k-1)\
           or vc_fpt(rem(g, e.v), k-1)

def rem(g, v):
    h = g.copy()
    h.delete_incident(v)
    return h

def min_vc(g):
    n = g.vertex_count()
    return next(k for k in range(n+1) if vc_fpt(g, k))

def vc_sat(g, k):
    n = g.vertex_count()
    cnf = CNF(n*k)

    for r in range(k):
        row = [c + r*n for c in range(1, n+1)]
        exactly_one(cnf, row)

    # for c in range(1, n+1):
    #     col = [c + r*n for r in range(k)]
    #     at_most_one(cnf, col)

    for e in g.edges():
        clause = []
        for r in range(k):
            clause.append((e.u + 1) + n*r)
            clause.append((e.v + 1) + n*r)

        cnf.add_clause(clause)

    return is_satisfiable(cnf)

def exactly_one(cnf, vars):
    cnf.add_clause([x for x in vars])
    at_most_one(cnf, vars)

def at_most_one(cnf, vars):
    for x,y in combinations(vars, 2):
        cnf.add_clause([-x, -y])

#Testing
test_fpt(vc_fpt)
test_sat(vc_sat)