from advalg.dnf import DNF
from typing import Callable

# 8 assignments
dnf2 = DNF(4)
dnf2.add_clause([1,2])
dnf2.add_clause([-1,-2])

# 28 satisfying assignments
dnf3 = DNF(5)
dnf3.add_clause([1,2])
dnf3.add_clause([-2,3])
dnf3.add_clause([-1])

# 704 satisfying assignments
dnf4 = DNF(10)
dnf4.add_clause([1,2,5,-10])
dnf4.add_clause([-2,3])
dnf4.add_clause([-1])

# 129 assignments bad test doesn't show approximation
dnf5 = DNF(15)
dnf5.add_clause([2,-3,-4,6,10,-12,13,-15])
dnf5.add_clause([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

tests = [
    (dnf2, 8),
    (dnf3, 28),
    (dnf4, 704),
]

samples = [10, 100, 1000]

def test_dnf(counter: Callable[[DNF, int], float]):
    """Tests the given counter function on several DNF formulas"""
    for (dnf, count) in tests:
        print(dnf)
        print(f"actual #sat = {count}")
        for s in samples:
            print(f"approx #sat ({s} iters) = {counter(dnf, s)}")
        print()