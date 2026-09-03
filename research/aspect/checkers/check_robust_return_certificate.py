"""Exact rational audit of robust reciprocal Pauli return certificates."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={
 "strict_box":(F(2,5),F(1,2),F(3,10),F(0),F(3,10)),
 "terminal_box":(F(1,2),F(1,2),F(3,10),F(2,5),F(1,2)),
 "positivity_failure":(F(1,4),F(1,2),F(3,10),F(2,5),F(1,2)),
 "mixing_only_failure":(F(0),F(1),F(0),F(0),F(0)),
}
rows={}
for name,(amin,A,X,Z,rho) in cases.items():
 exact=rho*rho==X*X+Z*Z
 positive=amin>=rho
 strict=A+rho<1
 rows[name]={"a_min":str(amin),"A":str(A),"X":str(X),"Z":str(Z),"rho":str(rho),"radial_exact":exact,"robust_positive":positive,"robust_strict":strict,"upper_norm":str(A+rho)}
checks={"all_radii_exact":all(v["radial_exact"] for v in rows.values()),"strict_box_certified":rows["strict_box"]["robust_positive"] and rows["strict_box"]["robust_strict"],"terminal_corner_detected":rows["terminal_box"]["robust_positive"] and rows["terminal_box"]["upper_norm"]=="1" and not rows["terminal_box"]["robust_strict"],"positivity_requires_lower_load":not rows["positivity_failure"]["robust_positive"],"zero_mixing_alone_does_not_certify":not rows["mixing_only_failure"]["robust_strict"]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"rho=sqrt(X^2+Z^2); robust positivity iff a_min>=rho; robust strict return iff A+rho<1","checks":checks,"cases":rows}
out=Path("research/aspect/results/robust_return_certificate.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
