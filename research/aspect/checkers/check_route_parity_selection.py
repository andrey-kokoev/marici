"""Exact target-parity selection rule and nonintertwining hostile."""
from fractions import Fraction as F
from pathlib import Path
import json

def mv(a,v):return [sum((a[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(a))]
def dot(a,b):return sum((a[i]*b[i] for i in range(len(a))),F(0))
U=[[F(1),0],[0,F(-1)]]
bp=[F(2),0];bm=[0,F(3)]
# Hostile source-to-target map collapses both source parity sectors to the same route.
T=[[F(1),F(1)],[0,0]];ep=[F(1),0];em=[0,F(1)]
tp=mv(T,ep);tm=mv(T,em)
checks={"plus_route_has_positive_parity":mv(U,bp)==bp,"minus_route_has_negative_parity":mv(U,bm)==[-x for x in bm],"opposite_target_parities_are_orthogonal":dot(bp,bm)==0,"nonintertwining_map_collapses_parities":tp==tm and dot(tp,tm)!=0,"hostile_map_fails_intertwining":mv(U,tm)!=[-x for x in mv(T,em)]}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"orthogonal_cross_pairing":str(dot(bp,bm)),"hostile_cross_pairing":str(dot(tp,tm)),"conclusion":"opposite source parity kills cross-grade return only when the route map intertwines a unitary target parity"}
out=Path("research/aspect/results/route_parity_selection.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
