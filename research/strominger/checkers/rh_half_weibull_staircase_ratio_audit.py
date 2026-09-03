import json,math
from fractions import Fraction as F
from pathlib import Path
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
def S(n,a,b):return det([[rise(a+i,j)*rise(b+i,j) for j in range(n)] for i in range(n)])
rows=[]
for n in range(1,11):
 r=S(n,F(2),F(5,2))/S(n,F(1),F(3,2));rows.append({"n":n,"ratio":str(r),"numerator_bits":r.numerator.bit_length(),"denominator_bits":r.denominator.bit_length()})
# The consecutive ratio isolates a potential product formula.
for i in range(1,len(rows)):
 q=F(rows[i]["ratio"])/F(rows[i-1]["ratio"]);rows[i]["successive_ratio"]=str(q)
checks={"all_ratios_positive":all(F(r["ratio"])>0 for r in rows),"ten_exact_ratios":len(rows)==10,"successive_ratios_recorded":all("successive_ratio" in r for r in rows[1:])}
result={"schema":"marici.strominger.rh_half_weibull_staircase_ratio_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact staircase ratios S_n(2,5/2)/S_n(1,3/2) and their successive quotients are tabulated through n=10 to test product structure. Positivity and arithmetic regularity do not themselves prove a closed product or asymptotic.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_half_weibull_staircase_ratio_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
