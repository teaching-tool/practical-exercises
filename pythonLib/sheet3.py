from dnf import DNF
from random import random
from itertools import accumulate

def approx_count(dnf, samples):
    clause_sat = [2 ** (dnf.var_count() - len(c)) for c in dnf.clauses()]
    total_sat = sum(clause_sat)
    clause_prob = [s / total_sat for s in clause_sat]
    success = 0

    for i in range(samples):
        clause_idx = sample_clause(clause_prob)
        assignment = sample_assignment(dnf, clause_idx)
        if good_sample(dnf, clause_idx, assignment):
            success += 1
    
    return total_sat * success / samples

def sample_clause(probs):
    r = random()
    cumulative = accumulate(probs)

    for i,p in enumerate(cumulative):
        if r <= p: return i

def good_sample(dnf, clause_idx, assignment):
    prev_clauses = dnf.clauses()[:clause_idx]
    return not any([c.is_satisfied(assignment) for c in prev_clauses])

def sample_assignment(dnf, clause_idx):
    n = dnf.var_count()
    assignment = {v : random() < 0.5 for v in range(1, n+1)}

    # TODO find better solution
    for lit in dnf.clause(clause_idx):
        if lit > 0: assignment[lit] = True
        if lit < 0: assignment[-lit] = False

    return assignment

# This is only for testing
def brute_count(dnf):
    assignments = [[]]

    for i in range(dnf.var_count()):
        new = []
        for a in assignments:
            new.append(a + [False])
            new.append(a + [True])
        assignments = new

    count = 0
    for a in assignments:
        asn = {(i+1):a[i] for i in range(len(a))}
        if dnf.is_satisfied(asn):
            count += 1

    return count

#TODO move tests to test file
# 28 satisfying assignments
dnf = DNF(5)
dnf.add_clause([1,2])
dnf.add_clause([-2,3])
dnf.add_clause([-1])
print(approx_count(dnf, 100000))

# 704 satisfying assignments
dnf2 = DNF(10)
dnf2.add_clause([1,2,5,-10])
dnf2.add_clause([-2,3])
dnf2.add_clause([-1])
print(approx_count(dnf2, 100000))