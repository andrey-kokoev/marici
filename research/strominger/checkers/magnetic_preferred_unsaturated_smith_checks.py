"""Smith form of the source-authorized unsaturated preferred boundary map."""
import json, math, os
from pathlib import Path

def rising(a,n):
    return math.prod(range(a,a+n))

def factorial_valuation(n,p):
    total=0
    while n:
        n//=p; total+=n
    return total

def valuation(n,p):
    total=0
    while n%p==0:
        n//=p; total+=1
    return total

records=[]
for g in range(2,402,2):
    U=rising(4,g); V=rising(g+8,g-1)
    content=math.gcd(2*g+7,3*g+7)*math.gcd(U,V)
    entries=((2*g+7)*U,(2*g+7)*V,(3*g+7)*U,(3*g+7)*V)
    v7_formula=min(factorial_valuation(g+3,7)-factorial_valuation(3,7),
                   factorial_valuation(2*g+6,7)-factorial_valuation(g+7,7))+(1 if g%7==0 else 0)
    records.append({"g":g,"smith_nonzero_invariant":str(content),
                    "equals_entry_gcd":content==math.gcd(*entries),
                    "coefficient_content":str(math.gcd(U,V)),
                    "cocircuit_content":math.gcd(g,7),
                    "v7_formula":v7_formula,"v7_matches":valuation(content,7)==v7_formula})

prefix=os.path.join(Path(__file__).parent,"magnetic_memory_one_checks.py");ns={"__file__":prefix}
exec(compile(open(prefix,encoding="utf-8").read().split("checks = []")[0],prefix,"exec"),ns)
generated=[]
for g in range(2,62,2):
    cols=ns["component"](g,g//2+4,2*g+8)
    boundary=(cols[0].get(0,0),cols[-1].get(0,0),cols[0].get(1,0),cols[-1].get(1,0))
    predicted=int(records[g//2-1]["smith_nonzero_invariant"])
    generated.append(math.gcd(*map(abs,boundary))==predicted)

passed=all(x["equals_entry_gcd"] and x["v7_matches"] for x in records) and all(generated)
result={"schema":"marici.checker_results.v1",
 "checker":"magnetic_preferred_unsaturated_smith_checks.py","passed":passed,
 "smith_form":"diag(h_g,0)",
 "h_g":"gcd(g,7)*gcd((4)^(overline g),(g+8)^(overline(g-1)))",
 "cokernel":"Z direct_sum Z/h_g",
 "prime_law":"v_p(h_g)=min(v_p((g+3)!/3!),v_p((2g+6)!/(g+7)!))+delta_(p=7 and 7|g)",
 "meaning":"This retains the fixed integral source normalization and is the source-authorized boundary arithmetic invariant.",
 "generated_crosscheck":"all even g=2..60","formula_replay":"all even g=2..400"}
Path(__file__).resolve().parents[1].joinpath("results/magnetic_preferred_unsaturated_smith.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
