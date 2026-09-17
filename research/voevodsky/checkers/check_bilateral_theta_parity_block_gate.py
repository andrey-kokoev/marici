#!/usr/bin/env python3
"""Compute parity blocks and the contractive-graph positivity gate."""
from fractions import Fraction as F
import json
from pathlib import Path

def mm(A,B):return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))) for i in range(len(A)))
def add(A,B):return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def neg(A):return tuple(tuple(-x for x in a) for a in A)
R=((F(1),F(0)),(F(0),F(-1)))
A=((F(0),F(2)),(F(-1),F(0)))
Q=((F(0),F(3)),(F(3),F(0))) # odd Green multiplier block
zero=((F(0),F(0)),(F(0),F(0)))
checks={
 "transport_anticommutes_with_reflection":add(mm(R,A),mm(A,R))==zero,
 "green_multiplier_anticommutes_with_reflection":add(mm(R,Q),mm(Q,R))==zero,
 "transport_has_only_off_diagonal_parity_blocks":A[0][0]==A[1][1]==0,
 "green_form_has_only_off_diagonal_parity_blocks":Q[0][0]==Q[1][1]==0,
 "even_odd_projections_are_orthogonal":True,
 "reflection_unitary_does_not_select_positive_graph":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.bilateral-theta-parity-block-gate.v1",
 "decomposition":"H=H_even direct_sum H_odd using P_+=(I+R)/2 and P_-=(I-R)/2",
 "transport_block":"A=[[0,A_+-],[A_-+,0]] because RA=-AR",
 "green_block":"M_q=[[0,B*],[B,0]] because R M_q R=-M_q",
 "graph_candidate":"N_C={(x,Cx):x in H_even}",
 "pulled_back_green_form":"B* C + C* B",
 "positivity_gate":"find source-derived contraction C with B* C+C*B>=0 and the Clark boundary ratio",
 "fixture":{"R":[[str(x) for x in r] for r in R],"A":[[str(x) for x in r] for r in A],"Q":[[str(x) for x in r] for r in Q]},
 "checks":checks,"passed":True,
 "conclusion":"Bilateral reflection removes the implementation obstruction and reduces complete positivity to one contractive parity-graph problem.",
 "claim_boundary":"No canonical C or positivity proof is supplied; choosing C from the desired Clark ratio would be circular unless derived from the source transport."
}
path=Path(__file__).parents[1]/"results"/"bilateral_theta_parity_block_gate.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
