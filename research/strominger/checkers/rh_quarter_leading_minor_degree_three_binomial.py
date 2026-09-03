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
 predicted=3*k*(k-1)//2;loose=2*k*(k-1);cur=[leading(a,k) for a in range(loose+2)];coeff=[]
 while cur:
  coeff.append(cur[0]);cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
 actual=max(i for i,x in enumerate(coeff) if x);records.append({"size":k,"predicted_degree":predicted,"actual_degree":actual,"leading_newton_coefficient_positive":coeff[predicted]>0,"all_coefficients_through_degree_positive":all(x>0 for x in coeff[:predicted+1]),"all_coefficients_above_degree_zero":all(x==0 for x in coeff[predicted+1:])})
checks={"degree_equals_three_binomial_for_sizes_one_to_eight":all(r["actual_degree"]==r["predicted_degree"] for r in records),"leading_coefficients_positive":all(r["leading_newton_coefficient_positive"] for r in records),"no_internal_newton_zeros":all(r["all_coefficients_through_degree_positive"] for r in records),"all_loose_bound_tails_zero":all(r["all_coefficients_above_degree_zero"] for r in records),"deliberate_degree_four_binomial_rejected":all(r["actual_degree"]!=2*r["size"]*(r["size"]-1) for r in records if r["size"]>1)}
result={"schema":"marici.strominger.rh_quarter_leading_minor_degree_three_binomial.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The top alternant has exponents 0,4,...,4(k-1); Vandermonde divisibility removes binomial(k,2) degrees, leaving exact shift degree 3 binomial(k,2) with positive leading coefficient. Exact Newton data through size eight verify the degree and have no internal coefficient zeros.","analytic_degree":"sum_j 4j - binomial(k,2) = 3 binomial(k,2)","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_leading_minor_degree_three_binomial.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
