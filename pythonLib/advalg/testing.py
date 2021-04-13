from graph import Graph
from dnf import Clause

g = Graph(10)
for i in range(9):
    g.add_edge(i, i+1, i*2)

for e in g.edges():
    print(f"{e.u} {e.v} {e.w}")

c = Clause([])