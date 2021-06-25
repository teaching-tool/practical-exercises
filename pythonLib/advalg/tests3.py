from advalg.dnf import DNF
from typing import Callable, List
import random
import matplotlib.pyplot as plt
import numpy as np

def random_dnf(vars: int, clauses: int, clause_size: int) -> DNF:
    dnf = DNF(vars)

    for i in range(clauses):
        clause = set()
        while len(clause) < clause_size:
            x = random.randint(1, vars)
            if x in clause or -x in clause:
                continue
            clause.add(x if random.random() < 0.5 else -x)
        dnf.add_clause(clause)
    
    return dnf
    
random.seed(1)

tests = [
    (random_dnf(10, 4, 2), 688),
    (random_dnf(12, 6, 3), 2240),
    (random_dnf(14, 8, 4), 6992),
    (random_dnf(16, 10, 5), 17408),
]

samples = np.arange(10, 100000, 10)

def results(counter: Callable[[DNF, int], float], dnf: DNF) -> List[float]:
    step = 10
    res = [counter(dnf, step) for s in samples]
    for i in range(1, len(res)):
        n = i+1
        res[i] = (1/n) * res[i] + ((n-1)/n) * res[i-1]
    return res

def test_dnf(counter: Callable[[DNF, int], float]):
    """
    Tests the given counter function on 4 different DNF formulas.
    Plots the output of your implementation and compares with actual result.
    """
    fig, axs = plt.subplots(2,2)
    fig.set_size_inches(8,6)
    fig.canvas.manager.set_window_title("DNF Tests")

    for i in range(4):
        dnf, count = tests[i]
        ax = axs[i//2, i%2]
        y = results(counter, dnf)
        ax.plot(samples, y, label="Estimate")
        ax.plot(samples, [count for x in samples], label="Actual")
        ax.set_title(f"DNF Test Case {i} (n = {dnf.var_count()}, m = {dnf.clause_count()})")
        ax.set_xscale("log")
        ax.legend()

    for i in range(4):
        dnf, count = tests[i]
        print(f"DNF Test Case {i}:")
        print(dnf)
        print(f"{count} Valid Assignments\n")

    plt.tight_layout()
    plt.show()