"""Exact rational audit of the sharp two-grade positive-return contraction gate."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={
 "strict":{"a":F(1,2),"b":F(1,3),"z2":F(1,16),"expect":True},
 "unit_boundary":{"a":F(1,2),"b":F(1,2),"z2":F(1,4),"expect":False},
 "diagonal_failure":{"a":F(1),"b":F(1,4),"z2":F(0),"expect":False},
 "mixed_failure":{"a":F(3,4),"b":F(3,4),"z2":F(1,4),"expect":False},
}
rows={}
for name,c in cases.items():
 a,b,z2=c["a"],c["b"],c["z2"]
 positive=a>=0 and b>=0 and z2<=a*b
 strict=positive and a<1 and b<1 and z2<(1-a)*(1-b)
 rows[name]={"positive_K":positive,"strict_contraction":strict,"expected":c["expect"],"mixed_slack":str((1-a)*(1-b)-z2),"pass":strict==c["expect"]}
checks={
 "all_cases_match_sharp_criterion":all(r["pass"] for r in rows.values()),
 "unit_boundary_has_zero_slack":rows["unit_boundary"]["mixed_slack"]=="0",
 "mixed_loading_can_fail_below_unit_diagonals":not rows["mixed_failure"]["strict_contraction"],
 "strict_example_has_positive_slack":F(rows["strict"]["mixed_slack"])>0,
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"a<1, b<1, |z|^2<(1-a)(1-b), with K positive","checks":checks,"cases":rows}
out=Path("research/aspect/results/sharp_two_grade_return_margin.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
