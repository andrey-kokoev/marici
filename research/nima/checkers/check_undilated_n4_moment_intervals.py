"""Directed rational intervals for coherent c=1 septic moments n=0..3."""
from fractions import Fraction as F
from math import comb,factorial
from decimal import Decimal
import json
import preconditioned_spline_weil as w
A=w.scale(F(2),w.log_q(F(2)))
BASE_C=[F(1),F(-5),F(33,4),F(-5),F(1)];BASE_M=[2,1,0,-1,-2]
def translated_cross(lag):
 d={}
 for c,m in zip(BASE_C,BASE_M):
  for shift in (lag,-lag): d[m+shift]=d.get(m+shift,F(0))+c/2
 ms=sorted(d,reverse=True);return [d[m] for m in ms],ms
PROFILES={'baseline':(BASE_C,BASE_M),'cross':translated_cross(1),'lag2_cross':translated_cross(2)}
def exp_iv(x):
 lo=w.exp_q(x[0]);hi=w.exp_q(x[1]);return (lo[0],hi[1])
def J(b,s):
 y=w.max0(s);e=exp_iv(w.scale(b,w.sub(s,y)));poly=w.Z;by=w.scale(b,y)
 for r in range(8): poly=w.add(poly,w.scale(F(1,factorial(r)),w.pow_pos(by,r)))
 return w.scale(F(1,b**8),w.mul(e,poly))
def closed(n,cs,ms):
 b=F(4*n+1,4);out=w.Z
 for c,m in zip(cs,ms):
  for j in range(9):
   s=w.add(w.scale(F(m),A),(F(4-j),F(4-j)))
   out=w.add(out,w.scale(c*F((-1)**j*comb(8,j)),J(b,s)))
 return out
source=json.load(open('research/grothendieck/results/undilated-septic-moment-formula-check.json'))
centers={(r['profile'],int(r['n'])):F(Decimal(r['closed'])) for r in source['rows']}
rows=[];failures=[]
for name,(cs,ms) in PROFILES.items():
 for n in range(4):
  iv=closed(n,cs,ms);x=centers[(name,n)];inside=iv[0]<=x<=iv[1]
  row={'profile':name,'n':n,'interval':[float(iv[0]),float(iv[1])],'center':float(x),'width':float(iv[1]-iv[0]),'source_center_enclosed':inside};rows.append(row)
  if not inside: failures.append(row)
out={'schema':'marici.nima.undilated-n4-moment-intervals.v1','status':'passed' if not failures else 'failed','interface':{'c':1,'a':'2 log 2','rate':'n+1/4'},'rows':rows,'failures':failures,'max_width':max(r['width'] for r in rows),'all_source_centers_enclosed':not failures,'claim_boundary':'directed intervals for finite moments only; archimedean assembly, jets, prime terms, and tail remain separate'}
print(json.dumps(out,sort_keys=True));assert not failures
