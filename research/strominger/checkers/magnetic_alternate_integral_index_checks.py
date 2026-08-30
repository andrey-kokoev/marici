"""Exact image index of the full-rank alternate magnetic chart."""
import json, math, os
from fractions import Fraction
from pathlib import Path
import sympy as sp

def rf(a,n): return math.prod(range(a,a+n))
def core_index(g):
    value=(2*g+9)*rf(4,g)
    for a in range(2,g+8,2):
        value*=(3*g+7+a)*rf(a,g)*(g+9-a)*rf(a,g)
    return value*(4*g+15)*rf(g+8,g)
def transverse(g):
    return Fraction(-8*(2*g+3)*(g*g-g-26)*math.factorial(2*g+1),
                    3*(g+5)*(g+6)*(g+7)*math.factorial(g-1))
def index(g):
    value=Fraction(core_index(g)*(2*g+7)*rf(4,g))*abs(transverse(g))
    assert value.denominator==1
    return value.numerator

prefix=os.path.join(Path(__file__).parent,"magnetic_memory_one_checks.py");ns={"__file__":prefix}
exec(compile(open(prefix,encoding="utf-8").read().split("checks = []")[0],prefix,"exec"),ns)
exact=[]
for g in range(2,22,2):
    cols=ns["component"](g,g//2+4,2*g+8);rows=[3 if x==1 else x for x in ns["hall_rows"](cols)]
    matrix=sp.Matrix([[c.get(row,0) for c in cols] for row in rows])
    exact.append(abs(int(matrix.det()))==index(g))
replay=[index(g)>1 for g in range(2,202,2)]
passed=all(exact) and all(replay)
result={"schema":"marici.checker_results.v1","checker":"magnetic_alternate_integral_index_checks.py",
 "passed":passed,"index_formula":"|det(A_g)|*(2g+7)*(4)^(overline g)*|sigma_g|",
 "sigma_g":"-8(2g+3)(g^2-g-26)(2g+1)!/[3(g+5)(g+6)(g+7)(g-1)!]",
 "classification":{"source_map":"injective over Z","observation_image":"finite-index, not saturated","cokernel":"finite of order equal to the index formula"},
 "exact_generated_determinants":"all even g=2..20","nonunimodular_replay":"all even g=2..200"}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_alternate_integral_index.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
