"""Exact rational interval test of the finite partial_y Nq polynomial."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=20
@dataclass(frozen=True)
class I:
 lo:F; hi:F
 def __add__(a,b):b=iv(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+(-iv(b))
 def __rsub__(a,b):return iv(b)-a
 def __mul__(a,b):
  b=iv(b);z=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi];return I(min(z),max(z))
 __rmul__=__mul__
 def inv(a):assert a.lo>0 or a.hi<0;return I(1/a.hi,1/a.lo)
 def __truediv__(a,b):return a*iv(b).inv()
 def __rtruediv__(a,b):return iv(b)/a
def iv(x):return x if isinstance(x,I) else I(F(x),F(x))
@dataclass(frozen=True)
class J:
 v:I; d:I
 def __add__(a,b):b=jj(b);return J(a.v+b.v,a.d+b.d)
 __radd__=__add__
 def __neg__(a):return J(-a.v,-a.d)
 def __sub__(a,b):return a+(-jj(b))
 def __rsub__(a,b):return jj(b)-a
 def __mul__(a,b):b=jj(b);return J(a.v*b.v,a.d*b.v+a.v*b.d)
 __rmul__=__mul__
 def inv(a):return J(a.v.inv(),-a.d/(a.v*a.v))
 def __truediv__(a,b):return a*jj(b).inv()
 def __rtruediv__(a,b):return jj(b)/a
 def __pow__(a,n):
  z=jj(1)
  for _ in range(n):z=z*a
  return z
def jj(x):return x if isinstance(x,J) else J(iv(x),iv(0))
def add(a,b):return [a[k]+b[k] for k in range(N)]
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 out=[jj(0) for _ in range(N)]
 for i in range(N):
  for k in range(N-i):out[i+k]=out[i+k]+a[i]*b[k]
 return out
def scale(a,c):return [x*c for x in a]
def exp0(a):
 out=[jj(0) for _ in range(N)];out[0]=jj(1);power=out[:]
 for k in range(1,N):power=mul(power,a);out=add(out,scale(power,F(1,factorial(k))))
 return out
def log1m(a):
 out=[jj(0) for _ in range(N)];power=[jj(0) for _ in range(N)];power[0]=jj(1)
 for k in range(1,N):power=mul(power,a);out=add(out,scale(power,F(1,k)))
 return out
p=I(F(2*3141592653589793238,10**18),F(2*3141592653589793239,10**18))
def coefficients(ql,qh):
 q=J(I(ql,qh),iv(1));A=J(p,iv(0))/q;h=[jj(0) for _ in range(N)]
 for n in range(1,N):h[n]=q**n/factorial(2*n)
 b=scale(h,6*A/((A-3)*(A-3)));m=add(scale(h,A),log1m(b));m4=[m[n]*(4**n) for n in range(N)];eta=sub(m4,scale(m,4))
 one=[jj(1)]+[jj(0)]*(N-1);u=sub(one,exp0(scale(m,-2)));c=sub(one,exp0(neg(eta)))
 mq=[J(x.d,iv(0)) for x in m];etaq=[J(x.d,iv(0)) for x in eta]
 nq=add(scale(mul(mul(u,exp0(scale(m,-2))),mq),4),mul(exp0(scale(m,-4)),sub(scale(mul(mq,c),4),mul(exp0(neg(eta)),etaq))))
 return [n*nq[n].v for n in range(1,N)]
q0,q1=F(3,10),F(7,16);y=I(F(1,1000),F(1,28));tail=F(14,10**7);boxes=4;lowers=[]
for k in range(boxes):
 coeff=coefficients(q0+(q1-q0)*k/boxes,q0+(q1-q0)*(k+1)/boxes);v=iv(0)
 for a in reversed(coeff):v=v*y+a
 lowers.append(v.lo)
result={"scope":"four equal exact q boxes; full y interval per box","q_boxes":boxes,
 "minimum_lower":str(min(lowers)),"minimum_lower_float":float(min(lowers)),"tail_upper":str(tail),
 "certifies_after_tail":min(lowers)>tail,"accepted_boxes":sum(x>tail for x in lowers)}
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-nq-y-polynomial-q-cover.json").write_text(out);print(out,end="")
