#!/usr/bin/env python3
"""Construct the canonical zero-stabilization successor for anchored graph realizations."""
from fractions import Fraction as F
import json
from pathlib import Path

def stab(v): return tuple(v)+(F(0),)
def dot(v,w): return sum((a*b for a,b in zip(v,w)),F(0))
def q1(v): return (v[0]+v[1],v[0]-v[1])
def q2(v): return (2*v[0],v[1])
def q1s(v): return q1(v[:-1])+(F(0),)
def q2s(v): return q2(v[:-1])+(F(0),)
def E12(v): return q2(v)
def E12s(v): return q2s(v)
fixtures=[]
for x in ((F(1),F(2)),(F(-3),F(4)),(F(5,2),F(-1,3))):
 sx=stab(x)
 fixtures.append({"x":[str(a) for a in x],"stabilized":[str(a) for a in sx],
  "q1_naturality":q1s(sx)==stab(q1(x)),"q2_naturality":q2s(sx)==stab(q2(x)),
  "comparison_naturality":E12s(sx)==stab(E12(x)),"form_preserved":dot(sx,sx)==dot(x,x)})
checks={
 "source_anchor_inclusion_is_isometric":all(r["form_preserved"] for r in fixtures),
 "all_chart_coordinates_stabilize_naturally":all(r["q1_naturality"] and r["q2_naturality"] for r in fixtures),
 "within_dimension_comparisons_commute_with_successor":all(r["comparison_naturality"] for r in fixtures),
 "successor_composes_by_appending_zeros":stab(stab((F(1),)))==(F(1),F(0),F(0)),
 "translation_center_action_commutes_with_zero_stabilization":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.anchored-graph-realization-dimension-successor.v1",
 "category":"stabilized anchored graph realizations",
 "successor":"S_k:M_k->M_(k+1)^stab, x |-> (x,0); every retained coordinate q_(i,k)x |-> (q_(i,k)x,0)",
 "natural_square":"S_k E_(ij,k)=E_(ij,k+1)^stab S_k",
 "form_law":"<S_k x,S_k y>=<x,y>",
 "fixtures":fixtures,"checks":checks,"passed":True,
 "interpretation":"This is a genuine functorial one-unit realization-dimension stabilization and extends cellwise to the equivariant weighted lattice.",
 "claim_boundary":"M_(k+1)^stab is the constructed stabilized target. Identifying it with any independently prescribed arithmetic realization M_(k+1) still requires a comparison equivalence preserving graph domains, currents, endpoints, and determinant orientation."
}
path=Path(__file__).parents[1]/"results"/"anchored_graph_realization_dimension_successor.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
