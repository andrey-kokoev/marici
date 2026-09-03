"""Exact dual-form width for quadratic lift admissibility."""
from fractions import Fraction as F
from pathlib import Path
import json

H=(F(4),F(9)); r=(F(1),F(1)); u=(r[0]/H[0],r[1]/H[1])
hnorm=H[0]*u[0]*u[0]+H[1]*u[1]*u[1]
route_u=r[0]*u[0]+r[1]*u[1]
width2=route_u*route_u/hnorm
dual=r[0]*r[0]/H[0]+r[1]*r[1]/H[1]
axis_width2=max(r[0]*r[0]/H[0],r[1]*r[1]/H[1])
checks={"dual_formula_exact":width2==dual==F(13,36),"dual_extremizer_saturates":route_u==hnorm,"mixed_direction_exceeds_each_axis":width2>axis_width2,"quadratic_form_is_positive":H[0]>0 and H[1]>0}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"squared_width":str(width2),"axis_only_squared_width":str(axis_width2),"dual_vector":[str(x) for x in u],"conclusion":"ellipsoidal admissibility width is the dual-form norm, and axis tests can miss the maximizing mixed lift"}
out=Path("research/aspect/results/ellipsoid_remainder_width.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
