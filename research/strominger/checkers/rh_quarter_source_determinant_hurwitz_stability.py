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
def exact(p,q):
 p=p[:];z=[F(0)]*max(1,len(p)-len(q)+1)
 while len(p)>=len(q) and any(p):
  d=len(p)-len(q);c=p[-1]/q[-1];z[d]=c;p=add(p,[F(0)]*d+[c*x for x in q],-1)
 assert p==[F(0)];return trim(z)
def Q(s):
 p=[F(1)]
 for c in (F(1),F(5,4),F(3,2),F(7,4)):p=mul(p,[c+s,F(1)])
 return p
@lru_cache(None)
def D(n,s=0):
 if n<=1:return [F(1)]
 return exact(add(mul(mul(Q(s+n-1),D(n-1,s)),D(n-1,s+2)),mul(mul(Q(s),D(n-1,s+1)),D(n-1,s+1)),-1),D(n-2,s+2))
def routh_first(p):
 b=list(reversed(p));cols=(len(b)+1)//2;rows=[[F(0)]*cols for _ in range(len(b))]
 rows[0][:]=b[0::2]+[F(0)]*(cols-len(b[0::2]));rows[1][:]=b[1::2]+[F(0)]*(cols-len(b[1::2]))
 for i in range(2,len(b)):
  if rows[i-1][0]==0:return [r[0] for r in rows[:i]]+[F(0)]
  for j in range(cols-1):rows[i][j]=(rows[i-1][0]*rows[i-2][j+1]-rows[i-2][0]*rows[i-1][j+1])/rows[i-1][0]
 return [r[0] for r in rows]
records=[];first_failure=None
for n in range(2,8):
 p=D(n);first=routh_first(p);ok=all(x>0 for x in first);rec={"order":n,"degree":len(p)-1,"all_polynomial_coefficients_positive":all(x>0 for x in p),"routh_first_column_positive":ok,"first_nonpositive_row":next((i for i,x in enumerate(first) if x<=0),None)};records.append(rec)
 if not ok and first_failure is None:first_failure=rec
checks={"all_source_coefficients_positive":all(r["all_polynomial_coefficients_positive"] for r in records),"all_exact_routh_columns_positive":first_failure is None,"tested_orders_two_through_seven":len(records)==6,"order_two_complex_pair_compatible_with_stability":records[0]["routh_first_column_positive"]}
result={"schema":"marici.strominger.rh_quarter_source_determinant_hurwitz_stability.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Routh arrays test whether every root of each bounded source determinant lies in the open left half-plane. Passing supplies finite Hurwitz stability, a factor-division invariant broader than rational linear splitting, but not an all-order stability proof or a Jacobi-sign induction.","records":records,"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_source_determinant_hurwitz_stability.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
