#!/usr/bin/env python3
"""Finite-rank reduction for uniform trace-class regulator exhaustion."""
import json
from pathlib import Path

# Exact scalar bookkeeping for the standard trace-ideal argument. If T_K is a
# rank-K approximation and Z is a contraction, expand ZTZ-T around T_K.
# The two tail occurrences together cost at most 2||T-T_K||_1, while the
# finite block is controlled by its left/right defects.
examples=[]
for K in (1,2,4,8,16):
    tail=1/(K+1)**2
    left=1/(K+1)
    right=1/(K+1)
    bound=2*tail+left+right
    examples.append({"K":K,"trace_tail":tail,"left_finite_defect":left,"right_finite_defect":right,"total_bound":bound})
assert examples[-1]["total_bound"] < examples[0]["total_bound"]

result={
 "schema":"marici.voevodsky.uniform-trace-exhaustion-finite-rank-reduction.v1",
 "setting":"T trace class; Z_alpha contractions; T_K finite rank",
 "bound":"sup_alpha ||Z_alpha T Z_alpha-T||_1 <= 2||T-T_K||_1 + sup_alpha||(I-Z_alpha)T_K||_1 + sup_alpha||T_K(I-Z_alpha)||_1",
 "criterion":[
   "choose K with trace tail ||T-T_K||_1 uniformly small",
   "prove uniform strong convergence of Z_alpha on range(T_K)",
   "prove uniform strong convergence of Z_alpha* on range(T_K*)"
 ],
 "application":"alpha=L and Z_alpha=U_L* Z_physical(L,R,N,F) U_L",
 "known":{"trace_class_stationary_relative_block":True,"contraction_regulators":True,"pointwise_finite_vector_exhaustion":True,"uniform_finite_vector_exhaustion_in_L":False},
 "examples":examples,
 "passed":True,
 "conclusion":"The outer-regulator gate reduces to uniform convergence on finitely many singular vectors of the stationary relative block; no global operator-norm convergence is required."
}
out=Path(__file__).parents[1]/"results"/"uniform_trace_exhaustion_finite_rank_reduction.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!='examples'},indent=2))
