from functools import reduce
from scipy.optimize import linprog

class LPEntity:
    def __le__(self, right):
        return ConstraintLE(TermList(self.terms()), right)

    def __ge__(self, right):
        return ConstraintGE(TermList(self.terms()), right)

    # More constraints?

    def __add__(self, other):
        return TermList(self.terms() + other.terms())

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return self * -1

    def __mul__(self, m: float):
        return TermList([(m*c, x) for (c,x) in self.terms()])

    def __rmul__(self, m: float):
        return self * m

class TermList(LPEntity):
    def __init__(self, ts):
        self.ts = ts

    def __repr__(self):
        s = ""
        for i,(c,x) in enumerate(self.ts):
            if i == 0: s += f"{c}*x{x}"
            elif c < 0: s += f" - {-c}*x{x}"
            else: s += f" + {c}*x{x}"
        return s

    def terms(self):
        return list(self.ts)

class Var(LPEntity):
    def __init__(self, x: int):
        self.x = x

    def terms(self):
        return [(1, self.x)]

class Minimize:
    def __init__(self, termlist: LPEntity):
        self.terms = termlist.terms()

    def coeff_vector(self, var_count):
        vec = [0 for i in range(var_count)]

        for (c,x) in self.terms:
            vec[x] = c

        return vec

    def __repr__(self):
        return f"Minimize({self.terms})"

class Maximize:
    def __init__(self, termlist: LPEntity):
        self.terms = termlist.terms()

    def coeff_vector(self, var_count):
        vec = [0 for i in range(var_count)]

        for (c,x) in self.terms:
            vec[x] = -c

        return vec
        
class ConstraintLE:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_equality(self):
        return False

    def coeffs(self, var_count):
        vec = [0 for i in range(var_count)]

        for (c,x) in self.left.terms():
            vec[x] = c

        return vec, self.right
    
    def __repr__(self):
        return f"{self.left} <= {self.right}"

class ConstraintGE:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_equality(self):
        return False

    def coeffs(self, var_count):
        vec = [0 for i in range(var_count)]

        for (c,x) in self.left.terms():
            vec[x] = -c

        return vec, -self.right
    
    def __repr__(self):
        return f"{self.left} >= {self.right}"

class LP:
    def __init__(self, variables, objective):
        self.variables = variables
        self.objective = objective
        self.constraints = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def solve(self):
        n = len(self.variables)
        obj = self.objective.coeff_vector(n)

        if len(self.constraints) == 0:
            return linprog(obj, A_ub=None, b_ub=None, method='revised simplex')

        A_ub, b_ub = [], []
        for c in self.constraints:
            coeff, cst = c.coeffs(n)
            if c.is_equality():
                A_eq.append(coeff)
                b_eq.append(cst)
            else:
                A_ub.append(coeff)
                b_ub.append(cst)

        return linprog(obj, A_ub=A_ub, b_ub=b_ub, method='revised simplex')

    def __repr__(self):
        n = len(self.variables)
        m = len(self.constraints)
        s = f"LP Object: {n} variables, {m} constraints"
        for i,v in enumerate(self.variables):
            if i == 0: s += f"\nVariables: x{v.x}"
            else: s += f", x{v.x}"
        s += "\nConstraints:"

        for c in self.constraints:
            s += f"\n{c}"

        return s