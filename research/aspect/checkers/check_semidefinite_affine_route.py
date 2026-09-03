"""Exact nullspace gate for semidefinite affine-route admissibility."""
from fractions import Fraction as F
from pathlib import Path
import json

b=F(1,2); r_support=F(1,4); r_null_good=F(0); r_null_bad=F(1,10)
# H=diag(1,0): x is bounded by one, y is unconstrained.
finite_endpoint=max((b+r_support*x+r_null_good*y)**2 for x in (F(-1),F(1)) for y in (F(0),F(20)))
bad_values=[(b+r_null_bad*y)**2 for y in (F(0),F(10),F(20))]
checks={"reduced_support_bound_exact":finite_endpoint==F(9,16),"null_killed_route_is_independent_of_null_coordinate":r_null_good==0,"route_visible_null_direction_grows":bad_values[0]<bad_values[1]<bad_values[2],"route_visible_null_exceeds_unit":bad_values[-1]>1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"reduced_support_max_squared":str(finite_endpoint),"bad_null_sequence":[str(x) for x in bad_values],"conclusion":"for semidefinite admissibility, a finite affine-route bound exists only if the route kills every admissibility-null direction before support reduction"}
out=Path("research/aspect/results/semidefinite_affine_route.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
