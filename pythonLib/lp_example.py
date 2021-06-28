from advalg.lp import *

# Linear programming problems are represented using the LP class.
# The optimization objective is either a maximization or a minimization of a linear combination.
# Constraints are linear inequalities (either <= or >=).
# There is a default lower bound of 0 on all variables.

# Variables are represented using the Var class
x0 = Var(0)
print(f"A variable: {x0}")

# You can use the 'variables' function to create a list of variables
x = variables(2)
print(f"A list of variables: {x}")

# Linear combinations are represented by the LinearComb class
# Here we create the linear combination 2*x0 + x*x1 using a list of tuples (constant, variable_number)
l1 = LinearComb([(2,0), (3,1)])
print(f"A linear combination (tuple syntax): {l1}")

# Linear combinations can also be created using overloaded operators
# Here we create the same linear combination using different syntax
l2 = 2*x[0] + 3*x[1]
print(f"The same linear combination (overloaded operators): {l2}")

# Linear combinations can also by created dynamically
# The linear combination 1*x0 + 2*x1 + ... + 10*x9 can be created using tuple syntax
l3 = LinearComb([(i+1,i) for i in range(5)])
print(f"A larger linear combination (tuple syntax): {l3}")

# The same linear combination can also be created using overloaded operators
# Note that a LinearComb object can be extended using += or -=
x = variables(5)
l4 = LinearComb()

for i in range(5):
    l4 += (i+1) * x[i]

print(f"The same linear combination (overloaded operators): {l4}")

# If you just need a sum of variables you can use LinearComb.sum
x = variables(5)
l5 = LinearComb.sum(x)
print(f"A simple sum of variables: {l5}")

# The optimization objective is either a maximization or minimization of a linear combination
x = variables(2)
l6 = 2*x[0] + 3*x[1]

obj_min = Minimize(l6)
print(f"Optimization objective for minimization: {obj_min}")

obj_max = Maximize(l6)
print(f"Optimization object for maximization: {obj_max}")

# Constraints are created using <= or >= operators
# Left hand side should be a LinearComb/Var object and the right hand side a float/int
x = variables(2)
l7 = x[0] + 2*x[1]

constraint_le = l7 <= 2.5
print(f"A <= constraint: {constraint_le}")

constraint_ge = l7 >= 2.5
print(f"A >= constraint: {constraint_ge}")

# With these basic building blocks we are ready to formulate the Linear Programming Problem:
# Maximize(x0 + 2*x1 - 3*x2) s.t.
# x0 + x1 <= 10
# x2 >= 1

x = variables(3)
lp = LP(x, Maximize(x[0] + 2*x[1] - 3*x[2]))
lp.add_constraint(x[0] + x[1] <= 10)
lp.add_constraint(x[2] >= 1)
print(lp)

# The solve method returns an LPResult, or None if the problem is infeasible
result = lp.solve()

# Print the solution to the LP
if result is not None:
    print(f"Objective value: {result.obj_value}")
    print(f"Assignment: {result.assignment}")