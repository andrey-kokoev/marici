import json
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
def H(a,r,k):return F(1) if k==0 else det([[m(r+i+j,a) for j in range(k)] for i in range(k)])
records=[]
for a in range(5):
 for r in range(9):
  for k in range(2,7):
   lhs=H(a,r,k)*H(a,r+2,k-2);gap=H(a,r,k-1)*H(a,r+2,k-1)-H(a,r+1,k-1)**2
   records.append({"shift":a,"moment_start":r,"size":k,"condensation_exact":lhs==gap,"turan_gap_positive":gap>0,"all_factors_positive":all(H(a,r+s,j)>0 for s in range(3) for j in range(k+1))})
checks={"all_desnanot_jacobi_identities_exact":all(x["condensation_exact"] for x in records),"all_tested_turan_gaps_positive":all(x["turan_gap_positive"] for x in records),"all_bounded_factors_positive":all(x["all_factors_positive"] for x in records),"tested_225_recurrences":len(records)==225}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_hankel_condensation_recurrence.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Contiguous Hankel minors satisfy exact Desnanot-Jacobi condensation, and every bounded Turan gap is positive. The recurrence does not by itself close a positivity induction: its required strict Turan inequality is algebraically equivalent to positivity of the next Hankel determinant times an already positive lower determinant.","record_count":len(records),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_hankel_condensation_recurrence.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
