"""Sufficient positive-kernel criterion for consuming Farkas surplus."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def dot(x,y):return sum((Q(a)*Q(b) for a,b in zip(x,y)),Q(0))
def cert(rows,bounds,m,c,target,bound):
 cols=len(target)
 return len(rows)==len(bounds)==len(m) and all(len(r)==cols for r in rows) and min(map(Q,m))>=0 and Q(c)>=0 and all(dot([r[j] for r in rows],m)==Q(target[j]) for j in range(cols)) and dot(bounds,m)+Q(c)==Q(bound)
def consume(rows,bounds,m,c,target,bound,d):
 if len(d)!=len(rows) or any(Q(z)<0 for z in d):raise ValueError('NONPOSITIVE_OR_MISSING_KERNEL')
 if any(dot([r[j] for r in rows],d) for j in range(len(target))):raise ValueError('NOT_A_NORMAL_KERNEL')
 B=dot(bounds,d)
 if B<=0:raise ValueError('NO_POSITIVE_BOUND_SYZYGY')
 assert cert(rows,bounds,m,c,target,bound)
 lam=Q(c)/B;new=tuple(Q(v)+lam*Q(z) for v,z in zip(m,d))
 assert cert(rows,bounds,new,0,target,bound)
 return new
rows=((-1,0),(0,-1),(1,1));bounds=(0,0,1);d=(1,1,1);v=(1,1)
checks=0
for T,m3 in product((Q(1),Q(3,2),Q(2),Q(3)),(Q(1),Q(3,2),Q(2),Q(3))):
 if m3>T:continue
 c=T-m3;m=(m3-1,m3-1,m3)
 assert cert(rows,bounds,m,c,v,T)
 assert consume(rows,bounds,m,c,v,T,d)==(T-1,T-1,T)
 checks+=1
assert checks>=8
for rr,bb,mm,cc,vv,TT,dd,reason in [
 (((1,),),(1,),(1,),Q(1),(1,),Q(2),(0,),'NO_POSITIVE_BOUND_SYZYGY'),
 (((-1,),(1,)),(0,0),(0,1),Q(1),(1,),Q(1),(1,1),'NO_POSITIVE_BOUND_SYZYGY'),
 (rows,bounds,(0,0,1),Q(1),v,Q(2),(0,0,1),'NOT_A_NORMAL_KERNEL')]:
 try:consume(rr,bb,mm,cc,vv,TT,dd)
 except ValueError as e:assert str(e)==reason
 else:raise AssertionError('bad syzygy admitted')
report={'passed':True,'two_dimensional_triangle_checks':checks,'positive_kernel_criterion':'d>=0, A^T d=0, bounds dot d>0; N(m,c)=m+(c/(bounds dot d))*d','hostile_no_kernel':True,'hostile_zero_bound_kernel':True,'hostile_wrong_normal_kernel':True,'scope':'Sufficient criterion for fixed primitive Farkas rows and one chosen d. No uniqueness or canonical selection with multiple d, no source authenticity, proof-history 4-cell or analytic correspondence.'}
out=Path(__file__).resolve().parents[1]/'results/general-syzygy-normalizer.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
