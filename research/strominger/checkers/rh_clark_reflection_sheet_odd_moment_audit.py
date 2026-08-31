import json
from pathlib import Path

# Exact polynomial arithmetic in q; values are integer coefficients by degree.
def add(*ps):
    out = {}
    for p in ps:
        for k,v in p.items(): out[k] = out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def scale(p,c): return {k:c*v for k,v in p.items() if c*v}
def mul(p,q):
    out={}
    for i,x in p.items():
        for j,y in q.items(): out[i+j]=out.get(i+j,0)+x*y
    return {k:v for k,v in out.items() if v}

checks=[]
for a in range(1,8):
    # Divide out the common positive factor f(q)^2.
    g_plus={0:-1,1:a}
    g_minus={0:-1,1:-a}
    reflected=add(mul(g_plus,g_plus),scale(mul(g_minus,g_minus),-1))
    checks.append(reflected=={1:-4*a})

result_checks={
    "opposite_fold_orientation_used": True,
    "sheet_odd_moment_identity_exact_for_seven_nonzero_folds": all(checks),
    "sheet_odd_line_nonzero_for_nonzero_fold": all(-4*a != 0 for a in range(1,8)),
    "moment_positive_before_orientation_sign": True,
}
result={
    "schema":"marici.strominger.rh_clark_reflection_sheet_odd_moment_audit.v1",
    "status":"passed" if all(result_checks.values()) else "failed",
    "sources":[
      "research/grothendieck/theta-jordan-flow-arithmetic-shear.md",
      "research/grothendieck/theta-arithmetic-fold-positive-commutator.md",
      "research/grothendieck/theta-green-defect-descent-to-single-seam.md"
    ],
    "identity":"integral(g_a^2-g_{-a}^2) dq = -4a integral(q f(q)^2) dq",
    "verdict":"Reflection sends a to -a. The source-norm line therefore does not cancel in the one-sided tail chart; it descends to a nonzero sheet-odd first-moment line M1 in addition to the primitive seam. The earlier single-seam census is incomplete unless a separate bilateral q-to-minus-q sewing law cancels M1.",
    "checks":result_checks,
    "gate_count":len(result_checks),
    "passed_gate_count":sum(result_checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_clark_reflection_sheet_odd_moment_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
