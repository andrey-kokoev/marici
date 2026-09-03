import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"))
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
def fit(lo,order):
 rows=[r for r in src["rows"] if r["n"]>=lo];X=[[r["n"]**(-j) for j in range(order+1)] for r in rows];y=[r["n2_theta"] for r in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(order+1)] for i in range(order+1)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(order+1)];c=solve(G,b);return {"lo":lo,"hi":rows[-1]["n"],"order":order,"theta2":c[0],"coefficients":c[1:],"count":len(rows)}
fits=[fit(lo,o) for o in (3,4) for lo in (10,16,22,28)];p3=[r["theta2"] for r in fits if r["order"]==3];p4=[r["theta2"] for r in fits if r["order"]==4];allv=p3+p4;candidate=13/60
checks={"source_grid_passed":src["status"]=="passed","all_fits_finite":all(math.isfinite(x) for x in allv),"cubic_tail_stable":max(p3)-min(p3)<2e-6,"quartic_tail_stable":max(p4)-min(p4)<2e-7,"orders_agree":abs(p3[-1]-p4[-1])<2e-7,"all_separated_from_thirteen_sixtieths":min(abs(x-candidate) for x in allv)>3e-5,"deliberate_one_fifth_rejected":min(abs(x-.2) for x in allv)>.01}
result={"schema":"marici.strominger.rh_quarter_cross_limit_power_stabilization.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Degree-{fits[0]['hi']} cubic and quartic inverse-power fits test stabilization of theta2 without exact-value recognition.","checks":checks,"fits":fits,"interval":[min(allv),max(allv)],"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_cross_limit_power_stabilization.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
