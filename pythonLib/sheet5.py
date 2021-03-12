from helpers import subsets, choose

def perfect_matchings(graph):
    if graph.vertex_count() % 2 != 0: 
        return 0

    count = 0

    for subset in subsets(graph.vertices()):
        reduced_graph = graph.minus_vertices(subset)
        edge_count = reduced_graph.edge_count()
        edge_sets = choose(edge_count, graph.vertex_count()/2)
        count += (-1) ** len(subset) * edge_sets

    return int(count)

def hamiltonian_cycles(graph):
    count = 0

    for subset in subsets(graph.vertices()):
        reduced_graph = graph.minus_vertices(subset)
        walks = closed_walks(graph.vertex_count(), reduced_graph)
        count += ((-1) ** len(subset)) * walks

    return int(count / (2 * graph.vertex_count()))

def closed_walks(k, graph):
    adj_matrix = graph.adj_matrix()
    adj_matrix.power(k)
    count = 0

    for i in range(adj_matrix.size()):
        count += adj_matrix.get(i,i)

    return count