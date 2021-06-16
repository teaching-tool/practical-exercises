from advalg.lp import *
from advalg.cnf import CNF
from advalg.dnf import DNF
from advalg.sat_solver import *

dnf = DNF(3)
dnf.add_clause([1,-2,3])
dnf.add_clause([-1,-3])
dnf.add_clause([1])
print(dnf)

cnf = CNF(3)
cnf.add_clause([1,-2,3])
cnf.add_clause([-1,-3])
cnf.add_clause([1])
cnf.add_clause([-1])
print(cnf)

success, solution = solve(cnf)
print(f"Satisfiable: {success}")
if success:
    print(f"Solution: {solution}")

# x = [Var(0), Var(1)]
# lp = LP(x, Minimize(x[1] + x[0]))
# lp.add_constraint(x[0] >= 1)
# lp.add_constraint(x[1] >= 1)
# lp.add_constraint(2*x[0] + 3*x[1] >= 10)
# res = lp.solve()

# print(f"Objective is: {res.obj_value}")
# print(f"Variables: {res.variables}")