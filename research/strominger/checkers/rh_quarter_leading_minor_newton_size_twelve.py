import json
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def entry(i,j,a):return reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1))
def det(m):
 m=[r[:] for r in m];n=len(m);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if m[i][k]),None)
  if p is None:return F(0)
  m[k],m[p]=m[p],m[k]
  if p!=k:out=-out
  z=m[k][k];out*=z
  for j in range(k,n):m[k][j]/=z
  for i in range(k+1,n):
   z=m[i][k]
   for j in range(k,n):m[i][j]-=z*m[k][j]
 return out
def leading(a,k):return det([[entry(i,j,a) for j in range(k)] for i in range(k)])
records=[]
for k in range(9,13):
 degree=3*k*(k-1)//2;cur=[leading(a,k) for a in range(degree+2)];coeff=[]
 while cur:
  coeff.append(cur[0]);cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
 records.append({"size":k,"sharp_degree":degree,"coefficient_count":degree+1,"all_coefficients_strictly_positive":all(x>0 for x in coeff[:degree+1]),"degree_tail_zero":coeff[degree+1]==0,"leading_coefficient_positive":coeff[degree]>0})
checks={"all_newton_coefficients_positive_sizes_nine_to_twelve":all(r["all_coefficients_strictly_positive"] for r in records),"sharp_degree_tails_zero":all(r["degree_tail_zero"] for r in records),"leading_coefficients_positive":all(r["leading_coefficient_positive"] for r in records),"tested_exactly_sizes_nine_to_twelve":[r["size"] for r in records]==[9,10,11,12],"deliberate_negative_orientation_rejected":det([[entry(i,j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_leading_minor_newton_size_twelve.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Using the proved sharp degree, every Newton coefficient of the leading-minor shift polynomials at sizes nine through twelve is tested exactly. Passing extends all-start solid-minor positivity through size twelve via the positive-weight reduction, but is not an all-size coefficient proof.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_leading_minor_newton_size_twelve.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
