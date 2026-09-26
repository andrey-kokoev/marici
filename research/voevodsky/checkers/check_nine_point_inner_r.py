"""Source inner R vs shifted momentum supertwistor five-bracket products."""
from nine_point_source_r import Kinematics
from pathlib import Path
import sympy as s
import json
root=Path(__file__).resolve().parents[1]
histories=json.loads((root/'results/nine-point-source-history-contract.json').read_text())['records']
checks=0
for parameters in (range(1,10),(1,2,4,7,11,16,22,29,37)):
 kin=Kinematics([(1,t,t*t,t**3) for t in parameters]);basis={i:s.eye(9)[i-1,:] for i in range(1,10)}
 def intersection(u,v,a,b,c):return kin.bracket(v,a,b,c)*basis[u]-kin.bracket(u,a,b,c)*basis[v]
 def five(rows):
  z=[r*s.Matrix.vstack(*kin.z[1:]) for r in rows];ferm=s.zeros(1,9);den=s.S.One
  for k in range(5):
   minor=s.Matrix.vstack(*(z[(k+j)%5] for j in range(1,5))).det();ferm+=minor*rows[k];den*=minor
  if den==0:raise ValueError('singular independent five-bracket')
  return {i:ferm[i-1] for i in range(1,10)},1/den
 def wedge(A,B):return [s.factor(A[i]*B[j]-A[j]*B[i]) for i in range(1,10) for j in range(i+1,10)]
 for h in histories:
  a1,b1=h['outer_pair'];a,b=h['inner_pair'];branch=h['branch']
  A,p=kin.ordinary(a1,b1);B,q=kin.inner(a1,b1,a,b,branch)
  C,r=kin.five_bracket(a1,b1)
  shifted=intersection(b1-1,b1,9,a1-1,a1)
  if branch=='left-nested':
   anchor=intersection(a1-1,a1,9,b1-1,b1)
   rows=[anchor,basis[a-1],basis[a],basis[b-1],shifted if b==b1 else basis[b]]
  else:rows=[basis[9],shifted if a==b1 else basis[a-1],basis[a],basis[b-1],basis[b]]
  D,t=five(rows);W=wedge(A,B);V=wedge(C,D)
  pivot=next(i for i,v in enumerate(V) if v);scale=s.factor(W[pivot]/V[pivot])
  assert scale!=0 and all(s.factor(x-scale*y)==0 for x,y in zip(W,V)),('fermions',h)
  assert s.factor(p*q*scale**4-r*t)==0,('normalization',h,s.factor(p*q*scale**4/(r*t)))
  checks+=1
report={'passed':True,'history_products':checks,'witnesses':2,'boundary_cases_per_witness':30,'check':'All36 wedge coordinates proportional; full prefactors agree after fourth-power scaling with independently constructed intersection five-brackets','scope':'Exact two rational twistor witnesses, including all sourced boundary histories; not all-kinematics proof or geometric contour identification.'}
(root/'results/nine-point-inner-r.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
