import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_weibull_critical_defect_slack_grid.json").read_text(encoding="utf-8"));raw=src["late_rows"]
kappas=tuple(i/100 for i in range(101));models=[]
for k in kappas:
 rows=[]
 for q in raw:
  n=q["n"];r=(1/(n+1)-q["critical"])*(n-1);crit=1/(n+1+k)-r/(n-1+k);slack=crit-q["epsilon"]
  rows.append({"n":n,"slack":slack,"n4_slack":n**4*slack})
 models.append({"kappa":k,"all_positive":all(x["slack"]>0 for x in rows),"minimum_slack":min(x["slack"] for x in rows),"rows":rows})
valid=[m for m in models if m["all_positive"]];best=max(models,key=lambda m:m["minimum_slack"])
checks={"source_audit_passed":src["status"]=="passed","unshifted_fails":not models[0]["all_positive"],"no_constant_shift_succeeds":not valid,"best_shift_still_negative":best["minimum_slack"]<0,"finite_outputs":all(math.isfinite(x["slack"]) for m in models for x in m["rows"])}
result={"schema":"marici.strominger.rh_weibull_shifted_inverse_barrier_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"A maximin scan over constant shifts kappa in [0,1] finds best kappa={best['kappa']}, but its minimum signed slack remains {best['minimum_slack']:.3e}. No constant shifted inverse profile propagates across degrees 8..16; a higher-order or accumulated-margin comparison is required.","checks":checks,"best_model":{"kappa":best["kappa"],"minimum_slack":best["minimum_slack"],"rows":best["rows"]},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_shifted_inverse_barrier_grid.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
