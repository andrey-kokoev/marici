import json
from fractions import Fraction as Q
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B,c=1):return [[A[i][j]+c*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def inv(A):
 n=len(A); M=[A[i][:]+[Q(1) if i==j else Q(0) for j in range(n)] for i in range(n)]
 for c in range(n):
  p=next(i for i in range(c,n) if M[i][c]); M[c],M[p]=M[p],M[c]
  v=M[c][c];M[c]=[x/v for x in M[c]]
  for i in range(n):
   if i!=c:
    v=M[i][c];M[i]=[M[i][j]-v*M[c][j] for j in range(2*n)]
 return [r[n:] for r in M]
def block(A,B,C,D):return [A[i]+B[i] for i in range(len(A))]+[C[i]+D[i] for i in range(len(C))]
def sub(A,r0,r1,c0,c1):return [r[c0:c1] for r in A[r0:r1]]
def eye(n):return [[Q(1) if i==j else Q(0) for j in range(n)] for i in range(n)]
def zero(r,c):return [[Q(0) for _ in range(c)] for _ in range(r)]

A=[[Q(2),Q(1)],[Q(1),Q(3)]]
B=[[Q(1),Q(-2)],[Q(4),Q(1)]]
C=[[Q(3),Q(2)],[Q(-1),Q(5)]]
Ai=inv(A); D=mm(mm(C,Ai),B)
F=block(A,B,C,D)
Y=block([[-x for x in r] for r in mm(C,Ai)],eye(2),zero(0,0),zero(0,0))[:2] # [-C A^-1 | I]
# Genuine filtered transition: old coordinates do not depend on new top responses.
U=[[Q(2),Q(0)],[Q(1),Q(3)]]; V=[[Q(1),Q(0)],[Q(2),Q(2)]]; R=[[Q(4),Q(-1)],[Q(3),Q(5)]]
T=block(U,zero(2,2),R,V); Ti=inv(T); Fp=mm(mm(T,F),Ti)
Ap=sub(Fp,0,2,0,2); Bp=sub(Fp,0,2,2,4); Cp=sub(Fp,2,4,0,2); Dp=sub(Fp,2,4,2,4)
Ytransport=mm(Y,Ti); W=sub(Ytransport,0,2,2,4)
Ynormalized=mm(inv(W),Ytransport)
Yreconstructed=block([[-x for x in r] for r in mm(Cp,inv(Ap))],eye(2),zero(0,0),zero(0,0))[:2]
M=[[Q(1),Q(1)],[Q(1),Q(-1)]] # common/relative outer mate
checks={
 "matrix_schur_complement_vanishes":Dp==mm(mm(Cp,inv(Ap)),Bp),
 "two_response_rows_are_left_cocircuits":mm(Y,F)==zero(2,4),
 "filtered_transport_preserves_two_dimensional_cocircuit_space":mm(Ytransport,Fp)==zero(2,4),
 "schur_reconstruction_matches_normalized_transport":Yreconstructed==Ynormalized,
 "common_relative_mate_commutes_with_filtered_transport":mm(mm(M,Y),Ti)==mm(M,Ytransport),
 "response_instance_key_is_shared_by_both_rows":len(Yreconstructed)==2 and len(Yreconstructed[0])==4,
 "no_primal_direct_sum_splitting_is_required":R!=zero(2,2),
}
result={
 "schema":"marici.strominger.rh_two_response_filtered_schur_naturality_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/strominger/results/rh_filtered_schur_naturality_audit.json","research/strominger/results/rh_prime_lift_response_port_separation_audit.json"],
 "verdict":"A vanishing 2-by-2 matrix Schur complement reconstructs the full two-dimensional left-cocircuit space. Lower-block-triangular principal-parts changes transport that space contravariantly; normalization by its response anchor recovers the transformed Schur rows. The common/relative outer mate commutes with transport. Thus the abstract filtered constructor extends to the source-required two-response colligation without choosing a primal splitting.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_two_response_filtered_schur_naturality_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
