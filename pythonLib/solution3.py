from random import random
from itertools import accumulate
from advalg.dnf import DNF
from advalg.tests3 import test_dnf

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

#Testing
test_dnf(approx_count)