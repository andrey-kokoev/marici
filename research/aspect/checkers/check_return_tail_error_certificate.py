"""Exact perturbative closure of finite normalized-return approximations."""
from fractions import Fraction as F
from pathlib import Path
import json

cases={"strict":(F(3,5),F(1,10)),"boundary":(F(4,5),F(1,5)),"failed":(F(9,10),F(1,5))}
rows={}
for name,(q,e) in cases.items():
 total=q+e; margin=1-total*total
 rows[name]={"approx_norm":str(q),"tail_error":str(e),"certified_total":str(total),"return_margin_lower":str(margin),"strict":total<1}
checks={"strict_certificate_positive":rows["strict"]["strict"] and F(rows["strict"]["return_margin_lower"])==F(51,100),"boundary_has_zero_margin":not rows["boundary"]["strict"] and rows["boundary"]["return_margin_lower"]=="0","failed_bound_detected":not rows["failed"]["strict"],"aligned_error_saturates_triangle":F(rows["strict"]["certified_total"])==F(7,10)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cases":rows,"criterion":"approximation norm plus certified omitted-tail norm is strictly below one"}
out=Path("research/aspect/results/return_tail_error_certificate.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
