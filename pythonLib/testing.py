from advalg.lp import *
import re

x = [Var(0), Var(1)]
lp = LP(x, Minimize(x[0] + x[1]))
lp.add_constraint(x[0] >= 1)
lp.add_constraint(x[1] >= 1)
lp.add_constraint(2*x[0] + 3*x[1] >= 10)
obj, vs = lp.solve()

print(f"Objective is: {obj}")
print(f"Variables: {vs}")