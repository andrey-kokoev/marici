"""Exact rational cases for the reciprocal Hermitian Pauli return region."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={
 "strict_mixed":(F(1,2),F(3,10),F(0),F(3,10)),
 "terminal_mixed":(F(1,2),F(3,10),F(2,5),F(1,2)),
 "positive_superunit":(F(3,4),F(3,5),F(0),F(3,5)),
 "nonpositive":(F(1,5),F(3,10),F(0),F(3,10)),
}
rows={}
for name,(a,x,z,r) in cases.items():
 radial_exact=r*r==x*x+z*z
 positive=a>=r
 strict=positive and a+r<1
 rows[name]={"a":str(a),"x":str(x),"z":str(z),"radius":str(r),"radial_exact":radial_exact,"positive":positive,"largest_eigenvalue":str(a+r),"strict_return":strict,"cross_grade_mixing":x!=0}
checks={"all_radii_exact":all(v["radial_exact"] for v in rows.values()),"strict_reciprocal_mixing_exists":rows["strict_mixed"]["strict_return"] and rows["strict_mixed"]["cross_grade_mixing"],"terminal_boundary_detected":rows["terminal_mixed"]["largest_eigenvalue"]=="1" and not rows["terminal_mixed"]["strict_return"],"positivity_and_contraction_are_distinct":rows["positive_superunit"]["positive"] and not rows["positive_superunit"]["strict_return"],"nonpositive_case_rejected":not rows["nonpositive"]["positive"]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"positive iff a>=sqrt(x^2+z^2); strict return iff additionally a+sqrt(x^2+z^2)<1","checks":checks,"cases":rows}
out=Path("research/aspect/results/positive_reciprocal_pauli_region.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
