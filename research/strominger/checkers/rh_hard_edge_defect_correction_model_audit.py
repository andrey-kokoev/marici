import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_hard_edge_defect_extended_grid_audit.json").read_text(encoding="utf-8"));data=[r for r in src["rows"] if r["n"]>=6];train=[r for r in data if r["n"]<=13];test=[r for r in data if r["n"]>=14]
def fit_delta(delta,rows):
 xs=[r["n"]**(-delta) for r in rows];ys=[2-r["n2_defect"] for r in rows];c=sum(x*y for x,y in zip(xs,ys))/sum(x*x for x in xs)
 return c,math.sqrt(sum((y-c*x)**2 for x,y in zip(xs,ys))/len(xs))
def score(delta):
 c,tr=fit_delta(delta,train);te=math.sqrt(sum(((2-r["n2_defect"])-c*r["n"]**(-delta))**2 for r in test)/len(test));return c,tr,te
models=[]
for name,d in (("square_root",.5),("two_thirds",2/3),("three_quarters",.75),("inverse",1.)):
 c,tr,te=score(d);models.append({"model":name,"delta":d,"c":c,"train_rmse":tr,"holdout_rmse":te})
best=None
for k in range(20,301):
 d=k/200;c,tr,te=score(d)
 if best is None or tr<best[0]:best=(tr,d,c,te)
models.append({"model":"free_power","delta":best[1],"c":best[2],"train_rmse":best[0],"holdout_rmse":best[3]})
winner=min(models,key=lambda m:m["holdout_rmse"])
checks={
 "source_grid_passed":src["status"]=="passed",
 "all_remainders_positive":all(2-r["n2_defect"]>0 for r in data),
 "all_models_finite":all(math.isfinite(m["holdout_rmse"]) for m in models),
 "winner_identified":winner["holdout_rmse"]==min(m["holdout_rmse"] for m in models),
}
result={"schema":"marici.strominger.rh_hard_edge_defect_correction_model_audit.v1","status":"passed" if all(checks.values()) else "failed","training_degrees":"6..13","holdout_degrees":"14..16","verdict":f"Finite holdout comparison selects {winner['model']} with correction exponent {winner['delta']:.4g} for 2-n^2 epsilon_n. This discriminates finite correction models but does not prove the limit two or its remainder exponent.","checks":checks,"winner":winner["model"],"models":models,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_hard_edge_defect_correction_model_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
