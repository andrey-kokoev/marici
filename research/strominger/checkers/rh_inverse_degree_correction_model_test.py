import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_diagonal_truncation_exponent_extended_grid_audit.json").read_text(encoding="utf-8"))
rows=[r for r in src["rows"] if r["n"]>=4]; train=[r for r in rows if r["n"]<=10]; test=[r for r in rows if r["n"]>10]
def solve(A,b):
 A=[list(map(float,row))+[float(v)] for row,v in zip(A,b)]; n=len(A)
 for i in range(n):
  k=max(range(i,n),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,n+1):A[i][j]/=p
  for r in range(n):
   if r!=i:
    f=A[r][i]
    for j in range(i,n+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(n)]
def linfit(powers,data):
 X=[[1.]+[r["n"]**(-p) for p in powers] for r in data]; y=[r["relative_b"]*r["n"]**3 for r in data]
 G=[[sum(x[i]*x[j] for x in X) for j in range(len(X[0]))] for i in range(len(X[0]))];h=[sum(x[i]*v for x,v in zip(X,y)) for i in range(len(X[0]))]
 return solve(G,h)
def pred(coef,powers,n):return coef[0]+sum(c*n**(-p) for c,p in zip(coef[1:],powers))
def rmse(coef,powers,data):return math.sqrt(sum((r["relative_b"]*r["n"]**3-pred(coef,powers,r["n"]))**2 for r in data)/len(data))
models=[]
for name,powers in (("inverse_degree",[1.]),("inverse_degree_plus_square",[1.,2.])):
 c=linfit(powers,train);models.append({"model":name,"powers":powers,"coefficients":c,"train_rmse":rmse(c,powers,train),"holdout_rmse":rmse(c,powers,test)})
best=None
for k in range(20,301):
 d=k/200; c=linfit([d],train); score=rmse(c,[d],train)
 if best is None or score<best[0]:best=(score,d,c)
models.append({"model":"free_exponent","powers":[best[1]],"coefficients":best[2],"train_rmse":best[0],"holdout_rmse":rmse(best[2],[best[1]],test)})
by={m["model"]:m for m in models}
checks={
 "source_grid_passed":src["status"]=="passed",
 "fixed_inverse_degree_holdout_below_one_percent_of_limit":by["inverse_degree"]["holdout_rmse"]<1e-3,
 "two_correction_improves_holdout":by["inverse_degree_plus_square"]["holdout_rmse"]<by["inverse_degree"]["holdout_rmse"],
 "free_exponent_does_not_beat_two_correction_holdout":by["free_exponent"]["holdout_rmse"]>by["inverse_degree_plus_square"]["holdout_rmse"],
}
result={"schema":"marici.strominger.rh_inverse_degree_correction_model_test.v1","status":"passed" if all(checks.values()) else "failed","training_degrees":"4..10","holdout_degrees":"11..12","verdict":"A fixed inverse-degree correction predicts held-out degrees, and adding an inverse-square term improves holdout error relative to a free single exponent. This favors an ordinary 1/n expansion over selecting a fractional correction exponent, but the two-point holdout is not an asymptotic theorem.","checks":checks,"models":models,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_inverse_degree_correction_model_test.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
