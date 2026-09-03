"""Exact rational audit of the optimal two-route Gram certificate."""
from fractions import Fraction as F
from pathlib import Path
import json

# Each case supplies U,V,C and an exact discriminant root D.
cases={
 "strict_correlated":(F(1,2),F(1,2),F(1,4),F(1,2)),
 "strict_rank_one":(F(9,100),F(16,100),F(12,100),F(1,4)),
 "terminal_rank_one":(F(9,25),F(16,25),F(12,25),F(1)),
}
rows={}
for name,(U,V,C,D) in cases.items():
 disc_exact=D*D==(U-V)*(U-V)+4*C*C
 feasible=C*C<=U*V
 lam=(U+V+D)/2
 rows[name]={"U":str(U),"V":str(V),"C":str(C),"D":str(D),"discriminant_exact":disc_exact,"gram_feasible":feasible,"lambda_max":str(lam),"strict":lam<1}
checks={"all_discriminants_exact":all(v["discriminant_exact"] for v in rows.values()),"all_corners_gram_feasible":all(v["gram_feasible"] for v in rows.values()),"correlated_case_strict":rows["strict_correlated"]["lambda_max"]=="3/4" and rows["strict_correlated"]["strict"],"rank_one_strict":rows["strict_rank_one"]["lambda_max"]=="1/4" and rows["strict_rank_one"]["strict"],"rank_one_terminal":rows["terminal_rank_one"]["lambda_max"]=="1" and not rows["terminal_rank_one"]["strict"]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"lambda_max <= (U+V+sqrt((U-V)^2+4 C_eff^2))/2, C_eff=min(C,sqrt(UV))","checks":checks,"cases":rows}
out=Path("research/aspect/results/route_gram_certificate.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
