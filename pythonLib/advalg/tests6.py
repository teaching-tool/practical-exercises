import os
from advalg.graph import Graph
from typing import Callable

dirname = os.path.dirname(__file__)
graph_path = os.path.join(dirname, 'data/vc_graph_small.txt')
g = Graph.from_file(graph_path)

def test_vc(vc_fpt: Callable[[Graph, int], bool]) -> None:
    """Tests the implementation of the FPT algorithm for vertex cover"""
    n = g.vertex_count()
    actual = next(k for k in range(n+1) if vc_fpt(g, k))
    if actual != 12:
        print(f"Test vc_graph_small failed. Expected 12 actual {actual}")
    else:
        print("Test vc_graph_small passed")