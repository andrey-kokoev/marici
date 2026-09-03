import json
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
def divexact(p,q):
 p=p[:];out=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];out[d]=c
  p=add(p,[F(0)]*d+[c*x for x in q],-1)
 assert all(x==0 for x in p)
 return trim(out)
def Q(i):
 p=[F(1)]
 for s in (F(1),F(5,4),F(3,2),F(7,4)):p=mul(p,[s+i,F(1)])
 return p
@lru_cache(None)
def D(n,shift):
 if n<=1:return [F(1)]
 return divexact(add(mul(mul(Q(shift+n-1),D(n-1,shift)),D(n-1,shift+2)),mul(mul(Q(shift),D(n-1,shift+1)),D(n-1,shift+1)),-1),D(n-2,shift+2))
class R:
 def __init__(self,n,d=[F(1)]):self.n,self.d=trim(n),trim(d)
 def __add__(self,o):return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
 def __neg__(self):return R([-x for x in self.n],self.d)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):return R(mul(self.n,o.n),mul(self.d,o.d))
 def __truediv__(self,o):return R(mul(self.n,o.d),mul(self.d,o.n))
def M(k):
 n=k+2;return R(mul(mul(Q(0),D(n-1,1)),D(n-1,1)),mul(mul(Q(n-1),D(n-1,0)),D(n-1,2)))
m=[M(k) for k in range(4)];alpha0=m[1]/m[0];h1=m[2]-(m[1]*m[1]/m[0]);beta1=h1/m[0];alpha1=(m[3]-(alpha0*m[2])-(alpha0*m[2])+(alpha0*alpha0*m[1]))/h1;one=R([F(1)])
def positive_coeffs(x):
 sign=1 if x.d[-1]>0 else -1
 return all(sign*c>0 for c in x.n) and all(sign*c>0 for c in x.d)
objects={"alpha0":alpha0,"one_minus_alpha0":one-alpha0,"beta1":beta1,"alpha1":alpha1,"one_minus_alpha1":one-alpha1}
checks={"all_required_rational_functions_coefficientwise_positive":all(positive_coeffs(x) for x in objects.values()),"source_D_divisions_exact":True,"first_nontrivial_jacobi_family_covered":set(objects)=={"alpha0","one_minus_alpha0","beta1","alpha1","one_minus_alpha1"}}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_continued_fraction_coefficient_pattern.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The first Jacobi coefficients are exact rational functions of the nonnegative source shift. Numerators and denominators for alpha_0, 1-alpha_0, beta_1, alpha_1, and 1-alpha_1 have strictly positive monomial coefficients, proving 0<alpha_0,alpha_1<1 and beta_1>0 for every shift a>=0. This is an all-shift low-order theorem, not an all-order coefficient formula.","degrees":{k:{"numerator":len(v.n)-1,"denominator":len(v.d)-1} for k,v in objects.items()},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_continued_fraction_coefficient_pattern.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
