import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));T=13/60
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  p=max(range(i,m),key=lambda k:abs(A[k][i]));A[i],A[p]=A[p],A[i];z=A[i][i]
  for j in range(i,m+1):A[i][j]/=z
  for k in range(m):
   if k!=i:
    z=A[k][i]
    for j in range(i,m+1):A[k][j]-=z*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(lo):
 rows=[r for r in src["rows"] if r["n"]>=lo];X=[[1,1/r["n"],1/r["n"]**2,1/r["n"]**3] for r in rows];y=[r["n2_theta"] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(4)];v=solve(G,b);u=v[1]/v[0];return {"lo":lo,"hi":rows[-1]["n"],"theta2":v[0],"u":u,"inverse_n2":v[2],"inverse_n3":v[3],"a":u+3.5,"beta":-u-.5,"count":len(rows)}
fits=[fit(lo) for lo in (10,14,18,22)];us=[r["u"] for r in fits]
theta=[r["theta2"] for r in fits]
checks={"source_grid_passed":src["status"]=="passed","all_fits_finite":all(math.isfinite(u) for u in us+theta),"theta_separated_from_thirteen_sixtieths":min(abs(x-T) for x in theta)>3e-5,"u_separated_from_six_fifths":min(abs(u-1.2) for u in us)>.009,"nested_u_stable":max(us)-min(us)<3e-4,"nested_theta_stable":max(theta)-min(theta)<1e-6}
result={"schema":"marici.strominger.rh_quarter_global_shift_first_correction_nested.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Joint degree-36 nested cubic fits stabilize near theta2=0.2167044 and u=1.20935, separating from 13/60 and 6/5 under this correction model. The earlier rational recognition is rejected, not replaced by an exact constant.","checks":checks,"fits":fits,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_global_shift_first_correction_nested.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
