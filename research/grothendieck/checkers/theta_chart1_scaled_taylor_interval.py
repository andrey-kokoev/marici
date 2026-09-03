"""Exact local-q polynomial cover for scaled Chart-1 H and J."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=14
@dataclass(frozen=True)
class I:
 lo:F;hi:F
 def __add__(a,b):b=iv(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+(-iv(b))
 def __rsub__(a,b):return iv(b)-a
 def __mul__(a,b):
  b=iv(b);x=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi);return I(min(x),max(x))
 __rmul__=__mul__
 def inv(a):assert a.lo>0 or a.hi<0;return I(1/a.hi,1/a.lo)
 def __truediv__(a,b):return a*iv(b).inv()
 def __rtruediv__(a,b):return iv(b)/a
def iv(x):return x if isinstance(x,I) else I(F(x),F(x))
@dataclass(frozen=True)
class Q:
 v:I;d:I
 def __add__(a,b):b=qq(b);return Q(a.v+b.v,a.d+b.d)
 __radd__=__add__
 def __neg__(a):return Q(-a.v,-a.d)
 def __sub__(a,b):return a+(-qq(b))
 def __rsub__(a,b):return qq(b)-a
 def __mul__(a,b):b=qq(b);return Q(a.v*b.v,a.d*b.v+a.v*b.d)
 __rmul__=__mul__
 def inv(a):return Q(a.v.inv(),-a.d/(a.v*a.v))
 def __truediv__(a,b):return a*qq(b).inv()
 def __rtruediv__(a,b):return qq(b)/a
def qq(x):return x if isinstance(x,Q) else Q(iv(x),iv(0))
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
p=I(F(2*3141592653589793238,10**18),F(2*3141592653589793239,10**18))
def evaluate(ql,qh):
 q=Q(I(ql,qh),iv(1));A=Q(p,iv(0))/q;h=[qq(0) for _ in range(N)]
 for n in range(1,N):h[n]=qq(F(1,factorial(2*n)))
 b=scale(h,6*A/((A-3)*(A-3)));m=add(scale(h,A),log1m(b));m4=[m[n]*4**n for n in range(N)];eta=sub(m4,scale(m,4))
 one=[qq(1)]+[qq(0)]*(N-1);u=sub(one,exp0(scale(m,-2)));R=sub(mul(u,u),mul(exp0(scale(m,-4)),sub(one,exp0(neg(eta)))))
 Hs=[(n-2)*R[n].v for n in range(3,N)];Js=[q.v*R[n].d+n*R[n].v for n in range(2,N)];z=I(ql/1000,F(1,64))
 def horner(c):
  v=iv(0)
  for a in reversed(c):v=v*z+a
  return v
 return horner(Hs),horner(Js)
q0,q1=F(3,10),F(7,16);boxes=512;records=[]
for k in range(boxes):
 ql=q0+(q1-q0)*k/boxes;qh=q0+(q1-q0)*(k+1)/boxes;H,J=evaluate(ql,qh)
 records.append({"q":[str(ql),str(qh)],"H_hi":float(H.hi),"J_lo":float(J.lo),
  "accepted":H.hi < -14 and J.lo > F(7,10)})
result={"scope":"512 disjoint Chart-1 q cells with exact degree-13 scaled polynomial enclosures","q_boxes":boxes,
 "accepted":sum(x["accepted"] for x in records),"records":records}
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-chart1-scaled-taylor-q-cover.json").write_text(out);print(out,end="")
