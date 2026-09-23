"""Independent exact Farkas infeasibility certificates for all 36 seven-label fibres."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
frozen=json.loads((OUT/'nine-point-support-stress.json').read_text())['first_no_seven_support_target'];assert frozen['attempt']==88
neg=frozen['negative_initial_columns'];w=list(map(Q,frozen['weights']));t=list(map(Q,frozen['slopes']))
x=[(-w[i] if i<neg else w[i]) for i in range(9)];y=[x[i]*t[i] for i in range(9)]
assert all(x[i]*y[j]-x[j]*y[i]>0 for i,j in combinations(range(9),2))
Z=s.Matrix([[s.Integer(j)**d for d in range(6)] for j in range(1,10)]);Y=s.Matrix([x,y])*Z
def form(X,V,k,i,j):return (X[i]*V[j]-X[j]*V[i],k[i]*V[j]-k[j]*V[i],X[i]*k[j]-X[j]*k[i])
def cross(n,m):return n[1]*m[2]-n[2]*m[1]
def cert(lines):
 for p,L in lines:
  if L[1]==L[2]==0 and L[0]<0:return [(p,Q(1))]
 for (p,L),(q,M) in combinations(lines,2):
  if cross(L,M)!=0:continue
  if L[1]==L[2]==0 or M[1]==M[2]==0:continue
  ratio=-Q(L[1],M[1]) if M[1] else -Q(L[2],M[2])
  if ratio>0 and L[1]+ratio*M[1]==L[2]+ratio*M[2]==0 and L[0]+ratio*M[0]<0:
   return [(p,Q(1)),(q,ratio)]
 for (p,L),(q,M),(r,T) in combinations(lines,3):
  a,b,c=cross(M,T),cross(T,L),cross(L,M)
  if min(a,b,c)<0 and max(a,b,c)<=0:a,b,c=-a,-b,-c
  if min(a,b,c)<0 or max(a,b,c)==0:continue
  if a*L[0]+b*M[0]+c*T[0]>=0:continue
  assert a*L[1]+b*M[1]+c*T[1]==0 and a*L[2]+b*M[2]+c*T[2]==0
  return [(p,Q(a)),(q,Q(b)),(r,Q(c))]
 return None
reports=[]
for support in combinations(range(9),7):
 z=Z[list(support),:];basis=z[:6,:];inv=basis.inv();k=tuple(Q(v) for v in (-z[6,:]*inv).row_join(s.ones(1,1)))
 assert len(k)==7 and all(sum(k[i]*z[i,d] for i in range(7))==0 for d in range(6))
 B=Y*inv;X=[Q(B[0,i]) for i in range(6)]+[Q(0)];V=[Q(B[1,i]) for i in range(6)]+[Q(0)]
 lines=[((i+1,j+1),form(X,V,k,i,j)) for i,j in combinations(range(7),2)]
 witness=cert(lines)
 if witness is None:raise AssertionError('No Farkas witness for support '+str(support))
 weights={p:lam for p,lam in witness}
 assert len(weights)<=3 and all(lam>0 for lam in weights.values())
 assert sum(weights.get(p,Q(0))*L[1] for p,L in lines)==0
 assert sum(weights.get(p,Q(0))*L[2] for p,L in lines)==0
 constant=sum(weights.get(p,Q(0))*L[0] for p,L in lines);assert constant<0
 reports.append({'retained_labels':[i+1 for i in support],
                 'contradiction_minors':[list(p) for p,lam in witness],
                 'positive_weights':list(map(str,[lam for p,lam in witness])),
                 'weighted_constant':str(constant)})
assert len(reports)==36
result={'schema':'marici.nima.nine-point-no-seven-support-verification.v1','passed':True,
 'strict_positive_nine_source':True,'seven_label_subsets_rejected':36,
 'maximum_minors_per_infeasibility_certificate':max(len(r['contradiction_minors']) for r in reports),
 'certificates':reports,
 'scope':'For this fixed strictly positive n=9 target, no source lift supported on any seven labels exists, even non-strictly. Exact nonnegative combinations of at most three ordered-minor inequalities give a negative constant on each subset. Does not establish minimum support for all targets or identify physical history cells.'}
(OUT/'nine-point-no-seven-support-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'subsets_rejected':36,'max_certificate_size':result['maximum_minors_per_infeasibility_certificate'],
 'first_certificate':reports[0]},indent=2))
