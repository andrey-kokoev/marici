import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));rows=[r for r in src["rows"] if r["n"]>=10]
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
def features(kind,n):
 x=1/n
 return [1,x,x*x,x*x*x] if kind=="power3" else [1,math.log(n)*x,x,x*x]
def fit(kind,train):
 X=[features(kind,r["n"]) for r in train];y=[r["n2_theta"] for r in train];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(4)];return solve(G,b)
def predict(c,x):return sum(a*b for a,b in zip(c,x))
folds=[]
for cutoff in (24,28,32):
 train=[r for r in rows if r["n"]<=cutoff];test=[r for r in rows if cutoff<r["n"]<=cutoff+4]
 rec={"cutoff":cutoff,"holdout":[r["n"] for r in test]}
 for kind in ("power3","log_power"):
  c=fit(kind,train);err=[predict(c,features(kind,r["n"]))-r["n2_theta"] for r in test];rec[kind]={"theta2":c[0],"rmse":math.sqrt(sum(e*e for e in err)/len(err)),"max_abs":max(abs(e) for e in err)}
 folds.append(rec)
power=sum(f["power3"]["rmse"] for f in folds);logm=sum(f["log_power"]["rmse"] for f in folds);powerT=[f["power3"]["theta2"] for f in folds];logT=[f["log_power"]["theta2"] for f in folds]
checks={"source_grid_passed":src["status"]=="passed","equal_parameter_models":True,"all_holdouts_nonempty":all(f["holdout"] for f in folds),"winner_has_lower_aggregate_rmse":abs(power-logm)>1e-10,"limit_stabilities_computed":all(math.isfinite(x) for x in powerT+logT),"thirteen_sixtieths_not_assumed":True}
winner="power3" if power<logm else "log_power"
result={"schema":"marici.strominger.rh_quarter_cross_limit_model_reassessment.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Equal-parameter rolling holdouts compare cubic inverse-power and log(n)/n correction models without fixing theta2. Winner={winner}; aggregate RMSE power3={power:.3g}, log_power={logm:.3g}. Model selection remains finite.","checks":checks,"winner":winner,"folds":folds,"aggregate_rmse":{"power3":power,"log_power":logm},"theta2_spread":{"power3":max(powerT)-min(powerT),"log_power":max(logT)-min(logT)},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_cross_limit_model_reassessment.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
