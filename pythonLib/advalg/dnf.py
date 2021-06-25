from typing import List, Dict, Iterable, Set, Iterator

class DNFClause:
    """Represents a clause in a logical formula in DNF"""
    def __init__(self, literals: Iterable[int]):
        """
        Constructs a clause with the given literals.
        Positive integers correspond to variables and negative integers correspond to negated variables.
        """
        self._literals = set(literals)
    
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """Is the clause satisfied by the given assignment?"""
        for lit in self._literals:
            if (abs(lit) not in assignment) or \
               (lit > 0 and not assignment[lit]) or \
               (lit < 0 and assignment[-lit]):
                    return False
        return True

    def __len__(self) -> int:
        """Returns the number of literals in the clause"""
        return len(self._literals)

    def __iter__(self) -> Iterator[int]:
        """Returns an iterator for the literals of the clause"""
        return iter(self._literals)

    def literals(self) -> Set[int]:
        """Returns the set of literals in the clause"""
        return set(self._literals)

    def _lit_str(self,literal):
        if literal > 0: return f"x{literal}"
        return f"!x{-literal}"

    def __repr__(self):
        s = "("
        for i,lit in enumerate(sorted(self._literals, key=abs)):
            if i == 0: s += f"{self._lit_str(lit)}"
            else: s += f" & {self._lit_str(lit)}"
        s += ")"
        return s

class DNF:
    """Represents a logical formula in Disjunctive Normal Form"""
    def __init__(self, var_count: int):
        """Constructs a DNF with variables x1,x2,...,x(var_count)"""
        self._var_count = var_count
        self._clauses = []

    def clause_count(self) -> int:
        """Returns the number of clauses in the formula"""
        return len(self._clauses)

    def var_count(self) -> int:
        """Returns the number of variables in the formula"""
        return self._var_count

    def clause(self, i: int) -> DNFClause:
        """Returns the clause with index i"""
        assert(0 <= i < self.clause_count())
        return self._clauses[i]

    def clauses(self) -> List[DNFClause]:
        """Returns a list with all clauses in the formula"""
        return list(self._clauses)

    def add_clause(self, literals: Iterable[int]) -> None:
        """
        Add a clause with the given literals.
        Positive integers correspond to variables and negative integers correspond to negated variables.
        """
        for literal in literals:
            assert(1 <= abs(literal) <= self.var_count())
        self._clauses.append(DNFClause(literals))

    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """Is this DNF formula satisfied by the given assignment?"""
        if self.clause_count() == 0:
            return True
        return any([c.is_satisfied(assignment) for c in self._clauses])
    
    def __repr__(self):
        s = f"DNF object: {self.var_count()} variables {self.clause_count()} clauses"
        for i,c in enumerate(self.clauses()):
            if i == 0: s += f"\n{c}"
            else: s += f" |\n{c}"
        return s
