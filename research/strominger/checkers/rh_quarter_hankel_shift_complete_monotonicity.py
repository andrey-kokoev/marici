import json,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def m(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def det(A):
 A=[r[:] for r in A];n=len(A);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  A[k],A[p]=A[p],A[k]
  if p!=k:out=-out
  z=A[k][k];out*=z
  for j in range(k,n):A[k][j]/=z
  for i in range(k+1,n):
   z=A[i][k]
   for j in range(k,n):A[i][j]-=z*A[k][j]
 return out
@lru_cache(None)
def H(a,r,k):return det([[m(r+i+j,a) for j in range(k)] for i in range(k)])
def diff(a,r,k,d):return sum(F((-1)**j*math.comb(d,j))*H(a,r+j,k) for j in range(d+1))
records=[];first_failure=None
for a in range(5):
 for k in range(1,6):
  for d in range(7):
   for r in range(11):
    z=diff(a,r,k,d);ok=z>0;records.append({"shift":a,"size":k,"difference_order":d,"moment_start":r,"signed_difference_positive":ok})
    if not ok and first_failure is None:first_failure=records[-1]
checks={"all_signed_hankel_shift_differences_positive":first_failure is None,"tested_orders_zero_through_six":{x["difference_order"] for x in records}==set(range(7)),"tested_1925_cases":len(records)==1925,"ordinary_first_difference_negative":all(H(a,1,k)-H(a,0,k)<0 for a in range(5) for k in range(1,6))}
result={"schema":"marici.strominger.rh_quarter_hankel_shift_complete_monotonicity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For Hankel sizes one through five, shifts zero through four, moment starts zero through ten, and difference orders zero through six, every signed shift difference is strictly positive. This finite exterior-power moment pattern implies more than the tested Turan gaps but is not an all-order induction.","record_count":len(records),"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_hankel_shift_complete_monotonicity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
