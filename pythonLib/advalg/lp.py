import os
import re

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

    def to_lp(self):
        lp_str = ""
        for i,(c,x) in enumerate(self.ts):
            if i == 0: lp_str += f"{c} x{x}"
            else: lp_str += f" {c} x{x}"
        return lp_str

class Var(LPEntity):
    def __init__(self, x: int):
        self.x = x

    def terms(self):
        return [(1, self.x)]
    
    def to_lp(self):
        return f"1 x{self.x}"

class Minimize:
    def __init__(self, termlist: LPEntity):
        self.termlist = termlist

    def __repr__(self):
        return f"Minimize({self.termlist})"

    def to_lp(self):
        return f"min: {self.termlist.to_lp()}"

class Maximize:
    def __init__(self, termlist: LPEntity):
        self.terms = termlist.terms()

    def to_lp(self):
        return f"max: {self.termlist.to_lp()};"
        
class ConstraintLE:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} <= {self.right}"

    def to_lp(self):
        return f"{self.left.to_lp()} <= {self.right}"

class ConstraintGE:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} >= {self.right}"

    def to_lp(self):
        return f"{self.left.to_lp()} >= {self.right}"

class LPResult:
    def __init__(self, obj_value, variables):
        self.obj_value = obj_value
        self.variables = variables

class LP:
    def __init__(self, variables, objective):
        self.variables = variables
        self.objective = objective
        self.constraints = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def solve(self):
        in_file = "lp_in.txt"
        out_file = "lp_out.txt"
        lp_str = self.to_lp()

        with open(in_file, "w") as fp:
            fp.write(lp_str)

        os.system(f"lp_solve < {in_file} > {out_file}")
        res = self.parse_output(out_file)
        
        os.remove(in_file)
        os.remove(out_file)

        return res

    def parse_output(self, out_file):
        number = r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'

        with open(out_file, "r") as fp:
            lines = fp.readlines()
            output = ''.join(lines)
            if re.search("This problem is infeasible", output):
                return None

            obj_match = re.search(rf"Value of objective function: ({number})", output)
            obj_value = float(obj_match.group(1))

            variables = {}
            for line in lines:
                match = re.match(rf'x(\d+)\s+({number})', line)
                if match:
                    var = int(match.group(1))
                    val = float(match.group(2))
                    variables[var] = val

            return LPResult(obj_value, variables)

    def to_lp(self):
        lp_str = f"{self.objective.to_lp()};"
        for c in self.constraints:
            lp_str += f"\n{c.to_lp()};"
        return lp_str

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