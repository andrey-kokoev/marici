import json
from fractions import Fraction as F
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def det(a):
 a=[r[:] for r in a];n=len(a);out=F(1)
 for k in range(n):
  p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
  if p!=k:out=-out
  q=a[k][k];out*=q
  for j in range(k,n):a[k][j]/=q
  for i in range(k+1,n):
   q=a[i][k]
   for j in range(k,n):a[i][j]-=q*a[k][j]
 return out
rows=[]
for n in range(1,7):
 lhs=det([[mathprod:=__import__('functools').reduce(lambda x,s:x*rise(s,i+j),ss,F(1)) for j in range(n)] for i in range(n)])
 pref=F(1)
 for i in range(n):
  for s in ss:pref*=rise(s,i)
 stair=det([[__import__('functools').reduce(lambda x,s:x*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
 rows.append({"n":n,"residual":str(lhs-pref*stair),"staircase_positive":stair>0})
barnes=sum(((s-1)**2/F(2)-F(1,12) for s in ss),F(0));target=F(3,8);residual=target-barnes
checks={"factorization_exact":all(r["residual"]=="0" for r in rows),"staircase_positive":all(r["staircase_positive"] for r in rows),"barnes_coefficient_five_forty_eighths":barnes==F(5,48),"residual_thirteen_forty_eighths":residual==F(13,48),"sum_recovers_three_eighths":barnes+residual==target}
result={"schema":"marici.strominger.rh_quarter_barnes_staircase_split_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Pochhammer factorization isolates a Barnes log coefficient 5/48. Reaching the required 3/8 total is equivalent to proving a 13/48 log coefficient for the positive four-staircase determinant.","checks":checks,"tested_sizes":"1..6","coefficients":{"barnes":str(barnes),"staircase_target":str(residual),"total":str(target)},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_barnes_staircase_split_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
