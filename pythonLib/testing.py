from advalg.lp import *
from advalg.cnf import CNF
from advalg.sat_solver import *

#SAT Example
cnf = CNF(3)
cnf.add_clause([1,-2,3])
cnf.add_clause([-1,-3])
cnf.add_clause([1])
print(f"{cnf}\n")

success, solution = solve(cnf)
print(f"Satisfiable: {success}")
if success:
    print(f"Solution: {solution}")

print()

#LP Example
x = [Var(0), Var(1)]
lp = LP(x, Minimize(x[1] + x[0]))
lp.add_constraint(x[0] >= 1)
lp.add_constraint(x[1] >= 1)
lp.add_constraint(2*x[0] + 3*x[1] >= 10)
print(f"{lp}\n")

res = lp.solve()
print(f"Objective is: {res.obj_value}")
print(f"Variables: {res.variables}")
