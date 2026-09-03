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
 p=p[:];z=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]=c;p=add(p,[F(0)]*d+[c*x for x in q],-1)
 assert p==[F(0)];return trim(z)
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mul(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s):
 if n<=1:return [F(1)]
 X=mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2));Y=mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1));return divexact(add(X,Y,-1),D(n-2,s+2))
def pos(p):return all(x>0 for x in p)
records=[]
for n in range(2,11):
 for s in range(5):
  X=mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2));Y=mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1));gap=add(X,Y,-1);div=D(n-2,s+2);quot=divexact(gap,div)
  records.append({"order":n,"shift_offset":s,"coefficientwise_dominance":pos(gap),"divisor_positive":pos(div),"quotient_positive":pos(quot),"recurrence_exact":quot==D(n,s)})
counter_div=[F(1),F(1)];counter_quot=[F(1),F(-1),F(1)];counter_num=mul(counter_div,counter_quot)
checks={"actual_condensation_gaps_coefficientwise_positive":all(r["coefficientwise_dominance"] for r in records),"actual_source_polynomials_coefficientwise_positive":all(r["divisor_positive"] and r["quotient_positive"] for r in records),"all_exact_divisions_verified":all(r["recurrence_exact"] for r in records),"tested_45_recurrences":len(records)==45,"nonnegative_division_cone_counterexample":all(x>=0 for x in counter_div) and all(x>=0 for x in counter_num) and any(x<0 for x in counter_quot) and counter_num==[F(1),F(0),F(0),F(1)]}
result={"schema":"marici.strominger.rh_quarter_jacobi_positive_polynomial_induction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The actual source recurrence has coefficientwise-positive gaps, divisors, and quotients through order ten and five shift offsets. But positive exact division does not preserve the positive-coefficient cone: (1+a^3)/(1+a)=1-a+a^2. Therefore condensation dominance alone cannot induct polynomial positivity; an additional divisibility structure or positive basis is required.","record_count":len(records),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_jacobi_positive_polynomial_induction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
