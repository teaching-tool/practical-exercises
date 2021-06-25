from typing import List, Iterable, Dict

class CNFClause:
    def __init__(self, literals: Iterable[int]):
        self._literals = set(literals)

    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        for lit in self._literals:
            if abs(lit) not in assignment:
                continue
            if (lit > 0 and assignment[lit]) or (lit < 0 and not assignment[lit]):
                return True
        return False

    def __len__(self):
        return len(self._literals)

    def __iter__(self):
        return iter(self._literals)

    def _lit_str(self,literal):
        if literal > 0: return f"x{literal}"
        return f"!x{-literal}"

    def __repr__(self):
        s = "("
        for i,lit in enumerate(sorted(self._literals, key=abs)):
            if i == 0: s += f"{self._lit_str(lit)}"
            else: s += f" | {self._lit_str(lit)}"
        s += ")"
        return s

class CNF:
    def __init__(self, var_count):
        self._var_count = var_count
        self._clauses = []

    def clause_count(self) -> int:
        return len(self._clauses) 

    def var_count(self) -> int:
        return self._var_count

    def clause(self, i: int) -> CNFClause:
        assert(0 <= i < self.clause_count())
        return self._clauses[i]

    def clauses(self) -> List[CNFClause]:
        return list(self._clauses)

    def add_clause(self, literals: Iterable[int]) -> None:
        for literal in literals:
            assert(1 <= abs(literal) <= self.var_count())
        self._clauses.append(CNFClause(literals))

    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        if self.clause_count() == 0:
            return True
        return all([c.is_satisfied(assignment) for c in self._clauses])

    def __repr__(self):
        s = f"CNF object: {self.var_count()} variables {self.clause_count()} clauses"
        for i,c in enumerate(self.clauses()):
            if i == 0: s += f"\n{c}"
            else: s += f" &\n{c}"
        return s