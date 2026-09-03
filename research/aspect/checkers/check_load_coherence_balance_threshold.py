"""Exact rational audit of total-load thresholds by coherence and balance."""
from fractions import Fraction as F
from pathlib import Path
import json

# kappa, gamma, exact D=sqrt(1-kappa^2(1-gamma^2)), threshold 2/(1+D)
cases={
 "equal_orthogonal":(F(1),F(0),F(0),F(2)),
 "equal_half_coherent":(F(1),F(1,2),F(1,2),F(4,3)),
 "imbalanced_orthogonal":(F(3,5),F(0),F(4,5),F(10,9)),
 "unit_coherent":(F(3,5),F(1),F(1),F(1)),
 "rank_limit":(F(0),F(0),F(1),F(1)),
}
rows={}
for name,(k,g,D,T) in cases.items():
 exact=D*D==1-k*k*(1-g*g)
 threshold=F(2,1)/(1+D)
 rows[name]={"kappa":str(k),"gamma":str(g),"D":str(D),"radical_exact":exact,"threshold":str(threshold),"declared_threshold":str(T),"matches":threshold==T}
checks={"all_radicals_exact":all(v["radical_exact"] for v in rows.values()),"all_thresholds_match":all(v["matches"] for v in rows.values()),"balanced_orthogonal_allows_load_two":rows["equal_orthogonal"]["threshold"]=="2","coherence_reduces_balanced_threshold":F(rows["equal_half_coherent"]["threshold"])<2,"imbalance_reduces_orthogonal_threshold":rows["imbalanced_orthogonal"]["threshold"]=="10/9","unit_coherence_and_rank_limit_reduce_to_trace_one":rows["unit_coherent"]["threshold"]=="1" and rows["rank_limit"]["threshold"]=="1"}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","criterion":"S < 2/(1+sqrt(1-kappa^2(1-gamma^2)))","checks":checks,"cases":rows}
out=Path("research/aspect/results/load_coherence_balance_threshold.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
