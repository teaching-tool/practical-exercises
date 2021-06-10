from advalg.graph_helpers import *
from advalg.brute_force import brute_cheapest_hamcycle, brute_hamcycles, brute_perf_matchings

cycle3 = make_cycle(3) # 6
cycle4 = make_cycle(4) # 
cycle10 = make_cycle(10) # 
cycle20 = make_cycle(20) # 

grid2x2 = make_grid(2,2) # 
grid3x3 = make_grid(3,3) # 
grid4x4 = make_grid(4,4) # 
grid6x4 = make_grid(6,3) # 
grid10x2 = make_grid(10,2) # 

clique4 = make_clique(4) # 3
clique5 = make_clique(5) # 12
clique6 = make_clique(6) # 60
clique7 = make_clique(7) # 360
clique8 = make_clique(8) # 2520
clique9 = make_clique(9) # 20160
clique10 = make_clique(10) # 181440
#clique

g = clique10
cycles = brute_hamcycles(g)
cycle_count = sum(1 for _ in cycles)
print(cycle_count // (2*g.vertex_count()))