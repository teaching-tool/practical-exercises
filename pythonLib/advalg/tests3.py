from advalg.dnf import DNF

# 1 assignment not good test
dnf1 = DNF(3)
dnf1.add_clause([1,2,3])

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
    (dnf1, 1),
    (dnf2, 8),
    (dnf3, 28),
    (dnf4, 704),
    (dnf5, 129)
]

samples = [10, 100, 1000]

def test_dnf(counter):
    """
    Tests the given counter function on several DNF formulas.
    """
    for (dnf, count) in tests:
        print(dnf)
        print(f"actual #sat = {count}")
        for s in samples:
            print(f"approx #sat ({s} iters) = {counter(dnf, s)}")
        print()

# This is only for testing
def brute_count(dnf):
    """
    Uses brute force to count number of satisfying assignments in the given dnf.
    Will be moved to some kind of brute force module.
    """
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
