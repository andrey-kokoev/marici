import json,math
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
def tr(p):
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
def ex(p,q):
 p=p[:];z=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]=c;p=ad(p,[F(0)]*d+[c*x for x in q],-1)
 assert p==[F(0)];return tr(z)
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mu(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s):
 if n<=1:return [F(1)]
 return ex(ad(mu(mu(Q(s+n-1),D(n-1,s)),D(n-1,s+2)),mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1)),-1),D(n-2,s+2))
def det(A):
 A=[r[:] for r in A];n=len(A);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  A[k],A[p]=A[p],A[k]
  if p!=k:out=-out
  z=A[k][k];out*=z
  for j in range(k,n):A[k][j]/=z
  for i in range(k+1,n):
   z=A[i][k]
   for j in range(k,n):A[i][j]-=z*A[k][j]
 return out
def hurwitz_minor(p,k):
 n=len(p)-1
 def a(idx):return p[idx] if 0<=idx<=n else F(0)
 H=[]
 for i in range(k):
  row=[]
  for j in range(k):
   if i%2==0:idx=n-(2*(j-i//2)+1)
   else:idx=n-2*(j-(i-1)//2)
   row.append(a(idx))
  H.append(row)
 return det(H)
def interp(xs,ys):
 out=[F(0)]
 for i,x in enumerate(xs):
  basis=[F(1)];den=F(1)
  for j,y in enumerate(xs):
   if i!=j:basis=mu(basis,[-y,F(1)]);den*=x-y
  out=ad(out,[ys[i]*c/den for c in basis])
 return tr(out)
def bern(p,d):
 p=p+[F(0)]*(d+1-len(p));return [sum(p[j]*F(math.comb(k,j),math.comb(d,j)) for j in range(k+1)) for k in range(d+1)]
s=0;X=mu(mu(Q(3),D(3,0)),D(3,2));Y=mu(mu(Q(0),D(3,1)),D(3,1));L=max(len(X),len(Y));X += [F(0)]*(L-len(X));Y += [F(0)]*(L-len(Y));degree=L-1
records=[];first_failure=None
for k in range(1,degree+1):
 xs=[F(j,k) for j in range(k+1)];ys=[hurwitz_minor([X[i]-t*Y[i] for i in range(L)],k) for t in xs];poly=interp(xs,ys);b=bern(poly,k);ok=all(z>=0 for z in b) and ys[0]>0
 rec={"minor_order":k,"interpolated_degree":len(poly)-1,"bernstein_nonnegative":ok,"zero_bernstein_coefficients":sum(z==0 for z in b)};records.append(rec)
 if not ok and first_failure is None:first_failure=rec
endpoint=tr(ad(X,Y,-1));endpoint_ok=all(hurwitz_minor(endpoint,k)>0 for k in range(1,len(endpoint)))
checks={"all_open_hurwitz_minors_bernstein_nonnegative":first_failure is None,"degree_dropped_endpoint_hurwitz":endpoint_ok,"all_twenty_two_principal_minors_checked":len(records)==22,"open_leading_coefficient_positive":X[-1]>0 and X[-1]==Y[-1]}
result={"schema":"marici.strominger.rh_quarter_order_four_interpolated_hurwitz_minors.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Each order-four parametric Hurwitz principal minor is reconstructed exactly from its degree-bounded rational samples and tested in the Bernstein basis. Passing certifies every open-pencil minor on 0<=t<1 and the degree-dropped endpoint separately, proving continuous Hurwitz stability without recursive symbolic Routh fractions.","pencil_degree":degree,"records":records,"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_order_four_interpolated_hurwitz_minors.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
