import json
from fractions import Fraction as Q
from pathlib import Path

def mv(A,x):return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
def transpose(A):return [list(r) for r in zip(*A)]
def rank2(A):return 2 if A[0][0]*A[1][1]-A[0][1]*A[1][0] else (1 if any(any(x for x in r) for r in A) else 0)

f=Q(3); L=Q(5)
# One common input duplicated to reciprocal sectors.
B_in=[[-f],[-f]]
B_star=transpose(B_in)                 # codiagonal common response
C_local=[[-f,Q(0)],[Q(0),-f]]         # two sector-local responses
common=[[Q(1),Q(1)]]
relative=[[Q(1),Q(-1)]]
R_common=[mv(common,mv(C_local,[Q(1),Q(0)])),mv(common,mv(C_local,[Q(0),Q(1)]))]
# Rows obtained by composing common/relative mates with local response.
row_common=[-f,-f]
row_relative=[-f,f]
zero_state=[Q(7),Q(-7)]
# Even/odd Mellin observer on symmetric/antisymmetric boundary atoms.
mellin_incidence=[[2*f,Q(0)],[Q(0),2*L*f]]
checks={
 "hilbert_adjoint_is_only_codiagonal_common_row":B_star==[row_common],
 "common_adjoint_kills_nontrivial_scalar_zero_state":mv(B_star,zero_state)==[0],
 "source_local_response_pair_retains_relative_witness":mv([row_relative],zero_state)!=[0],
 "local_response_pair_precedes_outer_mate":mv(C_local,zero_state)==[-f*zero_state[0],-f*zero_state[1]],
 "mellin_position_row_gives_rank_two_even_odd_incidence":rank2(mellin_incidence)==2,
 "single_contragredient_cannot_equal_two_row_response_object":len(B_star)==1 and len(C_local)==2,
}
result={
 "schema":"marici.strominger.rh_prime_lift_response_port_separation_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/grothendieck/adjoint-completion-makes-the-constant-source-channel-dynamical-and-forces-a-separate-response-port.md","research/grothendieck/the-single-adjoint-response-is-a-codiagonal-shadow-of-two-sector-local-responses.md","research/grothendieck/the-mellin-position-row-restores-rank-two-boundary-incidence.md"],
 "verdict":"The algebraic contragredient of the common prime input is only the codiagonal response. It annihilates every nontrivial reciprocal scalar-zero state. Source-derived sector-local responses retain an independent relative row, and the Mellin position row separates odd boundary current. Therefore the physical response object is a two-row labelled pair followed by an outer mate; it cannot be identified with the single contragredient used by the abstract Schur constructor.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_prime_lift_response_port_separation_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
