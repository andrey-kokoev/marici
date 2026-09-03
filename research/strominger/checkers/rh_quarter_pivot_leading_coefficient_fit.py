import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_pivot_curvature_grid.json").read_text(encoding="utf-8"));allrows=src["late_rows"]
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
 rows=[r for r in allrows if r["m"]>=lo];X=[[1,1/r["m"],1/r["m"]**2,1/r["m"]**3] for r in rows];y=[r["m_times_c_minus_one"] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(4)];v=solve(G,b);return {"lo":lo,"hi":rows[-1]["m"],"limit":v[0],"inverse_m":v[1],"inverse_m2":v[2],"inverse_m3":v[3],"count":len(rows)}
fits=[fit(lo) for lo in (10,14,18,22)];limits=[r["limit"] for r in fits]
checks={"source_grid_passed":src["status"]=="passed","all_limits_finite":all(math.isfinite(x) for x in limits),"all_limits_within_five_e_minus_five_of_two":max(abs(x-2) for x in limits)<5e-5,"nested_limits_stable":max(limits)-min(limits)<5e-5,"deliberate_limit_one_rejected":min(abs(x-1) for x in limits)>.9}
result={"schema":"marici.strominger.rh_quarter_pivot_leading_coefficient_fit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact degree-35 pivot curvatures fitted on four nested tails select lim m(c_m-1)=2. Stability strengthens finite recognition but does not prove the local O(m^-2) expansion.","checks":checks,"fits":fits,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_pivot_leading_coefficient_fit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
