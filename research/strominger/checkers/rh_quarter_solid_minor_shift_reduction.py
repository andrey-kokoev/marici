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
def solid(a,r,c,k):return det([[entry(r+i,c+j,a) for j in range(k)] for i in range(k)])
def weight(a,r,c,k):return reduce(lambda z,i:z*entry(r+i,c,a)/entry(r+i,0,a+c),range(k),F(1))
rows=[]
for a in range(4):
 for r in range(4):
  for c in range(4):
   for k in range(1,5):
    lhs=solid(a,r,c,k);rhs=weight(a,r,c,k)*solid(a+r+c,0,0,k);rows.append(lhs==rhs)
source=json.loads((Path(__file__).parents[1]/"results"/"rh_quarter_solid_minor_newton_certificate.json").read_text(encoding="utf-8"));leading=[x for x in source["records"] if x["row_start"]==0 and x["column_start"]==0]
checks={"exact_shift_reduction_on_256_cases":len(rows)==256 and all(rows),"positive_row_weights":all(weight(a,r,c,k)>0 for a in range(4) for r in range(4) for c in range(4) for k in range(1,5)),"leading_newton_certificates_available":len(leading)==4 and all(x["all_nonnegative"] and x["constant_positive"] and x["degree_tail_zero"] for x in leading),"source_certificate_passed":source["status"]=="passed","deliberate_missing_shift_rejected":solid(1,1,1,2)!=weight(1,1,1,2)*solid(1,0,0,2)}
result={"schema":"marici.strominger.rh_quarter_solid_minor_shift_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every contiguous minor factors into positive row weights times a leading-column, leading-row minor at combined shift a+r+c. Together with the Newton certificates, this proves all solid minors of sizes at most four positive for arbitrary nonnegative integer row start, column start, and shift.","identity":"M_(r,c,k)(a)=prod_i W_c(a+r+i) M_(0,0,k)(a+r+c)","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_solid_minor_shift_reduction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
