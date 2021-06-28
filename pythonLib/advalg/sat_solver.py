import os
import re
import subprocess
from typing import Tuple, Dict
from advalg.cnf import CNF

def is_satisfiable(cnf: CNF) -> bool:
    """Is the given CNF formula satisfiable?"""
    return solve(cnf) is not None

def solve(cnf: CNF) -> Dict[int, int]:
    """Returns a solution to cnf if it is satisfiable, otherwise None"""
    in_file = "cnf_in.cnf"
    out_file = "cnf_out.cnf"

    with open(in_file, "w") as fp:
        fp.write(to_cnf_format(cnf))

    command = f"minisat {in_file} {out_file}"
    subprocess.run(command, shell=True, capture_output=True)
    solution = parse_output(out_file)

    os.remove(in_file)
    os.remove(out_file)

    return solution

def parse_output(out_file: str) -> Tuple[bool, Dict[int, bool]]:
    with open(out_file, "r") as fp:
        lines = fp.readlines()

        if lines[0].startswith("UNSAT"):
            return None

        lits = [int(s) for s in lines[1].split(" ")][:-1]
        return {abs(l): l>0 for l in lits}

def to_cnf_format(cnf: CNF) -> str:
    """Returns a DIMACS CNF string representation of cnf"""
    s = f"p cnf {cnf.var_count()} {cnf.clause_count()}\n"

    for c in cnf.clauses():
        s += " ".join([str(l) for l in c]) + " 0\n"
        
    return s

def parse_clause(string: str):
    """Parse a CNF clause"""
    return [int(l) for l in string.split(" ")][:-1]

def parse_cnf(string: str) -> CNF:
    """Returns a CNF object from the given string representation"""
    lines = [l for l in string.splitlines() if not l.startswith("c")]
    match = re.match(r'p cnf (\d+) (\d+)', lines[0])
    assert(match is not None)
    
    n = int(match.group(1))
    m = int(match.group(2))
    cnf = CNF(n)

    for i in range(m):
        cnf.add_clause(parse_clause(lines[i+1]))
    
    return cnf