import json,math
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));rows=src["late_rows"]
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for r in range(m):
   if r!=i:
    q=A[r][i]
    for j in range(i,m+1):A[r][j]-=q*A[i][j]
 return [A[i][-1] for i in range(m)]
X=[[1,1/r["n"],1/r["n"]**2] for r in rows];y=[r["n2_theta"] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];fit=solve(G,b)
candidates={"13/60":13/60,"7/32":7/32,"3/14":3/14,"1/5":1/5};nearest=min(candidates,key=lambda k:abs(candidates[k]-fit[0]))
checks={"source_grid_passed":src["status"]=="passed","fit_finite":all(math.isfinite(v) for v in fit),"nearest_candidate_identified":nearest in candidates,"fit_near_13_over_60":abs(fit[0]-13/60)<.002}
result={"schema":"marici.strominger.rh_quarter_cross_limit_fit.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Quadratic inverse-degree extrapolation of exact n=14..18 cross ratios gives theta2={fit[0]:.8g}; nearest tested rational is {nearest}. This remains finite recognition, not a limit proof.","checks":checks,"fit":{"limit":fit[0],"inverse_n":fit[1],"inverse_n2":fit[2]},"candidates":candidates,"nearest":nearest,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_cross_limit_fit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
