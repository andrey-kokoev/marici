"""Exact natural-interval q-curvature test for finite partial_y Nq polynomial."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=20;K=4
@dataclass(frozen=True)
class I:
 lo:F;hi:F
 def __add__(a,b):b=iv(b);return I(a.lo+b.lo,a.hi+b.hi)
 __radd__=__add__
 def __neg__(a):return I(-a.hi,-a.lo)
 def __sub__(a,b):return a+(-iv(b))
 def __rsub__(a,b):return iv(b)-a
 def __mul__(a,b):
  b=iv(b);z=(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi);return I(min(z),max(z))
 __rmul__=__mul__
 def inv(a):assert a.lo>0 or a.hi<0;return I(1/a.hi,1/a.lo)
 def __truediv__(a,b):return a*iv(b).inv()
 def __rtruediv__(a,b):return iv(b)/a
def iv(x):return x if isinstance(x,I) else I(F(x),F(x))
@dataclass(frozen=True)
class T:
 c:tuple
 def __add__(a,b):b=tt(b);return T(tuple(a.c[i]+b.c[i] for i in range(K)))
 __radd__=__add__
 def __neg__(a):return T(tuple(-x for x in a.c))
 def __sub__(a,b):return a+(-tt(b))
 def __rsub__(a,b):return tt(b)-a
 def __mul__(a,b):
  b=tt(b);return T(tuple(sum((a.c[j]*b.c[i-j] for j in range(i+1)),iv(0)) for i in range(K)))
 __rmul__=__mul__
 def inv(a):
  z=[a.c[0].inv()]
  for n in range(1,K):z.append(-sum((a.c[j]*z[n-j] for j in range(1,n+1)),iv(0))/a.c[0])
  return T(tuple(z))
 def __truediv__(a,b):return a*tt(b).inv()
 def __rtruediv__(a,b):return tt(b)/a
 def __pow__(a,n):
  z=tt(1)
  for _ in range(n):z=z*a
  return z
def tt(x):return x if isinstance(x,T) else T((iv(x),)+(iv(0),)*(K-1))
def add(a,b):return [a[i]+b[i] for i in range(N)]
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[tt(0) for _ in range(N)]
 for i in range(N):
  for j in range(N-i):z[i+j]=z[i+j]+a[i]*b[j]
 return z
def scale(a,c):return [x*c for x in a]
def exp0(a):
 z=[tt(0) for _ in range(N)];z[0]=tt(1);power=z[:]
 for k in range(1,N):power=mul(power,a);z=add(z,scale(power,F(1,factorial(k))))
 return z
def log1m(a):
 z=[tt(0) for _ in range(N)];power=[tt(0) for _ in range(N)];power[0]=tt(1)
 for k in range(1,N):power=mul(power,a);z=add(z,scale(power,F(1,k)))
 return z
def build(ql,qh):
 q=T((I(ql,qh),iv(1),iv(0),iv(0)));p=I(F(2*3141592653589793238,10**18),F(2*3141592653589793239,10**18));A=tt(p)/q
 h=[tt(0) for _ in range(N)]
 for n in range(1,N):h[n]=q**n/factorial(2*n)
 b=scale(h,6*A/((A-3)*(A-3)));m=add(scale(h,A),log1m(b));m4=[m[n]*(4**n) for n in range(N)];eta=sub(m4,scale(m,4))
 one=[tt(1)]+[tt(0)]*(N-1);u=sub(one,exp0(scale(m,-2)));c=sub(one,exp0(neg(eta)))
 # q derivative shifts normalized Taylor coefficients.
 mq=[T((x.c[1],2*x.c[2],3*x.c[3],iv(0))) for x in m];etaq=[T((x.c[1],2*x.c[2],3*x.c[3],iv(0))) for x in eta]
 nq=add(scale(mul(mul(u,exp0(scale(m,-2))),mq),4),mul(exp0(scale(m,-4)),sub(scale(mul(mq,c),4),mul(exp0(neg(eta)),etaq))))
 # q curvature of partial_y polynomial: second derivative = 2*T coefficient 2.
 return [2*n*nq[n].c[2] for n in range(1,N)]
q0,q1=F(3,10),F(7,16);y=I(F(1,1000),F(1,28));boxes=4;records=[]
for k in range(boxes):
 lo=q0+(q1-q0)*k/boxes;hi=q0+(q1-q0)*(k+1)/boxes;coef=build(lo,hi);v=iv(0)
 for a in reversed(coef):v=v*y+a
 remainder=max(abs(v.lo),abs(v.hi))*(hi-lo)**2/8
 records.append((remainder,v,lo,hi))
worst=max(records,key=lambda x:x[0])
result={"scope":"four equal exact q boxes; natural interval q-curvature enclosures","q_boxes":boxes,
 "worst_curvature_lower_float":float(worst[1].lo),"worst_curvature_upper_float":float(worst[1].hi),
 "maximum_secant_remainder_float":float(worst[0]),"boxes_useful_against_margin_0_387":sum(x[0]<F(387,1000) for x in records)}
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-nq-y-polynomial-q-curvature.json").write_text(out);print(out,end="")
