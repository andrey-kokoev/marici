import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
base=Path(__file__).parents[1];cm=json.loads((base/"results"/"rh_quarter_cross_ratio_complete_monotonicity.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def theta(n,a):return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
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
records=[];failures=[]
for a in range(13):
 for start in range(2,9):
  for size in range(1,6):
   H=[[theta(start+i+j,a) for j in range(size)] for i in range(size)];K=[[theta(start+i+j,a)-theta(start+i+j+1,a) for j in range(size)] for i in range(size)];dh,dk=det(H),det(K);rec={"shift":a,"start_degree":start,"size":size,"hankel_positive":dh>0,"one_minus_shifted_hankel_positive":dk>0};records.append(rec)
   if dh<=0 or dk<=0:failures.append(rec)
checks={"complete_monotonicity_source_passed":cm["status"]=="passed","all_hankel_determinants_positive":all(r["hankel_positive"] for r in records),"all_one_minus_shifted_hankel_determinants_positive":all(r["one_minus_shifted_hankel_positive"] for r in records),"tested_455_pairs":len(records)==455,"deliberate_row_reversal_negative":det([[theta(2+i+j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_hankel_moment.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Hankel and one-minus-shifted Hankel determinants test positive Hausdorff-moment conditions for sizes one through five, seven starting degrees, and thirteen shifts. Passing is finite evidence and does not construct a measure.","record_count":len(records),"failures":failures,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_cross_ratio_hankel_moment.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
