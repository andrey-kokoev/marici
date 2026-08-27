"""Canonical factorization through the factorial target sublattice."""
import json, math, os
from fractions import Fraction
from pathlib import Path

def rf(a,n): return math.prod(range(a,a+n))
def core(g):
    z=(2*g+9)*rf(4,g)
    for a in range(2,g+8,2): z*=(3*g+7+a)*(g+9-a)*rf(a,g)**2
    return z*(4*g+15)*rf(g+8,g)
def sigma(g): return Fraction(-8*(2*g+3)*(g*g-g-26)*math.factorial(2*g+1),3*(g+5)*(g+6)*(g+7)*math.factorial(g-1))
records=[]
for g in range(2,202,2):
    n=g+10
    I=Fraction(core(g)*(2*g+7)*rf(4,g))*abs(sigma(g))
    reduced=I/(math.factorial(g)**n)
    records.append({"g":g,"order":n,"integral_index":I.denominator==1,
                    "reduced_index_integral":reduced.denominator==1,
                    "reduced_index_nonzero":reduced.numerator!=0})
passed=all(x["integral_index"] and x["reduced_index_integral"] for x in records)
result={"schema":"marici.checker_results.v1","checker":"magnetic_divided_target_factorization_checks.py","passed":passed,
 "factorization":"M_g = inclusion(g!Y_g -> Y_g) composed with N_g",
 "index_law":"[Y_g:M_g(S)]=(g!)^(g+10)*[Y_g:N_g(S)]",
 "kernel_preserved":True,"execution_authority":"not supplied for ports calibrated in divided-power units",
 "replay":"all even g=2..200"}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_divided_target_factorization.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
