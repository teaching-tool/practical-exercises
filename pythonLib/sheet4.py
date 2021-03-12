from math import inf
from helpers import haversine, combinations, subsets
from graph import Graph
import prim
import fileinput

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
    edges = []
    in_matching = {v:False for v in g.vertices()}

    for e in g.edges():
        if in_matching[e.u] or in_matching[e.v]: continue
        in_matching[e.u] = in_matching[e.v] = True
        edges.append(e)
    
    return edges

# TODO find compatible lp solver
def vc_lp(g):
    pass

#TODO move testing to test file
def tour_cost(g, tour):
    return sum([g.edge_weight(tour[i], tour[i+1]) for i in range(len(tour)-1)])

names = []
positions = []

for line in fileinput.input():
    name,pos = line.split(",")
    lat,lon = pos.split("/")
    names.append(name)
    positions.append((float(lat), float(lon)))

g = Graph(len(names))

for u in range(len(names)):
    (lat1,lon1) = positions[u]
    for v in range(u+1, len(names)):
        (lat2,lon2) = positions[v]
        g.add_edge(u,v,haversine(lat1, lon1, lat2, lon2))

tour = tsp_dp(0, g)
tour2 = tsp_approx(0, g)
print(tour_cost(g, tour) / 1000)
print(tour_cost(g, tour2) / 1000)