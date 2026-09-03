import json,itertools
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
def minor(a,r,c,k):return det([[entry(r+i,c+j,a) for j in range(k)] for i in range(k)])
records=[];failures=[]
for k in range(1,5):
 for r in range(4):
  for c in range(4):
   degree=4*k*c+2*k*(k-1);vals=[minor(a,r,c,k) for a in range(degree+2)];coeff=[];cur=vals[:]
   while cur:
    coeff.append(cur[0]);cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
   within=coeff[:degree+1];tail=coeff[degree+1]
   ok=within[0]>0 and all(x>=0 for x in within) and tail==0
   rec={"size":k,"row_start":r,"column_start":c,"degree_bound":degree,"newton_coefficient_count":len(within),"all_nonnegative":all(x>=0 for x in within),"constant_positive":within[0]>0,"degree_tail_zero":tail==0}
   records.append(rec)
   if not ok:failures.append(rec)
checks={"all_solid_minors_have_nonnegative_newton_certificates":not failures,"tested_sizes_one_to_four":{r["size"] for r in records}=={1,2,3,4},"tested_64_minor_families":len(records)==64,"all_degree_tails_zero":all(r["degree_tail_zero"] for r in records),"all_constants_positive":all(r["constant_positive"] for r in records),"deliberate_negative_orientation_not_certified":det([[entry(i,j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_solid_minor_newton_certificate.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact forward differences test nonnegative Newton-series certificates for 64 contiguous-minor polynomial families of sizes one through four. Such a certificate proves positivity for every integer shift a>=0 within the tested sizes; failure is retained without refitting.","records":records,"failures":failures,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_solid_minor_newton_certificate.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
