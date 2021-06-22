from advalg.graph import Graph
from typing import Callable

def load_graph():
    with open("data/vc_graph_small.txt") as reader:
        lines = reader.readlines()
        n = int(lines[0])
        g = Graph(n)

        for line in lines[1:]:
            u,v = line.split(" ")
            g.add_edge(int(u)-1, int(v)-1)

    return g

g = load_graph()

def test_vc(vc_fpt: Callable[[Graph, int], bool]) -> None:
    """Tests the implementation of the FPT algorithm for vertex cover"""
    n = g.vertex_count()
    actual = next(k for k in range(n+1) if vc_fpt(g, k))
    if actual != 12:
        print(f"Test vc_graph_small failed. Expected 12 actual {actual}")
    else:
        print("Test vc_graph_small passed")