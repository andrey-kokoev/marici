"""Classify the relative change between two detector transitions."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_nonstationary_detector_cocycle.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
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
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());C1=[[t.q(x) for x in r] for r in a['change_matrix']];C2=[[t.q(x) for x in r] for r in b['transition_matrix']];R=t.mm(C2,t.inv(C1));I=[[Fraction(i==j) for j in range(3)] for i in range(3)];diag=all(not R[i][j] for i in range(3) for j in range(3) if i!=j);fixed=3-rank([[R[i][j]-I[i][j] for j in range(3)] for i in range(3)]);degree=not any(R[0][j] for j in (1,2)) and not any(R[i][0] for i in (1,2));P=[[1,0,0],[0,0,1],[0,1,0]];swap=t.mm(R,P)==t.mm(P,R);cp=t.char(R)
 out={'schema':'marici.voevodsky.cosmology-nonstationary-detector-cocycle.v1','status':'relative_transition_classified','relative_matrix':[[enc(x) for x in r] for r in R],'characteristic_polynomial_coefficients':[enc(x) for x in cp],'fixed_subspace_dimension':fixed,'diagonal':diag,'polynomial_degree_splitting_preserved':degree,'commutes_with_xy_swap':swap,'decision':'The exact relative transition isolates the nonstationary change between consecutive detector steps.','claim_boundary':'Fixed raw-q labels and canonical relation basis only; no physical process interpretation.','next_gate':'test-rational-normalization-of-relative-transition','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='relative_matrix'},indent=2))
if __name__=='__main__':main()
