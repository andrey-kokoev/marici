"""Exact base/remainder coherence budgets for total route norm."""
from fractions import Fraction as F
from pathlib import Path
import json

q=F(3,5); g=F(2,5)
cases={"orthogonal":F(0),"partial":F(1,2),"aligned":F(1)}
rows={}
for name,k in cases.items():
 total2=q*q+2*k*q*g+g*g; margin=1-total2
 rows[name]={"coherence":str(k),"total_norm_squared_bound":str(total2),"return_margin_lower":str(margin),"strict":total2<1}
checks={"orthogonal_margin":rows["orthogonal"]["return_margin_lower"]=="12/25","partial_margin":rows["partial"]["return_margin_lower"]=="6/25","aligned_is_terminal":not rows["aligned"]["strict"] and rows["aligned"]["return_margin_lower"]=="0","coherence_monotone":F(rows["orthogonal"]["total_norm_squared_bound"])<F(rows["partial"]["total_norm_squared_bound"])<F(rows["aligned"]["total_norm_squared_bound"])}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"cases":rows,"conclusion":"the total route gate depends on base-remainder coherence; orthogonality gives a root-sum-square bound while alignment saturates the triangle bound"}
out=Path("research/aspect/results/base_remainder_coherence.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
