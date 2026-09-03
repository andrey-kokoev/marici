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
def S(n,a,b):return F(1) if n==0 else det([[rise(a+i,j)*rise(b+i,j) for j in range(n)] for i in range(n)])
a=F(1);b=F(3,2);rows=[]
for n in range(2,15):
 first=(a+n-1)*(b+n-1)*S(n-1,a,b)*S(n-1,a+2,b+2)
 cross=a*b*S(n-1,a+1,b+1)**2;theta=cross/first
 rows.append({"n":n,"theta":float(theta),"one_minus_theta":float(1-theta),"n_theta":float(n*theta),"identity_residual":str(S(n,a,b)*S(n-2,a+2,b+2)-first+cross)})
late=rows[-5:]
checks={"condensation_identity_exact":all(r["identity_residual"]=="0" for r in rows),"strict_fractional_cancellation":all(0<r["theta"]<1 for r in rows),"theta_decreases":all(rows[i+1]["theta"]<rows[i]["theta"] for i in range(len(rows)-1)),"n_theta_stabilizes":max(r["n_theta"] for r in late)-min(r["n_theta"] for r in late)<.05}
result={"schema":"marici.strominger.rh_half_weibull_condensation_balance_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For source staircase parameters, the condensation cross-minor fraction theta_n is positive, decreasing, and finite data test whether it is O(1/n). The exact recurrence cannot discard it: an O(1/n) fraction contributes at first asymptotic order through log(1-theta_n).","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_half_weibull_condensation_balance_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
