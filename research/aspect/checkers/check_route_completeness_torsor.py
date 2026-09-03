"""Exact hostile audit of incomplete route families."""
from fractions import Fraction as F
from pathlib import Path
import json

def mv(a,v):return [sum((a[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(a))]
def norm2(v):return sum((x*x for x in v),F(0))
v=[F(0),F(1)]
B_seen=[[F(1),F(0)]]
B_missing=[[F(0),F(1)]]
B_full=B_seen+B_missing
seen=mv(B_seen,v); missing=mv(B_missing,v); full=mv(B_full,v)
checks={"truncated_routes_false_radicalize":seen==[0],"omitted_route_detects_torsor_direction":missing==[1],"complete_route_family_detects_direction":norm2(full)==1,"full_gram_exceeds_truncated_gram_on_direction":norm2(full)>norm2(seen)}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"seen_image":[str(x) for x in seen],"missing_image":[str(x) for x in missing],"full_image":[str(x) for x in full],"conclusion":"kernel descent is valid only for a source-complete route family; omitted routes can detect a direction that retained routes kill"}
out=Path("research/aspect/results/route_completeness_torsor.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
