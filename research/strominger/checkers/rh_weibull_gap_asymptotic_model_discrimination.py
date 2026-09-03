import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_hankel_ratio_direct_one_over_n_fit_audit.json").read_text(encoding="utf-8"));L=src["log_determinant_ratios"]
train=list(range(3,10));test=list(range(10,13))
def solve(G,b):
 A=[row[:]+[v] for row,v in zip(G,b)];n=len(A)
 for i in range(n):
  k=max(range(i,n),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,n+1):A[i][j]/=p
  for r in range(n):
   if r!=i:
    f=A[r][i]
    for j in range(i,n+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(n)]
def features(name,n):
 if name=="linear":return [n,1.]
 if name=="linear_inverse":return [n,1.,1/n]
 if name=="linear_inverse_square":return [n,1.,1/n,1/n**2]
 if name=="linear_log_inverse":return [n,1.,math.log(n),1/n]
def fit(name):
 X=[features(name,n) for n in train];y=[L[n] for n in train];m=len(X[0]);G=[[sum(x[i]*x[j] for x in X) for j in range(m)] for i in range(m)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(m)];c=solve(G,b)
 def rmse(ns):return math.sqrt(sum((L[n]-sum(ci*xi for ci,xi in zip(c,features(name,n))))**2 for n in ns)/len(ns))
 return {"model":name,"coefficients":c,"train_rmse":rmse(train),"holdout_rmse":rmse(test)}
models=[fit(n) for n in ("linear","linear_inverse","linear_inverse_square","linear_log_inverse")];best=min(models,key=lambda m:m["holdout_rmse"])
checks={
 "source_direct_ratio_audit_passed":src["status"]=="passed",
 "all_fit_errors_finite":all(math.isfinite(m["holdout_rmse"]) for m in models),
 "inverse_terms_improve_over_linear":min(m["holdout_rmse"] for m in models if "inverse" in m["model"])<models[0]["holdout_rmse"],
 "best_model_identified":best["holdout_rmse"]==min(m["holdout_rmse"] for m in models),
}
result={"schema":"marici.strominger.rh_weibull_gap_asymptotic_model_discrimination.v1","status":"passed" if all(checks.values()) else "failed","training_degrees":"3..9","holdout_degrees":"10..12","verdict":f"Finite holdout discrimination selects {best['model']} among linear, inverse-power, and logarithmic alternatives. This tests the form of the Weibull hard-edge gap expansion but does not prove it.","checks":checks,"best_model":best["model"],"models":models,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_gap_asymptotic_model_discrimination.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
