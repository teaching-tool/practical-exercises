class DNF:
    def __init__(self, var_count):
        self._var_count = var_count
        self._clauses = []

    def clause_count(self):
        return len(self._clauses)

    def var_count(self):
        return self._var_count

    def clause(self, i):
        assert(0 <= i < self.clause_count())
        return self._clauses[i]

    def clauses(self):
        return [self.clause(i) for i in range(self.clause_count())]

    def add_clause(self, clause):
        for literal in clause:
            assert(1 <= abs(literal) <= self.var_count())
        self._clauses.append(Clause(clause))

    def is_satisfied(self, assignment):
        return any([c.is_satisfied(assignment) for c in self._clauses])

class Clause:
    def __init__(self, literals):
        self._literals = set(literals)
    
    # TODO fix for partial assignments
    def is_satisfied(self, assignment):
        for lit in self._literals:
            if lit > 0 and not assignment[lit] or \
               lit < 0 and assignment[-lit]: return False
        return True

    def __len__(self):
        return len(self._literals)

    def __iter__(self):
        return iter(self._literals)