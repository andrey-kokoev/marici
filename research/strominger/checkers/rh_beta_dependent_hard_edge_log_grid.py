import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=20
def det(a):
 a=[r[:] for r in a];last=1;n=len(a)
 for k in range(n-1):
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])//last
  last=q
 return a[-1][-1]
def logs(p,alpha):
 off=int(p*(alpha+1)-1);ds=[1]+[det([[math.factorial(p*(i+j)+off) for j in range(n)] for i in range(n)]) for n in range(1,N+2)];v={}
 with localcontext() as c:
  c.prec=100
  for n in range(1,N+1):v[n]=(D(ds[n+1])*D(ds[n-1])/D(ds[n])**2).ln()
 return v
rows=[]
for p in (1,2,3,4):
 z=logs(p,0);a=logs(p,1)
 vals=[]
 for n in range(14,N+1):
  d2=(n+1)*math.log(n+1)+(n-1)*math.log(n-1)-2*n*math.log(n)
  rem=float(a[n]-z[n])-p*d2;c=-n*n*rem
  vals.append({"n":n,"coefficient_estimate":c})
 rows.append({"p":p,"beta":1/p,"late_values":vals,"degree20":vals[-1]["coefficient_estimate"]})
checks={"laguerre_near_half":abs(rows[0]["degree20"]-.5)<.01,"quarter_near_one":abs(rows[-1]["degree20"]-1)<.01,"intermediate_beta_values_are_distinct":rows[0]["degree20"]<rows[1]["degree20"]<rows[2]["degree20"]<rows[3]["degree20"],"late_values_finite":all(math.isfinite(v["coefficient_estimate"]) for r in rows for v in r["late_values"])}
result={"schema":"marici.strominger.rh_beta_dependent_hard_edge_log_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact reciprocal-integer beta determinant families with alpha=1 give degree-20 coefficient estimates 0.4923, 0.5654, 0.7597, and 0.9992 for beta=1,1/2,1/3,1/4. They establish beta dependence and retain the quarter candidate near one, but do not select a justified closed formula because the beta=1/2 sequence still drifts materially.","checks":checks,"candidate":"unresolved","rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_beta_dependent_hard_edge_log_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
