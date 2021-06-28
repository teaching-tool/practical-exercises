from advalg.cnf import CNF
from advalg.sat_solver import is_satisfiable, solve

# Boolean formulas in Conjunctive Normal Form (CNF) are represented using the CNF class.
# Literals are represented as integers.
# Positive and negative integers indiciate positive and negative literals respectively.
# Variable assignments are Dictionaries mapping integers to booleans.

# Let's take a look at an example:
# (x1 or x2) and (not x1 or x3) and (not x2)

# Create a CNF object with 3 variables (x1, x2, x3)
cnf = CNF(3)

# Add the clause (x1 or x2)
cnf.add_clause([1,2])

# Add the clause (not x1 or x3)
cnf.add_clause([-1, 3])

# Add the clause (not x2)
cnf.add_clause([-2])

# Print the cnf object to make sure it is correct
print(cnf)

# Check if the assignment (x1 = x2 = x3 = true) satisfies the CNF
satisfied = cnf.is_satisfied({1: True, 2: True, 3: True})
print(f"Satisfied by x1 = x2 = x3 = true: {satisfied}")

# We can also check if a specific clause is satisfied by an assignment
first_clause = cnf.clause(0)
clause_satisfied = first_clause.is_satisfied({1: True, 2: True, 3: True})
print(f"First claused satisifed by x1 = x2 = x3 = true: {clause_satisfied}")

# Using the sat_solver module we can check if a CNF is satisfiable
print(f"Satisfiable: {is_satisfiable(cnf)}")

# Get a valid assignment for the CNF, will return None if it is unsatisfiable
assignment = solve(cnf)
print(f"A valid assignment: {assignment}")