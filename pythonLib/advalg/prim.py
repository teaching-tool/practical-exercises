import heapq
from graph import Graph

def mst(graph: Graph) -> Graph:
    start_vtx = next(graph.vertices())
    tree = Graph()
    tree.add_vertex(start_vtx)
    in_tree = {v:v==start_vtx for v in graph.vertices()}
    edges = graph.incident(start_vtx)
    heapq.heapify(edges)

    while len(edges) > 0:
        u,v,w = heapq.heappop(edges)
        if in_tree[u] and in_tree[v]:
            continue
        new_vtx = u if in_tree[v] else v
        tree.add_vertex(new_vtx)
        tree.add_edge(u,v,w)
        in_tree[new_vtx] = True
        for e in graph.incident(new_vtx):
            heapq.heappush(edges, e)
        
    return tree
