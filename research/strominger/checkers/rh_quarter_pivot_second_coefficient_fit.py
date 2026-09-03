import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_pivot_curvature_grid.json").read_text(encoding="utf-8"));rows=src["late_rows"]
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
X=[[1,1/r["m"],1/r["m"]**2] for r in rows];y=[r["m2_residual_from_two"] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];fit=solve(G,b);target=-7/4
checks={"source_grid_passed":src["status"]=="passed","fit_finite":all(math.isfinite(v) for v in fit),"fit_rejects_minus_seven_quarters":abs(fit[0]-target)>.03,"raw_residuals_move_toward_target":abs(rows[-1]["m2_residual_from_two"]-target)<abs(rows[0]["m2_residual_from_two"]-target)}
result={"schema":"marici.strominger.rh_quarter_pivot_second_coefficient_fit.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Quadratic inverse-degree extrapolation gives the second pivot-curvature coefficient {fit[0]:.8g}, which rejects the candidate -7/4 under this correction model. For second coefficient beta, log c_m=2/m+(beta-2)/m^2+O(m^-3). This is finite extrapolation, not a recurrence derivation.","checks":checks,"fit":{"limit":fit[0],"inverse_m":fit[1],"inverse_m2":fit[2]},"target":target,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_pivot_second_coefficient_fit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
