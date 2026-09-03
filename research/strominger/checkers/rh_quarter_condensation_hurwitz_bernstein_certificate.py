import json,math
from fractions import Fraction as F
from pathlib import Path
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(p,q,s=1):
 r=[F(0)]*max(len(p),len(q))
 for i,x in enumerate(p):r[i]+=x
 for i,x in enumerate(q):r[i]+=s*x
 return trim(r)
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return trim(r)
class R:
 def __init__(self,n,d=None):self.n,self.d=trim(n),[F(1)] if d is None else trim(d)
 def __add__(self,o):return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
 def __neg__(self):return R([-x for x in self.n],self.d)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):return R(mul(self.n,o.n),mul(self.d,o.d))
 def __truediv__(self,o):return R(mul(self.n,o.d),mul(self.d,o.n))
def pa_mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return r
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=pa_mul(p,[c+s,F(1)])
 return p
def bernstein(p):
 d=len(p)-1
 return [sum(p[j]*F(math.comb(k,j),math.comb(d,j)) for j in range(k+1)) for k in range(d+1)]
def cert(x):
 sign=F(1) if x.d[0]>0 else F(-1);bn=bernstein([sign*c for c in x.n]);bd=bernstein([sign*c for c in x.d]);return all(c>=0 for c in bn) and any(c>0 for c in bn) and all(c>=0 for c in bd) and any(c>0 for c in bd)
def endpoint_routh_cubic(p):
 b=list(reversed(trim(p)));return len(b)==4 and b[0]>0 and b[1]>0 and (b[1]*b[2]-b[0]*b[3])/b[1]>0 and b[3]>0
records=[]
for s in range(5):
 X,Y=Q(s+1),Q(s);c=[R([X[i],-Y[i]]) for i in range(5)];b=list(reversed(c));r0=b[0];r1=b[1];r2=(b[1]*b[2]-b[0]*b[3])/b[1];r3=(r2*b[3]-b[1]*b[4])/r2;r4=b[4];cols=[r0,r1,r2,r3,r4]
 endpoint=[X[i]-Y[i] for i in range(5)]
 records.append({"shift_offset":s,"all_symbolic_routh_entries_bernstein_nonnegative":all(cert(x) for x in cols),"endpoint_cubic_hurwitz":endpoint_routh_cubic(endpoint),"entry_count":len(cols)})
checks={"continuous_open_pencils_bernstein_certified":all(r["all_symbolic_routh_entries_bernstein_nonnegative"] for r in records),"all_t_one_endpoints_hurwitz":all(r["endpoint_cubic_hurwitz"] for r in records),"five_shift_offsets_certified":len(records)==5,"all_five_routh_entries_checked":all(r["entry_count"]==5 for r in records)}
result={"schema":"marici.strominger.rh_quarter_condensation_hurwitz_bernstein_certificate.v1","status":"passed" if all(checks.values()) else "failed","verdict":"At source order two, every symbolic Routh first-column numerator and denominator for X-tY has a nonnegative Bernstein certificate on 0<=t<1, and each degree-dropped t=1 endpoint is Hurwitz stable. This proves continuous pencil stability at five shift offsets, not at higher source order.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_condensation_hurwitz_bernstein_certificate.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
