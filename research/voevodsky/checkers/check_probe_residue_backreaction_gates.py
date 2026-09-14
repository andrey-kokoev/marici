#!/usr/bin/env python3
"""Exact gate test for adjoint probe-residue backreaction."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
PACKET=ROOT/'research/voevodsky/probe_residue_does_not_canonically_backreact_on_the_prime_lattice.md'
RESULT=ROOT/'research/voevodsky/results/probe_residue_backreaction_gates.json'
T=(F(1),F(5,6),F(3,4),F(7,10));N=5

def transpose(a):return [list(x) for x in zip(*a)]
def mmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in transpose(b)] for row in a]
def mv(a,x):return [sum(y*z for y,z in zip(row,x)) for row in a]
def integral(v):return all(x.denominator==1 for x in v)
def effective(v):return all(x>=0 for x in v)
def fs(x):return f'{x.numerator}/{x.denominator}'
M=[[t**i for i in range(1,N+1)] for t in T]
A=[[F(0)]*N for _ in range(N+1)]
for i in range(N):A[i][i]=-1;A[i+1][i]=1
response=mmul(A,transpose(M));basis_deltas=[[response[i][r] for i in range(N+1)] for r in range(len(T))]
coarse=basis_deltas[0];zero=[F(0)]*(N+1);occupied=[F(1)]+[F(0)]*N
coarse_at_occupied=[x+y for x,y in zip(occupied,coarse)]
scale=[[F(2) if i==j==0 else (F(1) if i==j else F(0)) for j in range(len(T))] for i in range(len(T))]
scaled_M=mmul(scale,M);scaled_response=mmul(A,transpose(scaled_M))
# Kernel witness for four evaluations in five shell directions.
q=[F(7,16),F(-521,240),F(241,60),F(-197,60),F(1)]
checks={
 'root_embedding_degree_zero':all(sum(A[r][c] for r in range(N+1))==0 for c in range(N)),
 'all_response_directions_degree_zero':all(sum(v)==0 for v in basis_deltas),
 'coarse_response_integral':integral(coarse),
 'some_modulated_response_nonintegral':any(not integral(v) for v in basis_deltas[1:]),
 'zero_divisor_not_effective_under_coarse_response':not effective([x+y for x,y in zip(zero,coarse)]),
 'occupied_divisor_admits_coarse_response':effective(coarse_at_occupied) and coarse_at_occupied[-1]==1,
 'row_rescaling_preserves_blind_witness':mv(M,q)==[0]*len(T) and mv(scaled_M,q)==[0]*len(T),
 'row_rescaling_changes_adjoint_response':scaled_response!=response,
 'scalar_multiple_remains_degree_zero':sum(3*x for x in coarse)==0,
 'scalar_multiple_changes_displacement':[3*x for x in coarse]!=coarse,
}
delta=coarse;D=occupied;E=occupied
u_sum=[D[i]+E[i]+delta[i] for i in range(N+1)];sum_updates=[D[i]+delta[i]+E[i]+delta[i] for i in range(N+1)]
checks['affine_update_not_monoid_additive']=u_sum!=sum_updates
checks['candidate_moves_point_not_ambient_basis']=A==[[-1 if r==c else (1 if r==c+1 else 0) for c in range(N)] for r in range(N+1)]
text=PACKET.read_text(encoding='utf-8');checks['additional_action_required']='requires an explicit additional partial action' in text;checks={k:bool(v) for k,v in checks.items()}
result={'schema':'marici.voevodsky.probe-residue-backreaction-gates.v1','packet_sha256':sha256(PACKET.read_bytes()).hexdigest(),'settings':[fs(x) for x in T],'response_matrix':[[fs(x) for x in row] for row in response],'basis_deltas':[[fs(x) for x in v] for v in basis_deltas],'integral_basis_responses':[integral(v) for v in basis_deltas],'coarse_at_occupied_divisor':[fs(x) for x in coarse_at_occupied],'checks':checks,'passed':all(checks.values()),'disposition':{'admitted':'rational degree-zero tangent response and partial effective state move','rejected':'canonical integral global source-lattice or natural-monoid endomorphism','required_for_extension':'typed feedback action, integral normalization, coupling, and effective domain'}}
RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'passed':result['passed'],'checks':len(checks),'integral_responses':result['integral_basis_responses'],'coarse_delta':result['basis_deltas'][0]}));raise SystemExit(0 if result['passed'] else 1)
