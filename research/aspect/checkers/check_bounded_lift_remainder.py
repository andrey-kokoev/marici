"""Exact margin budget for bounded lift torsors and omitted route maps."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={"strict":(F(1,2),F(1,10),F(2)),"boundary":(F(3,5),F(1,10),F(4)),"failed":(F(3,4),F(1,5),F(2))}
rows={}
for name,(q,e,m) in cases.items():
 total=q+e*m; margin=1-total*total
 rows[name]={"base_norm":str(q),"remainder_on_torsor":str(e),"torsor_radius":str(m),"total_bound":str(total),"return_margin":str(margin),"strict":total<1}
checks={"strict_budget_passes":rows["strict"]["strict"] and rows["strict"]["return_margin"]=="51/100","boundary_zero_margin":not rows["boundary"]["strict"] and rows["boundary"]["return_margin"]=="0","failed_budget_detected":not rows["failed"]["strict"],"nonzero_remainder_needs_finite_radius":F(rows["strict"]["remainder_on_torsor"])>0}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"base route norm plus remainder norm on torsor times admissible torsor radius is below one","checks":checks,"cases":rows}
out=Path("research/aspect/results/bounded_lift_remainder.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
