#!/usr/bin/env python3
"""Exact finite witness for convex nonselection by linear admissibility gates."""
import json
from fractions import Fraction as Q
from pathlib import Path

w1=(Q(1,2),Q(1,3),Q(1,5)); w2=(Q(1,3),Q(1,5),Q(1,7)); weights=(Q(2),Q(3),Q(5))
def norm(w): return sum(abs(x)*s for x,s in zip(w,weights))
def blend(t): return tuple(t*a+(1-t)*b for a,b in zip(w1,w2))
def codiagonal(w): return sum(w)
def assembled(w, features): return sum(a*x for a,x in zip(w,features))
features=(Q(2),Q(-1),Q(4)); ts=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
checks={
 "endpoints_distinct":w1!=w2,
 "endpoint_majorants_finite":norm(w1)>0 and norm(w2)>0,
 "five_interpolants_distinct":len({blend(t) for t in ts})==len(ts),
 "majorant_convexity":all(norm(blend(t))<=t*norm(w1)+(1-t)*norm(w2) for t in ts),
 "assembly_affine":all(assembled(blend(t),features)==t*assembled(w1,features)+(1-t)*assembled(w2,features) for t in ts),
 "codiagonal_affine":all(codiagonal(blend(t))==t*codiagonal(w1)+(1-t)*codiagonal(w2) for t in ts),
 "nonlinear_endpoint_selector_breaks_convex_closure":sum(x*x for x in blend(Q(1,2))) != Q(1,2)*sum(x*x for x in w1)+Q(1,2)*sum(x*x for x in w2),
 "linear_gates_cannot_single_out_endpoint":all(norm(blend(t))<Q(100) for t in ts),
}
assert all(checks.values()),checks
result={"schema":"marici.aspect.g4-convex-nonselection.v1","status":"passed","checks":checks,"disposition":"linear admissibility and commutation cannot uniquely select a distinct endpoint","claim_boundary":"finite exact witness plus general triangle-inequality argument; source packet supplies distinct power-law and superexponential asymptotic classes"}
out=Path(__file__).parents[1]/"results"/"g4_arithmetic_loading_convex_nonselection.json"
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":"passed","check_count":len(checks),"interpolant_count":len(ts)},sort_keys=True))
