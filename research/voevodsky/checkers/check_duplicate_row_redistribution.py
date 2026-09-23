"""Typed signed redistribution among two separately rooted identical upper rows."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def certified(p,L,T,alpha=1):
 a,u,v,c=map(Q,p);return min(a,u,v,c)>=0 and u+v-a==Q(alpha) and Q(L)*(u+v)+c==Q(T)
def move(p,theta,L,T,roots=('lower','upper-A','upper-B'),bound_B=None,alpha=1):
 if roots!=('lower','upper-A','upper-B'):raise PermissionError('MISSING_ROW_ROOT')
 if bound_B is not None and Q(bound_B)!=Q(L):raise ValueError('UPPER_B_BOUND_MISMATCH')
 assert certified(p,L,T,alpha)
 a,u,v,c=map(Q,p);theta=Q(theta)
 if not -v<=theta<=u:raise ValueError('NEGATIVE_MULTIPLIER')
 q=(a,u-theta,v+theta,c);assert certified(q,L,T,alpha);return q
checks=0
for T,u,theta in product((Q(2),Q(3),Q(4)),(Q(1),Q(3,2),Q(2)),(Q(0),Q(1,2),Q(1))):
 if u>T or theta>u:continue
 p=(u-1,u,Q(0),T-u)
 q=move(p,theta,1,T)
 for phi in (Q(0),Q(1,2)):
  if phi>q[1]:continue
  assert move(q,phi,1,T)==move(p,theta+phi,1,T)
  # Target scaling k multiplies ALL multipliers, surplus and transfer.
  k=Q(2);scaled=lambda z:tuple(k*x for x in z)
  assert move(scaled(p),k*theta,1,k*T,alpha=k)==scaled(q)
  # Source refinement L=1 -> K=1/2 adds (1-K)*(u+v) to surplus,
  # which is unchanged by moving weight between identical upper rows.
  K=Q(1,2)
  refine=lambda z:(z[0],z[1],z[2],z[3]+(1-K)*(z[1]+z[2]))
  assert move(refine(p),theta,K,T)==refine(q)
  checks+=1
assert checks>10
start=(Q(1),Q(2),Q(0),Q(0));assert move(start,1,1,2)==(1,1,1,0)
try:move(start,3,1,2)
except ValueError as e:assert str(e)=='NEGATIVE_MULTIPLIER'
else:raise AssertionError('overdraw')
try:move(start,1,1,2,roots=('lower','upper-A'))
except PermissionError:pass
else:raise AssertionError('missing upper-B root')
try:move(start,1,1,2,bound_B=2)
except ValueError as e:assert str(e)=='UPPER_B_BOUND_MISMATCH'
else:raise AssertionError('unequal upper row bound')
report={'passed':True,'composition_scaling_refinement_checks':checks,'transfer':'(a,u,v,c) -> (a,u-theta,v+theta,c), -v<=theta<=u, both upper rows same bound L','composition':'R_phi R_theta=R_(theta+phi) when intermediate and total types valid','target_scaling':'S_k R_theta=R_(k theta) S_k','source_refinement':'F_LK R_theta=R_theta F_LK for duplicate upper bounds','overdraw_missing_root_unequal_bound_refused':True,'scope':'Mathematically typed candidate proof 2-cell on explicitly duplicated primitive source row identities. No original-category 2-cell, global proof path identification, operational authority or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/duplicate-row-redistribution.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
