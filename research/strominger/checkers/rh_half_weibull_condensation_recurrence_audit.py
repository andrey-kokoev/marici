import json
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
def S(n,a,b):return F(1) if n==0 else det([[rise(a+i,j)*rise(b+i,j) for j in range(n)] for i in range(n)])
rows=[]
for a,b in ((F(1),F(3,2)),(F(2),F(5,2)),(F(3,2),F(7,3))):
 for n in range(2,9):
  lhs=S(n,a,b)*S(n-2,a+2,b+2);rhs=(a+n-1)*(b+n-1)*S(n-1,a,b)*S(n-1,a+2,b+2)-a*b*S(n-1,a+1,b+1)**2
  rows.append({"a":str(a),"b":str(b),"n":n,"residual":str(lhs-rhs)})
checks={"all_exact_residuals_zero":all(r["residual"]=="0" for r in rows),"source_parameters_tested":any(r["a"]=="1" and r["b"]=="3/2" for r in rows),"shifted_parameters_tested":any(r["a"]=="2" and r["b"]=="5/2" for r in rows),"deliberate_off_recurrence_nonzero":S(5,F(1),F(3,2))*S(3,F(3),F(7,2))!=5*F(7,2)*S(4,F(1),F(3,2))*S(4,F(3),F(7,2))}
result={"schema":"marici.strominger.rh_half_weibull_condensation_recurrence_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Desnanot-Jacobi condensation yields an exact parameter-shifted recurrence for S_n(a,b), verified on 21 rational cases with a deliberate malformed-recurrence control. Asymptotic use still requires cancellation control.","checks":checks,"tested_rows":len(rows),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_half_weibull_condensation_recurrence_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
