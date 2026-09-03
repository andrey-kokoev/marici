"""Exact audit of robust trace-upper/determinant-lower return margins."""
from fractions import Fraction as F
from pathlib import Path
import json

# T, D, exact discriminant root, exact worst lambda
cases={
 "strict":(F(1),F(4,25),F(3,5),F(4,5)),
 "terminal_rank_one":(F(1),F(0),F(1),F(1)),
 "terminal_nondegenerate":(F(3,2),F(1,2),F(1,2),F(1)),
 "strict_high_trace":(F(3,2),F(14,25),F(1,10),F(4,5)),
}
rows={}
for name,(T,D,R,L) in cases.items():
 feasible=0<=D<=T*T/4
 exact=R*R==T*T-4*D
 lam=(T+R)/2
 margin=1-T+D
 rows[name]={"T":str(T),"D":str(D),"feasible_corner":feasible,"radical_exact":exact,"worst_lambda":str(lam),"declared_lambda":str(L),"complement_margin":str(margin),"strict":T<2 and margin>0}
checks={"all_corners_feasible":all(v["feasible_corner"] for v in rows.values()),"all_radicals_exact":all(v["radical_exact"] for v in rows.values()),"all_lambdas_match":all(v["worst_lambda"]==v["declared_lambda"] for v in rows.values()),"strict_cases_pass":rows["strict"]["strict"] and rows["strict_high_trace"]["strict"],"terminal_cases_have_zero_margin":rows["terminal_rank_one"]["complement_margin"]=="0" and rows["terminal_nondegenerate"]["complement_margin"]=="0"}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"nonempty class 0<=D<=T^2/4; robust strict iff T<2 and 1-T+D>0; worst lambda=(T+sqrt(T^2-4D))/2","checks":checks,"cases":rows}
out=Path("research/aspect/results/robust_trace_determinant_margin.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
