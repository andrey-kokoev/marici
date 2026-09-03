import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=32
def det(a):
 a=[r[:] for r in a];last=1;n=len(a)
 for k in range(n-1):
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])//last
  last=q
 return a[-1][-1]
def seq(alpha):
 off=int(2*(alpha+1)-1);ds=[1]+[det([[math.factorial(2*(i+j)+off) for j in range(n)] for i in range(n)]) for n in range(1,N+2)];v={}
 with localcontext() as c:
  c.prec=100
  for n in range(1,N+1):v[n]=(D(ds[n+1])*D(ds[n-1])/D(ds[n])**2).ln()
 return v
z=seq(0);a=seq(1);target=5/9;rows=[]
for n in range(14,N+1):
 d2=(n+1)*math.log(n+1)+(n-1)*math.log(n-1)-2*n*math.log(n)
 c=-n*n*(float(a[n]-z[n])-2*d2);rows.append({"n":n,"coefficient":c,"n_error_from_5_9":n*(c-target)})
late=[r for r in rows if r["n"]>=25]
checks={"degree_32_reached":rows[-1]["n"]==32,"coefficient_decreases":all(rows[i+1]["coefficient"]<rows[i]["coefficient"] for i in range(len(rows)-1)),"late_values_near_5_9":max(abs(r["coefficient"]-target) for r in late)<.01,"n_error_stabilizes":max(r["n_error_from_5_9"] for r in late)-min(r["n_error_from_5_9"] for r in late)<.01}
result={"schema":"marici.strominger.rh_half_weibull_log_limit_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact half-Weibull determinants through degree 32 support c(1/2)=5/9 with an O(n^-1) finite correction. This identifies a sharper candidate but remains a finite asymptotic diagnostic.","checks":checks,"candidate":"c(1/2)=5/9","late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_half_weibull_log_limit_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
