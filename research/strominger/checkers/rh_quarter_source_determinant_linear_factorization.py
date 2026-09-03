import json,math
from fractions import Fraction as F
from functools import lru_cache
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
def divmodp(p,q):
 p=p[:];z=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]=c;p=add(p,[F(0)]*d+[c*x for x in q],-1)
 return trim(z),trim(p)
def exact(p,q):
 z,r=divmodp(p,q);assert r==[F(0)];return z
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mul(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s=0):
 if n<=1:return [F(1)]
 X=mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2));Y=mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1));return exact(add(X,Y,-1),D(n-2,s+2))
def squareq(x):return x>=0 and math.isqrt(x.numerator)**2==x.numerator and math.isqrt(x.denominator)**2==x.denominator
p2=D(2);root=F(15,8);quad,rem=divmodp(p2,[root,F(1)]);disc=quad[1]**2-4*quad[2]*quad[0]
records=[]
for n in range(2,9):
 p=D(n);roots=[]
 for j in range(1,8*(4*n+4)+1):
  c=F(j,8)
  while True:
   z,r=divmodp(p,[c,F(1)])
   if r!=[F(0)]:break
   roots.append(str(c));p=z
 records.append({"order":n,"degree":len(D(n))-1,"eighth_lattice_root_count":len(roots),"residual_degree":len(p)-1,"roots":roots})
checks={"order_two_center_root_exact":rem==[F(0)],"order_two_residual_is_quadratic":len(quad)-1==2,"order_two_quadratic_not_rationally_split":not squareq(disc),"complete_positive_rational_linear_factorization_excluded":len(quad)-1==2 and not squareq(disc),"bounded_orders_censused":len(records)==7}
result={"schema":"marici.strominger.rh_quarter_source_determinant_linear_factorization.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The positive-linear-factor proposal already fails for D_2(a). It has the exact center factor a+15/8, but the residual quadratic has nonsquare discriminant, so D_2 does not split into rational linear factors. The eighth-lattice census through order eight cannot restore a factor-multiplicity induction.","order_two_discriminant":str(disc),"records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_source_determinant_linear_factorization.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
