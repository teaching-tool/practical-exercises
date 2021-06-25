from random import random
from advalg.dnf import DNF, DNFClause
from advalg.tests3 import test_dnf

# Check the documentation for DNF and DNFClause before you begin

# Implement the approx_count function
def approx_count(dnf: DNF, sample_count: int) -> float:
    """Estimates number of valid assignments for the given dnf using sample_count samples"""
    pass

# The function call below tests your implementation on 4 formulas in DNF
test_dnf(approx_count)