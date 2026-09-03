import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_weibull_critical_defect_slack_grid.json").read_text(encoding="utf-8"));rows=[]
for q in src["late_rows"]:
 n=q["n"];r=(1/(n+1)-q["critical"])*(n-1);r3eff=n**3*(r-1+4/n-10/n**2);e4eff=n**4*(q["epsilon"]-2/n**2+6/n**3)
 rows.append({"n":n,"r3_effective":r3eff,"e4_effective":e4eff,"sum_effective":r3eff+e4eff})
def solve(A,b):
 A=[x[:]+[y] for x,y in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda j:abs(A[j][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for h in range(m):
   if h!=i:
    f=A[h][i]
    for j in range(i,m+1):A[h][j]-=f*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(key):
 X=[[1,1/r["n"],1/r["n"]**2,1/r["n"]**3] for r in rows];y=[r[key] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(4)];return solve(G,b)
fr=fit("r3_effective");fe=fit("e4_effective");fs=fit("sum_effective")
target_r=-163/8;target_e=103/8;target_s=-15/2
checks={"source_audit_passed":src["status"]=="passed","r3_fit_near_minus_163_over_8":abs(fr[0]-target_r)<.03,"e4_fit_near_103_over_8":abs(fe[0]-target_e)<.03,"sum_fit_near_minus_15_over_2":abs(fs[0]-target_s)<.04,"finite_fits":all(math.isfinite(x) for x in fr+fe+fs)}
result={"schema":"marici.strominger.rh_weibull_fourth_order_coefficient_fit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Cubic inverse-degree extrapolation of the precision grid tests rational candidates r3=-163/8, e4=103/8, and r3+e4=-15/2. Agreement is finite evidence; exact values require Jacobi asymptotics.","checks":checks,"fits":{"r3":fr,"e4":fe,"sum":fs},"targets":{"r3":target_r,"e4":target_e,"sum":target_s},"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_fourth_order_coefficient_fit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
