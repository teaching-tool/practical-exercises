from graph import Graph
from helpers import haversine, subsets, permutations
from math import inf
from map_visualizer import plot_tour

def cities_denmark():
    names = []
    positions = []

    with open("data/cities.txt") as reader:
        for line in reader.readlines():
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

    return g,names

# Helper functions
def is_vc(g, vc):
    return all([e.u in vc or e.v in vc for e in g.edges()])

def is_hamcycle(g, tour):
    unique = len(set(tour)) == len(tour) - 1
    all_visited = all([v in tour for v in g.vertices()])
    is_cycle = tour[0] == tour[-1]
    legal_edges = all([g.edge_exists(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    return unique and all_visited and is_cycle and legal_edges

def tour_cost(g, tour):
    return sum([g.edge_weight(tour[i], tour[i+1]) for i in range(len(tour)-1)])

def brute_vc(g):
    return min([len(sub) for sub in subsets(g.vertices()) if is_vc(g,sub)])

def brute_hamcycle(g):
    tours = [p + (p[0],) for p in permutations(g.vertices(), g.vertex_count())]
    ham_cycles = [t for t in tours if is_hamcycle(g,t)]
    if len(ham_cycles) == 0: return inf
    return min([tour_cost(g, t) for t in ham_cycles])

#Testing

g,names = cities_denmark()
cost = 964225.4

def test_tsp_dp(tsp_dp):
    tour = tsp_dp(0,g)
    cities = [names[i] for i in tour]
    if not is_hamcycle(g,tour):
        plot_tour(cities, "TSP-DP\nTest failed: Not a ham-cycle")
    elif abs(tour_cost(g,tour) - cost) > 0.1:
        plot_tour(cities, "TSP-DP\nTest failed: Ham-cycle not optimal")
    else:
        plot_tour(cities, "TSP-DP\nTest passed!: Ham-cycle is optimal")

def test_tsp_approx(tsp_approx):
    tour = tsp_approx(0,g)
    cities = [names[i] for i in tour]
    if not is_hamcycle(g,tour):
        plot_tour(cities, "TSP-DP\nTest failed: Not a ham-cycle")
    elif (tour_cost(g,tour)/cost) > 2:
        plot_tour(cities, "TSP-DP\nTest failed: cost(ham-cycle) > 2 * cost(optimal ham-cycle)")
    else:
        plot_tour(cities, "TSP-DP\nTest passed!: Ham-cycle is a 2-approximation")

def test_vc_approx(vc_approx):
    for g,vc_size in []: # Make tests
        vc = set(vc_approx(g))
        if not is_vc(vc):
            print("Test failed: Not a vertex cover")
        elif (len(vc) / vc_size) > 2:
            print("Test failed: |vc| > 2 * |optimal vc|")
        else:
            print("Test passed!")

# Come up with example graphs (metric?)