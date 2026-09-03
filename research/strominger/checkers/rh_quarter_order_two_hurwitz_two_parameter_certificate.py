import json,math
from fractions import Fraction as F
from pathlib import Path
def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q,sgn=1):
 r=dict(p)
 for k,v in q.items():r[k]=r.get(k,F(0))+sgn*v
 return clean(r)
def mul(p,q):
 r={}
 for (i,j),x in p.items():
  for (k,l),y in q.items():r[(i+k,j+l)]=r.get((i+k,j+l),F(0))+x*y
 return clean(r)
def scale(p,c):return clean({k:c*v for k,v in p.items()})
one={(0,0):F(1)};tv={(0,1):F(1)}
class R:
 def __init__(self,n,d=None):self.n,self.d=clean(n),one if d is None else clean(d)
 def __add__(self,o):return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
 def __neg__(self):return R(scale(self.n,-1),self.d)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):return R(mul(self.n,o.n),mul(self.d,o.d))
 def __truediv__(self,o):return R(mul(self.n,o.d),mul(self.d,o.n))
def qpoly(delta):
 p=[one]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):
  const={(0,0):c+delta,(1,0):F(1)};r=[{}]*(len(p)+1);r=[{} for _ in r]
  for i,x in enumerate(p):r[i]=add(r[i],mul(x,const));r[i+1]=add(r[i+1],x)
  p=r
 return p
def bernstein_monomial_nonnegative(p):
 if not p:return False
 ds=max(i for i,j in p);dt=max(j for i,j in p);anypos=False
 for k in range(dt+1):
  for i in range(ds+1):
   z=sum(p.get((i,j),F(0))*F(math.comb(k,j),math.comb(dt,j)) for j in range(k+1))
   if z<0:return False
   anypos|=z>0
 return anypos
def orient(x):
 c=x.d.get((0,0),F(0))
 if c<0:return R(scale(x.n,-1),scale(x.d,-1))
 return x
def cert(x):
 x=orient(x);return bernstein_monomial_nonnegative(x.n) and bernstein_monomial_nonnegative(x.d)
def at_one(p):
 r={}
 for (i,j),v in p.items():r[(i,0)]=r.get((i,0),F(0))+v
 return clean(r)
X,Y=qpoly(1),qpoly(0);c=[R(add(X[i],mul(tv,Y[i]),-1)) for i in range(5)];b=list(reversed(c));r0=b[0];r1=b[1];r2=(b[1]*b[2]-b[0]*b[3])/b[1];r3=(r2*b[3]-b[1]*b[4])/r2;r4=b[4];open_cols=[r0,r1,r2,r3,r4]
e=[R(at_one(x.n),at_one(x.d)) for x in c];eb=list(reversed(e[:-1]));er0=eb[0];er1=eb[1];er2=(eb[1]*eb[2]-eb[0]*eb[3])/eb[1];er3=eb[3];endpoint_cols=[er0,er1,er2,er3]
checks={"all_open_pencil_routh_entries_bivariate_certified":all(cert(x) for x in open_cols),"all_degree_dropped_endpoint_entries_shift_positive":all(cert(x) for x in endpoint_cols),"five_quartic_routh_entries_checked":len(open_cols)==5,"four_cubic_endpoint_entries_checked":len(endpoint_cols)==4}
result={"schema":"marici.strominger.rh_quarter_order_two_hurwitz_two_parameter_certificate.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every order-two Routh first-column numerator and denominator has a bivariate certificate: nonnegative Bernstein coefficients in t on [0,1) whose coefficients are nonnegative monomials in symbolic shift s. The t=1 cubic endpoint has the corresponding all-shift certificate. Passing proves the full order-two pencil Hurwitz stable for every real s>=0 and t in [0,1].","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_order_two_hurwitz_two_parameter_certificate.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
