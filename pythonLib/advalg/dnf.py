from typing import List, Dict, Iterable

class Clause:
    def __init__(self, literals: Iterable[int]):
        self._literals = set(literals)
    
    # TODO fix for partial assignments
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        for lit in self._literals:
            if lit > 0 and not assignment[lit] or \
               lit < 0 and assignment[-lit]: return False
        return True

    def __len__(self):
        return len(self._literals)

    def __iter__(self):
        return iter(self._literals)

    def __repr__(self):
        s = "("
        for i,lit in enumerate(sorted(self._literals, key=abs)):
            if i == 0: s += f"{lit}"
            else: s += f", {lit}"
        s += ")"
        return s

class DNF:
    def __init__(self, var_count: int):
        self._var_count = var_count
        self._clauses = []

    def clause_count(self) -> int:
        return len(self._clauses)

    def var_count(self) -> int:
        return self._var_count

    def clause(self, i: int) -> Clause:
        assert(0 <= i < self.clause_count())
        return self._clauses[i]

    def clauses(self) -> List[Clause]:
        return [self.clause(i) for i in range(self.clause_count())]

    def add_clause(self, literals: Iterable[int]) -> None:
        for literal in literals:
            assert(1 <= abs(literal) <= self.var_count())
        self._clauses.append(Clause(literals))

    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        if self.clause_count() == 0:
            return True
        return any([c.is_satisfied(assignment) for c in self._clauses])
    
    def __repr__(self):
        s = f"DNF vars={self.var_count()} "
        for i,c in enumerate(self.clauses()):
            if i == 0: s += f"{c}"
            else: s += f", {c}"
        return s
