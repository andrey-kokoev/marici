"""Factorial divisibility and bounded Smith profile of the alternate chart."""
import json, math, os
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

prefix=os.path.join(Path(__file__).parent,"magnetic_memory_one_checks.py");ns={"__file__":prefix}
exec(compile(open(prefix,encoding="utf-8").read().split("checks = []")[0],prefix,"exec"),ns)
records=[]
for g in (2,4,6,8):
    cols=ns["component"](g,g//2+4,2*g+8);rows=[3 if x==1 else x for x in ns["hall_rows"](cols)]
    M=sp.Matrix([[c.get(row,0) for c in cols] for row in rows])
    D=smith_normal_form(M,domain=ZZ); factors=[abs(int(D[i,i])) for i in range(D.rows)]
    records.append({"g":g,"order":len(cols),"entry_gcd":math.gcd(*[abs(int(x)) for x in M]),
                    "entry_gcd_equals_factorial":math.gcd(*[abs(int(x)) for x in M])==math.factorial(g),
                    "all_invariant_factors_nonunit":all(x>1 for x in factors),
                    "all_invariant_factors_divisible_by_factorial":all(x%math.factorial(g)==0 for x in factors),
                    "invariant_factors":[str(x) for x in factors]})
passed=all(x["entry_gcd_equals_factorial"] and x["all_invariant_factors_nonunit"] and x["all_invariant_factors_divisible_by_factorial"] for x in records)
result={"schema":"marici.checker_results.v1","checker":"magnetic_alternate_factorial_smith_checks.py","passed":passed,
 "unbounded_certificate":"For integer a, a^(overline(g-j)) is divisible by (g-j)! and (4-a)^(overline j) by j!. Multiplication by binomial(g,j)=g!/(j!(g-j)!) makes every source coefficient divisible by g!, hence every path-matrix entry is divisible by g!.",
 "consequence":"If the alternate chart has order n, its cokernel surjects onto (Z/g!)^n.",
 "bounded_smith_profiles":"g=2,4,6,8","records":records}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_alternate_factorial_smith.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="records"},indent=2));raise SystemExit(0 if passed else 1)
