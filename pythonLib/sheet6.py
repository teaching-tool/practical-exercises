from graph import Graph
import fileinput

#TODO find compatible SAT-solver
def cnf_experiment():
    pass

def vc_fpt(g, k):
    if g.edge_count() == 0: return True
    if k == 0: return False

    e = next(g.edges())
    return vc_fpt(g.minus_vertices([e.u]), k-1)\
           or vc_fpt(g.minus_vertices([e.v]), k-1)

def min_vc(g: Graph):
    n = g.vertex_count()
    return next(k for k in range(n+1) if vc_fpt(g, k))

#TODO move to testing file
g = Graph()
for line in fileinput.input():
    e = line.split(" ")
    u = int(e[0])
    v = int(e[1])

    if not g.has_vertex(u): g.add_vertex(u)
    if not g.has_vertex(v): g.add_vertex(v)
    g.add_edge(u,v)

print(min_vc(g))