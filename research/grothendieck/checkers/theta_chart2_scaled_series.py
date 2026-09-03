"""Dependency-free exact endpoint series for scaled Chart-2 factors H and J."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=14
@dataclass(frozen=True)
class Q:
 v:F;d:F
 def __add__(a,b):b=qq(b);return Q(a.v+b.v,a.d+b.d)
 __radd__=__add__
 def __neg__(a):return Q(-a.v,-a.d)
 def __sub__(a,b):return a+(-qq(b))
 def __rsub__(a,b):return qq(b)-a
 def __mul__(a,b):b=qq(b);return Q(a.v*b.v,a.d*b.v+a.v*b.d)
 __rmul__=__mul__
 def inv(a):return Q(1/a.v,-a.d/a.v**2)
 def __truediv__(a,b):return a*qq(b).inv()
 def __rtruediv__(a,b):return qq(b)/a
def qq(x):return x if isinstance(x,Q) else Q(F(x),F(0))
def add(a,b):return [a[i]+b[i] for i in range(N)]
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[qq(0) for _ in range(N)]
 for i in range(N):
  for j in range(N-i):z[i+j]=z[i+j]+a[i]*b[j]
 return z
def scale(a,c):return [x*c for x in a]
def exp0(a):
 z=[qq(0) for _ in range(N)];z[0]=qq(1);p=z[:]
 for k in range(1,N):p=mul(p,a);z=add(z,scale(p,F(1,factorial(k))))
 return z
def log1m(a):
 z=[qq(0) for _ in range(N)];p=[qq(0) for _ in range(N)];p[0]=qq(1)
 for k in range(1,N):p=mul(p,a);z=add(z,scale(p,F(1,k)))
 return z
def factors(qv,pv):
 q=Q(qv,1);A=Q(pv,0)/q;h=[qq(0) for _ in range(N)]
 for n in range(1,N):h[n]=qq(F(1,factorial(2*n)))
 b=scale(h,6*A/((A-3)*(A-3)));m=add(scale(h,A),log1m(b));m4=[m[n]*4**n for n in range(N)];eta=sub(m4,scale(m,4))
 u=sub([qq(1)]+[qq(0)]*(N-1),exp0(scale(m,-2)))
 R=sub(mul(u,u),mul(exp0(scale(m,-4)),sub([qq(1)]+[qq(0)]*(N-1),exp0(neg(eta)))))
 H=[Q((n-2)*R[n].v,(n-2)*R[n].d) for n in range(N)]
 J=[Q(qv*R[n].d+n*R[n].v,0) for n in range(N)]
 return R,H,J
P=[F(2*3141592653589793238,10**18),F(2*3141592653589793239,10**18)];QS=[F(7,16),F(1,2)]
records=[]
for p in P:
 for q in QS:
  R,H,J=factors(q,p)
  leadH=next(i for i,x in enumerate(H) if x.v);leadJ=next(i for i,x in enumerate(J) if x.v)
  def value(c,z):return sum((c[n].v*z**(n-(leadH if c is H else leadJ)) for n in range(leadH if c is H else leadJ,N)),F(0))
  hz=[value(H,q/1000),value(H,F(1,64))];jz=[value(J,q/1000),value(J,F(1,64))]
  records.append({"p":str(p),"q":str(q),"R_lead":next(i for i,x in enumerate(R) if x.v),
   "H_lead":leadH,"J_lead":leadJ,"H_scaled_signs":[(-1 if x.v<0 else 1 if x.v>0 else 0) for x in H[leadH:]],
   "J_scaled_signs":[(-1 if x.v<0 else 1 if x.v>0 else 0) for x in J[leadJ:]],
   "H_scaled_endpoint_values_float":[float(x) for x in hz],"J_scaled_endpoint_values_float":[float(x) for x in jz]})
result={"scope":"four rational endpoint parameter cases; not uniform","order":N-1,"records":records}
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-chart2-scaled-series.json").write_text(out);print(out,end="")
