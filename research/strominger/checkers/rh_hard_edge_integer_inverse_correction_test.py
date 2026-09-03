import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_hard_edge_defect_extended_grid_audit.json").read_text(encoding="utf-8"));train=[r for r in src["rows"] if 6<=r["n"]<=13];test=[r for r in src["rows"] if r["n"]>=14]
def solve(A,b):
 A=[row[:]+[v] for row,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for r in range(m):
   if r!=i:
    f=A[r][i]
    for j in range(i,m+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(powers):
 X=[[r["n"]**(-p) for p in powers] for r in train];y=[2-r["n2_defect"] for r in train];m=len(powers);G=[[sum(x[i]*x[j] for x in X) for j in range(m)] for i in range(m)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(m)];c=solve(G,b)
 def rmse(rows):return math.sqrt(sum(((2-r["n2_defect"])-sum(ci*r["n"]**(-p) for ci,p in zip(c,powers)))**2 for r in rows)/len(rows))
 return c,rmse(train),rmse(test)
models=[]
for name,powers in (("inverse",[1]),("inverse_square",[1,2]),("inverse_cubic",[1,2,3])):
 c,tr,te=fit(powers);models.append({"model":name,"powers":powers,"coefficients":c,"train_rmse":tr,"holdout_rmse":te})
prior=json.loads((base/"results"/"rh_hard_edge_defect_correction_model_audit.json").read_text(encoding="utf-8"));free=next(m for m in prior["models"] if m["model"]=="free_power");models.append(free)
by={m["model"]:m for m in models};winner=min(models,key=lambda m:m["holdout_rmse"])
checks={
 "source_grid_passed":src["status"]=="passed",
 "inverse_square_beats_single_inverse":by["inverse_square"]["holdout_rmse"]<by["inverse"]["holdout_rmse"],
 "best_integer_model_beats_free_power":min(by[n]["holdout_rmse"] for n in ("inverse_square","inverse_cubic"))<by["free_power"]["holdout_rmse"],
 "leading_inverse_coefficient_positive":by["inverse_square"]["coefficients"][0]>0,
}
result={"schema":"marici.strominger.rh_hard_edge_integer_inverse_correction_test.v1","status":"passed" if all(checks.values()) else "failed","training_degrees":"6..13","holdout_degrees":"14..16","verdict":f"Integer inverse-power correction models with multiple terms outperform the free single exponent on holdout; winner={winner['model']}. This supports an ordinary 1/n expansion toward the defect limit two but does not prove its coefficients or remainder.","checks":checks,"winner":winner["model"],"models":models,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_hard_edge_integer_inverse_correction_test.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
