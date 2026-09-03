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
for k in range(1,9):
 degree=2*k*(k-1);cur=[leading(a,k) for a in range(degree+2)];coeff=[]
 while cur:
  coeff.append(cur[0]);cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
 within=coeff[:degree+1];records.append({"size":k,"degree_bound":degree,"coefficient_count":len(within),"constant_positive":within[0]>0,"all_coefficients_nonnegative":all(x>=0 for x in within),"degree_tail_zero":coeff[degree+1]==0,"strictly_positive_coefficient_count":sum(x>0 for x in within)})
checks={"all_leading_families_certified":all(r["constant_positive"] and r["all_coefficients_nonnegative"] and r["degree_tail_zero"] for r in records),"tested_sizes_one_through_eight":[r["size"] for r in records]==list(range(1,9)),"degree_bounds_verified":all(r["degree_tail_zero"] for r in records),"each_family_has_positive_coefficient":all(r["strictly_positive_coefficient_count"]>0 for r in records),"deliberate_negative_orientation_rejected":det([[entry(i,j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_leading_minor_newton_size_eight.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Newton coefficients test the reduced leading-minor families through size eight. Passing, combined with the positive-weight shift reduction, proves all solid minors through size eight positive for every nonnegative integer start and shift.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_leading_minor_newton_size_eight.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
