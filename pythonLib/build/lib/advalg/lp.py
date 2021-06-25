import os
import re
import subprocess
from typing import List, Tuple, Dict

class LPEntity:
    def __le__(self, right: float) -> "ConstraintLE":
        return ConstraintLE(LinearFunc(self.terms()), right)

    def __ge__(self, right: float) -> "ConstraintGE":
        return ConstraintGE(LinearFunc(self.terms()), right)

    def __add__(self, other: "LPEntity") -> "LinearFunc":
        return LinearFunc(self.terms() + other.terms())

    def __sub__(self, other: "LPEntity") -> "LinearFunc":
        return self + (-other)

    def __neg__(self) -> "LinearFunc":
        return self * -1

    def __mul__(self, m: float) -> "LinearFunc":
        return LinearFunc([(m*c, x) for (c,x) in self.terms()])

    def __rmul__(self, m: float) -> "LinearFunc":
        return self * m

#List of tuples (constant, var_number)
class LinearFunc(LPEntity):
    def __init__(self, ts: List[Tuple[float, int]] = None):
        self.ts = ts if ts is not None else []

    @staticmethod
    def sum(vars: List["Var"]) -> "LinearFunc":
        return LinearFunc([(1, v.x) for v in vars])

    def __repr__(self):
        s = ""
        for i,(c,x) in enumerate(self.ts):
            if i == 0: s += f"{c}*x{x}"
            elif c < 0: s += f" - {-c}*x{x}"
            else: s += f" + {c}*x{x}"
        return s

    def terms(self) -> List[Tuple[float, int]]:
        return list(self.ts)

    def to_lp(self) -> str:
        lp_str = ""
        for i,(c,x) in enumerate(self.ts):
            if i == 0: lp_str += f"{c} x{x}"
            else: lp_str += f" {c} x{x}"
        return lp_str

# Just var_number
class Var(LPEntity):
    def __init__(self, x: int):
        self.x = x

    def terms(self) -> List[Tuple[float, int]]:
        return [(1, self.x)]
    
    def to_lp(self) -> str:
        return f"1 x{self.x}"
    
    def __repr__(self):
        return f"x{self.x}"

# Takes a termlist (])
class Minimize:
    def __init__(self, lin_func: LPEntity):
        self.lin_func = lin_func

    def __repr__(self):
        return f"Minimize({self.lin_func})"

    def to_lp(self) -> str:
        return f"min: {self.lin_func.to_lp()}"

class Maximize:
    def __init__(self, lin_func: LPEntity):
        self.lin_func = lin_func

    def __repr__(self):
        return f"Maximize({self.lin_func})"

    def to_lp(self) -> str:
        return f"max: {self.lin_func.to_lp()};"
        
class ConstraintLE:
    def __init__(self, left: LPEntity, right: float):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} <= {self.right}"

    def to_lp(self) -> str:
        return f"{self.left.to_lp()} <= {self.right}"

class ConstraintGE:
    def __init__(self, left: LPEntity, right: float):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} >= {self.right}"

    def to_lp(self) -> str:
        return f"{self.left.to_lp()} >= {self.right}"

class LPResult:
    def __init__(self, obj_value: float, variables: Dict[int, float]):
        self.obj_value = obj_value
        self.variables = variables

class LP:
    def __init__(self, variables: List[Var], objective):
        self.variables = variables
        self.objective = objective
        self.constraints = []

    def add_constraint(self, constraint) -> None:
        self.constraints.append(constraint)

    def solve(self) -> LPResult:
        in_file = "lp_in.txt"
        lp_str = self.to_lp()

        with open(in_file, "w") as fp:
            fp.write(lp_str)

        command = f"lp_solve < {in_file}"
        res = subprocess.run(command, shell = True, capture_output=True, text = True)
        os.remove(in_file)
        return self.parse_output(res.stdout)

    def parse_output(self, output:str) -> LPResult:
        number = r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
        
        if re.search("This problem is infeasible", output):
            return None

        obj_match = re.search(rf"Value of objective function: ({number})", output)
        obj_value = float(obj_match.group(1))

        variables = {}
        for line in output.splitlines():
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

def variables(n: int) -> List[Var]:
    return [Var(i) for i in range(n)]