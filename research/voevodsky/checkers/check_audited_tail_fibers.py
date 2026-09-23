"""One-atom audit access via a residual generator, not witness transport.

Exact audit interval computed by intersection of a line with residual support
halfspaces generated on demand. Tests use m=3 and independent source vertices.
No uniform query-work bound is claimed.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def caps(m):return [Q(100+2*j) for j in range(m)]
def slopes(m):return [Q(1,128**j) for j in range(m)]
def interval(m,U,V):
 # Residual polygon generators j>=1. Normals perpendicular to each generator,
 # in both orientations, give all polygon edges (for m>=3).
 assert m>=3
 c=caps(m);q=slopes(m);lo=Q(0);hi=c[0];lower=('cap',);upper=('cap',)
 for j in range(1,m):
  for sign in (-1,1):
   a,b=sign*(-q[j]),Q(sign)
   bound=sum(c[k]*max(Q(0),a+b*q[k]) for k in range(1,m))
   # a(U-h)+b(V-h)<=bound
   coefficient=-(a+b);rhs=bound-a*U-b*V
   if coefficient>0 and rhs/coefficient<hi:hi=rhs/coefficient;upper=(str(a),str(b),str(bound))
   elif coefficient<0 and rhs/coefficient>lo:lo=rhs/coefficient;lower=(str(a),str(b),str(bound))
   elif coefficient==0 and rhs<0:return None
 return None if lo>hi else (lo,hi,lower,upper)
def lift(m,U,V,h):
 c=caps(m);q=slopes(m);mass=U-h;value=V-h
 def greedy(reverse):
  x=[Q(0)]*m;remaining=mass
  for j in (range(m-1,0,-1) if reverse else range(1,m)):
   x[j]=min(c[j],max(Q(0),remaining));remaining-=x[j]
  assert remaining==0
  return x
 low=greedy(True);high=greedy(False);lv=dot(q,low);hv=dot(q,high)
 assert lv<=value<=hv
 theta=(value-lv)/(hv-lv) if hv!=lv else Q(0)
 x=[(1-theta)*a+theta*b for a,b in zip(low,high)];x[0]=h
 assert sum(x)==U and dot(q,x)==V and all(0<=a<=b for a,b in zip(x,c))
 return x
checks=0;records=[]
for m in (3,4,8,16,64):
 c=caps(m);q=slopes(m)
 for shift in range(5):
  x=[cap*Q((j+shift)%5,4) for j,cap in enumerate(c)]
  U,V=sum(x),dot(q,x);ans=interval(m,U,V);assert ans is not None
  lo,hi,*_=ans;assert lo<=x[0]<=hi
  for h in (lo,(lo+hi)/2,hi):lift(m,U,V,h);checks+=1
  # Audits h<=r: possible iff lo<=r; forced iff hi<=r.
  # With retained h>=a,h<=b, replace [lo,hi] by its intersection.
  assert max(lo,hi+1)>min(hi,hi+2)
  records.append({'m':m,'U':str(U),'V':str(V),'interval':[str(lo),str(hi)],'active_bounds':ans[2:]})
# Same total, opposite extreme weighted sums: unique greedy witnesses.
m=3;q=slopes(m)
left=(Q(50),Q(50)*q[2]);right=(Q(50),Q(50))
a=interval(m,*left);b=interval(m,*right)
assert a[:2]==(0,0) and b[:2]==(50,50)
lift(m,*left,Q(0));lift(m,*right,Q(50))
# Interior controls on both source and observable polygon, not just tips.
x=(Q(20),Q(30),Q(40));y=(Q(70),Q(30),Q(40))
a=interval(3,sum(x),dot(q,x));b=interval(3,sum(y),dot(q,y))
assert a[1]<b[0]
report={'passed':True,'exact_lift_checks':checks,'records':records,
 'interior_transport_obstruction':{'left_source':list(map(str,x)),'right_source':list(map(str,y)),
 'left_audit_interval':list(map(str,a[:2])),'right_audit_interval':list(map(str,b[:2])),
 'separating_threshold':str((a[1]+b[0])/2)},
 'semantics':{'possible_h_le_r':'lo<=r','forced_h_le_r':'hi<=r','exact_h':'membership of (U-h,V-h) in residual generator image'},
 'representation':'Residual source generator plus m; support inequalities streamed, only active audit bounds retained. O(m) streamed inequalities here, not a constant-work claim.',
 'scope':'Audit-conditioned queries within a fixed observable fiber. Not an implementation of global optimization with arbitrary accumulated frames; no actual-source selection or audit-preserving transport follows.'}
(OUT/'audited-tail-fibers.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
