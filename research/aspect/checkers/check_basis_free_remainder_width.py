"""Exact coordinate-rescaling audit for omitted-route lift budgets."""
from fractions import Fraction as F
from pathlib import Path
import json

# Physical admissible displacement is |w|<=2 and R(w)=w/10.
scales=[F(1),F(2),F(1,2),F(5)]
rows=[]
for alpha in scales:
 # basis v'=alpha v, coefficient radius M'=2/alpha, operator norm epsilon'=alpha/10
 M=F(2)/alpha; eps=alpha/F(10); width=M*eps
 rows.append({"basis_scale":str(alpha),"coordinate_radius":str(M),"coordinate_operator_bound":str(eps),"product_width":str(width)})
checks={"width_invariant_under_rescaling":len({r["product_width"] for r in rows})==1,"invariant_width_exact":rows[0]["product_width"]=="1/5","radius_alone_is_not_invariant":len({r["coordinate_radius"] for r in rows})>1,"operator_bound_alone_is_not_invariant":len({r["coordinate_operator_bound"] for r in rows})>1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"rescalings":rows,"conclusion":"the physical budget is the support width sup ||Rw|| over admissible lift displacements, not a coordinate radius or operator coefficient separately"}
out=Path("research/aspect/results/basis_free_remainder_width.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
