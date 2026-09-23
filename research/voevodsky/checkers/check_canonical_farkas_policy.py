"""Min-surplus then lexicographic Farkas proof selection need not compose."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
# source normals/bounds at reference s; target normal 1 and physical bound T.
def choose(normals,bounds,source_ref,target_ref,T):
 target_residual=Q(T)-Q(target_ref)
 choices=[]
 for coeff in product(range(5),repeat=len(normals)):
  if sum(Q(a)*n for a,n in zip(coeff,normals))!=1:continue
  source_residual=sum(Q(a)*(b-n*Q(source_ref)) for a,b,n in zip(coeff,bounds,normals))
  shift=Q(target_ref)-Q(source_ref)
  surplus=target_residual-(source_residual-shift)
  if surplus>=0:choices.append((surplus,coeff))
 assert choices
 return min(choices)
S_norm=(-Q(1),Q(1));S_bound=(Q(0),Q(1));s=Q(0);mid=Q(1,4);end=Q(1,2)
a=choose(S_norm,S_bound,s,mid,2)
b=choose((Q(1),),(Q(2),),mid,end,3)
direct=choose(S_norm,S_bound,s,end,3)
assert a==(Q(0),(1,2)) and b==(Q(1),(1,)) and direct==(Q(0),(2,3))
# Composition uses (N M, N c+k): scalar N=1 here.
composite=(b[1][0]*a[0]+b[0],tuple(b[1][0]*v for v in a[1]))
assert composite==(Q(1),(1,2)) and composite!=direct
# Both composite and direct certify S subset x<=3 at shifted reference.
def verify(coeff,surplus,T,ref):
 normal=sum(Q(a)*n for a,n in zip(coeff,S_norm));raw=sum(Q(a)*h for a,h in zip(coeff,S_bound))
 return normal==1 and surplus>=0 and raw+surplus==Q(T) and Q(T)-Q(ref)==raw-normal*Q(ref)+surplus
assert verify(composite[1],composite[0],3,end) and verify(direct[1],direct[0],3,end)
report={'passed':True,'policy':'minimize nonnegative surplus then lexicographic multiplier over coefficients 0..4','first':{'multiplier':list(a[1]),'surplus':str(a[0])},'second':{'multiplier':list(b[1]),'surplus':str(b[0])},'composite':{'multiplier':list(composite[1]),'surplus':str(composite[0])},'direct':{'multiplier':list(direct[1]),'surplus':str(direct[0])},'reference_points':['0','1/4','1/2'],'policy_not_compositional':True,'scope':'Finite bounded multiplier menu with explicit source/intermediate/target presentations; not global LP canonicalization or analytic realization.'}
out=Path(__file__).resolve().parents[1]/'results/canonical-farkas-policy.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
