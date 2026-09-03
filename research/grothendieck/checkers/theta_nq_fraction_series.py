"""Dependency-free exact y-series test for coefficient positivity of partial_y Nq."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
N=20
@dataclass(frozen=True)
class J:
 v:F; d:F
 def __add__(a,b):b=j(b);return J(a.v+b.v,a.d+b.d)
 __radd__=__add__
 def __neg__(a):return J(-a.v,-a.d)
 def __sub__(a,b):return a+(-j(b))
 def __rsub__(a,b):return j(b)-a
 def __mul__(a,b):b=j(b);return J(a.v*b.v,a.d*b.v+a.v*b.d)
 __rmul__=__mul__
 def inv(a):return J(1/a.v,-a.d/(a.v*a.v))
 def __truediv__(a,b):return a*j(b).inv()
 def __rtruediv__(a,b):return j(b)/a
def j(x):return x if isinstance(x,J) else J(F(x),F(0))
def add(a,b):return [a[k]+b[k] for k in range(N)]
def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 out=[j(0) for _ in range(N)]
 for i in range(N):
  for k in range(N-i):out[i+k]=out[i+k]+a[i]*b[k]
 return out
def scale(a,c):return [x*c for x in a]
def exp0(a):
 # valid for a[0]=0
 out=[j(0) for _ in range(N)];out[0]=j(1);power=out[:]
 for k in range(1,N):power=mul(power,a);out=add(out,scale(power,F(1,factorial(k))))
 return out
def log1m(a):
 out=[j(0) for _ in range(N)];power=[j(0) for _ in range(N)];power[0]=j(1)
 for k in range(1,N):power=mul(power,a);out=add(out,scale(power,F(1,k)))
 return out
def build(qv,pv):
 q=J(qv,1);A=J(pv,0)/q
 z=[j(0) for _ in range(N)]
 for n in range(1,N):z[n]=q**n if False else J(q.v**n,n*q.v**(n-1)*q.d)
 h=[z[n]/factorial(2*n) for n in range(N)]
 den=(A-3)*(A-3);b=scale(h,6*A/den)
 m=add(scale(h,A),log1m(b));m4=[m[n]*(4**n) for n in range(N)];eta=sub(m4,scale(m,4))
 u=sub([j(1)]+[j(0)]*(N-1),exp0(scale(m,-2)))
 c=sub([j(1)]+[j(0)]*(N-1),exp0(neg(eta)))
 e2,e4,ee=exp0(scale(m,-2)),exp0(scale(m,-4)),exp0(neg(eta))
 mq=[J(x.d,0) for x in m];etaq=[J(x.d,0) for x in eta]
 nq=add(scale(mul(mul(u,e2),mq),4),mul(e4,sub(scale(mul(mq,c),4),mul(ee,etaq))))
 return nq
P=[F(2*3141592653589793238,10**18),F(2*3141592653589793239,10**18)]
Q=[F(3,10),F(7,16)];rows=[];negative=[];balances=[];tail_diagnostics=[]
for p in P:
 for q in Q:
  nq=build(q,p);coeff=[n*nq[n].v for n in range(1,N)]
  rows.append([str(x) for x in coeff])
  negative += [(str(p),str(q),n) for n,x in enumerate(coeff) if x<0]
  terms=[coeff[k]*F(1,28)**k for k in range(len(coeff))]
  positive=sum((x for x in terms if x>0),F(0));negative_mass=-sum((x for x in terms if x<0),F(0))
  balances.append((positive-negative_mass,positive,negative_mass,p,q))
  nz=[abs(x) for x in terms if x]
  ratios=[nz[k]/nz[k-1] for k in range(max(1,len(nz)-5),len(nz))]
  tail_diagnostics.append((max(ratios),nz[-1],p,q))
worst=min(balances);worst_ratio=max(tail_diagnostics)
# Exact diagnostic for a centered/secant q model at the worst physical y.
q0,q1=Q;secant_errors=[];q_monotone=True
for p in P:
 vals=[]
 for i in range(5):
  q=q0+(q1-q0)*i/4;nq=build(q,p)
  vals.append(sum((n*nq[n].v*F(1,28)**(n-1) for n in range(1,N)),F(0)))
 q_monotone &= all(vals[i+1]>=vals[i] for i in range(4))
 for i in range(1,4):secant_errors.append(abs(vals[i]-(vals[0]+(vals[4]-vals[0])*F(i,4))))
result={"scope":"four rational (p,q) endpoint cases; not a parameter-uniform enclosure",
"partial_y_polynomial_degree":N-2,"cases":4,"negative_coefficient_count":len(negative),
"negative_degrees":sorted(set(x[2] for x in negative)),"all_nonnegative":not negative,
"minimum_truncated_value_positive":worst[0]>0,"minimum_truncated_value_exact":str(worst[0]),
"minimum_truncated_value_float":float(worst[0]),
"negative_to_positive_mass_float":float(worst[2]/worst[1]),
"max_observed_last_five_term_ratio_float":float(worst_ratio[0]),
"associated_last_term_abs_float":float(worst_ratio[1]),
"q_secant_max_error_at_y_1_over_28_float":float(max(secant_errors)),
"five_point_q_monotone":q_monotone,"p":str(worst[3]),"q":str(worst[4])}
out=json.dumps(result,indent=2)+"\n"
Path("research/grothendieck/results/theta-nq-fraction-series.json").write_text(out)
print(out,end="")
assert negative and worst[0]>0
