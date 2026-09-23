"""Exact necessary support-size probe across all 36 seven-label subimages at n=9."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
subsets=list(combinations(range(9),7));assert len(subsets)==36
cache=[]
for S in subsets:
 z=Z[list(S),:];inverse=z[:6,:].inv();v=s.Matrix([-x for x in list((z[6,:]*inverse))]+[s.Integer(1)])
 assert (v.T*z)==s.zeros(1,6)
 cache.append((S,z,inverse,tuple(Q(x) for x in v)))
def solve(L,M):
 c,a,b=L;d,e,f=M;det=a*f-b*e
 return None if det==0 else ((b*d-c*f)/det,(c*e-a*d)/det)
def check(Y,entry):
 S,z,inverse,k=entry
 source=Y*inverse;x=[Q(source[0,j]) for j in range(6)]+[Q(0)];y=[Q(source[1,j]) for j in range(6)]+[Q(0)]
 forms={(i,j):(x[i]*y[j]-x[j]*y[i],k[i]*y[j]-k[j]*y[i],x[i]*k[j]-x[j]*k[i]) for i,j in combinations(range(7),2)}
 # A full-dimensional retained-seven lift is necessary for any paired-minor
 # or zero-middle-column cell that sits inside its closed positive image.
 for p,q in combinations(forms,2):
  z=solve(forms[p],forms[q])
  if z is None:continue
  if all(c+a*z[0]+b*z[1]>=0 for c,a,b in forms.values()):
   active=sum(c+a*z[0]+b*z[1]==0 for c,a,b in forms.values())
   return {'support':[j+1 for j in S],'active_minors':active}
 return None
def main():
 sources=[{'name':'uniform','w':[1]*9,'t':list(range(9))},
          {'name':'irregular','w':[2,7,1,4,8,2,6,1,5],'t':[0,2,3,7,8,13,15,19,30]},
          {'name':'steep','w':[1,3,1,9,2,5,1,7,2],'t':[0,1,2,3,5,8,13,21,34]}]
 rows=[]
 for item in sources:
  C=s.Matrix([item['w'],[w*t for w,t in zip(item['w'],item['t'])]])
  assert all(C[0,i]*C[1,j]-C[0,j]*C[1,i]>0 for i,j in combinations(range(9),2))
  Y=C*Z;found=[r for entry in cache if (r:=check(Y,entry)) is not None]
  rows.append({'source_name':item['name'],'seven_label_subimages_with_nonnegative_lift':len(found),
    'first_supports':found[:8]})
 result={'schema':'marici.nima.nine-point-seven-support-coverage-probe.v1','rows':rows,
  'scope':'Exact necessary support-size census at three strictly positive n=9 targets. Zero feasible seven-label subsets would obstruct every n=9 cell supported on at most seven labels at that target. Nonzero counts do not identify sourced physical history cells or prove coverage.'}
 (OUT/'nine-point-seven-support-coverage-probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
