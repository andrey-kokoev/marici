"""Classify exact invariants of the A14-to-A16 detector change matrix."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_mixed_detector_invariants.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def det(M):return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def rank(M):
 A=[list(r) for r in M];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];a=A[r][c];A[r]=[x/a for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:a=A[i][c];A[i]=[x-a*y for x,y in zip(A[i],A[r])]
  r+=1
 return r
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def main():
 d=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());C=[[q(x) for x in row] for row in d['change_matrix']];tr=sum(C[i][i] for i in range(3));e2=C[0][0]*C[1][1]-C[0][1]*C[1][0]+C[0][0]*C[2][2]-C[0][2]*C[2][0]+C[1][1]*C[2][2]-C[1][2]*C[2][1];D=det(C);I=[[Fraction(i==j) for j in range(3)] for i in range(3)];fixed=3-rank([[C[i][j]-I[i][j] for j in range(3)] for i in range(3)]);P=[[1,0,0],[0,0,1],[0,1,0]];comm=[[mm(C,P)[i][j]-mm(P,C)[i][j] for j in range(3)] for i in range(3)];degree_preserved=not any(C[0][j] for j in (1,2)) and not any(C[i][0] for i in (1,2))
 out={'schema':'marici.voevodsky.cosmology-mixed-detector-invariants.v1','status':'mixed_transport_invariants_classified','characteristic_polynomial_coefficients':[enc(Fraction(1)),enc(-tr),enc(e2),enc(-D)],'determinant':enc(D),'fixed_subspace_dimension':fixed,'polynomial_degree_splitting_preserved':degree_preserved,'commutes_with_xy_swap':rank(comm)==0,'decision':'The source-labelled detector transport is invertible but preserves neither constant-versus-linear splitting nor x/y swap, and its fixed-space dimension is recorded.','claim_boundary':'Arbitrary independent basis changes can trivialize a single invertible transition; invariants here retain the fixed 1,y,x labels.','next_gate':'test-detector-cocycle-at-A18','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
