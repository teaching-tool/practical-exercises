from advalg.lp import *

x = [Var(0), Var(1)]
lp = LP(x, Minimize(x[1] + x[0]))
lp.add_constraint(x[0] >= 1)
lp.add_constraint(x[1] >= 1)
lp.add_constraint(2*x[0] + 3*x[1] >= 10)
res = lp.solve()

print(f"Objective is: {res.obj_value}")
print(f"Variables: {res.variables}")