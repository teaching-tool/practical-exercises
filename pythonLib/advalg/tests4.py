from math import inf
from advalg.graph import Graph
from advalg.helpers import haversine, subsets, permutations
from advalg.map_visualizer import plot_tour
from advalg.brute_force import is_hamcycle, is_vc

def cities_denmark():
    """
    Constructs a complete graph with vertices corresponding to Danish cities.
    An edge between two cities is weighted by the great-circle distance between them.
    Returns the graph and the city names as a pair.
    Vertex v corresponds to city at index v.
    """
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

def tour_cost(g, tour):
    """ Returns the total cost of the given tour in g. """
    return sum([g.edge_weight(tour[i], tour[i+1]) for i in range(len(tour)-1)])

#Testing

def test_tsp_dp(tsp_dp):
    """Tests the implementation of the DP for TSP"""
    g,names = cities_denmark()
    cost = 964225.4
    tour = tsp_dp(0,g)
    cities = [names[i] for i in tour]
    if not is_hamcycle(g,tour):
        plot_tour(cities, "TSP-DP\nTest failed: Not a ham-cycle")
    elif abs(tour_cost(g,tour) - cost) > 0.1:
        plot_tour(cities, "TSP-DP\nTest failed: Ham-cycle not optimal")
    else:
        plot_tour(cities, "TSP-DP\nTest passed!: Ham-cycle is optimal")

def test_tsp_approx(tsp_approx):
    """Tests the implementation of the 2-approximation for TSP"""
    g,names = cities_denmark()
    cost = 964225.4
    tour = tsp_approx(0,g)
    cities = [names[i] for i in tour]
    if not is_hamcycle(g,tour):
        plot_tour(cities, "TSP-DP\nTest failed: Not a ham-cycle")
    elif (tour_cost(g,tour)/cost) > 2:
        plot_tour(cities, "TSP-DP\nTest failed: cost(ham-cycle) > 2 * cost(optimal ham-cycle)")
    else:
        plot_tour(cities, "TSP-DP\nTest passed!: Ham-cycle is a 2-approximation")

def test_vc_approx(vc_approx):
    """Tests the implementation of the 2-approximation for vertex cover"""
    for g,vc_size in []: # Make tests
        vc = set(vc_approx(g))
        if not is_vc(vc):
            print("Test failed: Not a vertex cover")
        elif (len(vc) / vc_size) > 2:
            print("Test failed: |vc| > 2 * |optimal vc|")
        else:
            print("Test passed!")

# Come up with example graphs (metric?)