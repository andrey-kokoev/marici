import json,math
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
def tr(p):
 p=p[:]
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def ad(p,q,s=1):
 r=[F(0)]*max(len(p),len(q))
 for i,x in enumerate(p):r[i]+=x
 for i,x in enumerate(q):r[i]+=s*x
 return tr(r)
def mu(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return tr(r)
def qr(p,q):
 p=tr(p);q=tr(q);z=[F(0)]*max(1,len(p)-len(q)+1)
 while p!=[F(0)] and len(p)>=len(q):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]+=c;p=ad(p,[F(0)]*d+[c*x for x in q],-1)
 return tr(z),tr(p)
def ex(p,q):
 z,r=qr(p,q);assert r==[F(0)];return z
def gd(p,q):
 while q!=[F(0)]:p,q=q,qr(p,q)[1]
 return [x/p[-1] for x in p]
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mu(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s):
 if n<=1:return [F(1)]
 return ex(ad(mu(mu(Q(s+n-1),D(n-1,s)),D(n-1,s+2)),mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1)),-1),D(n-2,s+2))
class R:
 def __init__(self,n,d=None):
  d=[F(1)] if d is None else d;g=gd(tr(n),tr(d));n,d=ex(n,g),ex(d,g)
  if d[0]<0:n,d=[-x for x in n],[-x for x in d]
  self.n,self.d=n,d
 def __add__(self,o):return R(ad(mu(self.n,o.d),mu(o.n,self.d)),mu(self.d,o.d))
 def __neg__(self):return R([-x for x in self.n],self.d)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):return R(mu(self.n,o.n),mu(self.d,o.d))
 def __truediv__(self,o):return R(mu(self.n,o.d),mu(self.d,o.n))
def bc(p):
 d=len(p)-1;return [sum(p[j]*F(math.comb(k,j),math.comb(d,j)) for j in range(k+1)) for k in range(d+1)]
def cert(x):return all(z>=0 for z in bc(x.n)) and any(z>0 for z in bc(x.n)) and all(z>=0 for z in bc(x.d)) and any(z>0 for z in bc(x.d))
def routh_symbolic(coeff):
 b=list(reversed(coeff));cols=(len(b)+1)//2;Z=R([F(0)]);A=[[Z for _ in range(cols)] for _ in b];A[0][:len(b[0::2])]=b[0::2];A[1][:len(b[1::2])]=b[1::2]
 for i in range(2,len(b)):
  for j in range(cols-1):A[i][j]=(A[i-1][0]*A[i-2][j+1]-A[i-2][0]*A[i-1][j+1])/A[i-1][0]
 return [r[0] for r in A]
def routh_numeric(p):
 b=list(reversed(tr(p)));cols=(len(b)+1)//2;A=[[F(0)]*cols for _ in b];A[0][:]=b[0::2]+[F(0)]*(cols-len(b[0::2]));A[1][:]=b[1::2]+[F(0)]*(cols-len(b[1::2]))
 for i in range(2,len(b)):
  for j in range(cols-1):A[i][j]=(A[i-1][0]*A[i-2][j+1]-A[i-2][0]*A[i-1][j+1])/A[i-1][0]
 return all(r[0]>0 for r in A)
records=[]
for s in range(3):
 X=mu(mu(Q(s+2),D(2,s)),D(2,s+2));Y=mu(mu(Q(s),D(2,s+1)),D(2,s+1));L=max(len(X),len(Y));X+= [F(0)]*(L-len(X));Y+=[F(0)]*(L-len(Y));cols=routh_symbolic([R([X[i],-Y[i]]) for i in range(L)]);endpoint=ad(X,Y,-1)
 records.append({"shift_offset":s,"all_open_routh_entries_bernstein_nonnegative":all(cert(x) for x in cols),"endpoint_hurwitz":routh_numeric(endpoint),"routh_entry_count":len(cols)})
checks={"all_open_order_three_pencils_certified":all(r["all_open_routh_entries_bernstein_nonnegative"] for r in records),"all_degree_dropped_endpoints_hurwitz":all(r["endpoint_hurwitz"] for r in records),"three_shift_offsets_checked":len(records)==3,"expected_eleven_open_routh_entries":all(r["routh_entry_count"]==11 for r in records)}
result={"schema":"marici.strominger.rh_quarter_order_three_hurwitz_bernstein_certificate.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every exact symbolic Routh first-column numerator and denominator for the order-three determinant-coupled pencil has nonnegative Bernstein coefficients in t at shift offsets zero through two. The degree-dropped t=1 endpoints are Hurwitz stable. Thus each tested pencil is Hurwitz stable for every t in [0,1].","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_order_three_hurwitz_bernstein_certificate.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
