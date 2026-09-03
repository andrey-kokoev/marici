import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_weibull_critical_defect_slack_grid.json").read_text(encoding="utf-8"));raw=src["late_rows"]
poly=json.loads((base/"results"/"rh_weibull_polynomial_branch_separation_grid.json").read_text(encoding="utf-8"));pv={r["n"]:r["abs_P_at_zero"] for r in poly["late_rows"]};actual_rho9=pv[9]/pv[8]
def profile(n,k,c):return (1+c/(n*n))/(n+k)
models=[]
for ik in range(31,72,2):
 k=ik/100
 for ic in range(-100,101,2):
  c=ic/20;rows=[];valid=True
  for q in raw:
   n=q["n"];r=(1/(n+1)-q["critical"])*(n-1);vm=profile(n-1,k,c);v=profile(n,k,c);vp=profile(n+1,k,c)
   if min(vm,v,vp)<=0:valid=False;break
   crit=1+r-vp/v-r*vm/v;slack=crit-q["epsilon"];rows.append({"n":n,"slack":slack,"n4_slack":n**4*slack})
  if valid:
   initial_margin=actual_rho9-profile(9,k,c)/profile(8,k,c);models.append({"kappa":k,"c":c,"minimum_slack":min(x["slack"] for x in rows if x["n"]>=9),"all_positive":all(x["slack"]>0 for x in rows if x["n"]>=9),"initial_margin_at_9":initial_margin,"rows":rows})
best=max(models,key=lambda m:m["minimum_slack"]);valid=[m for m in models if m["all_positive"]];admitted=[m for m in valid if m["initial_margin_at_9"]>=0]
chosen=max(admitted,key=lambda m:m["minimum_slack"]) if admitted else None
checks={"source_audit_passed":src["status"]=="passed","positive_slack_profiles_found":bool(valid),"profile_meets_initial_and_slack_gates":chosen is not None,"chosen_initial_margin_nonnegative":chosen is not None and chosen["initial_margin_at_9"]>=0,"finite_outputs":all(math.isfinite(m["minimum_slack"]) for m in models)}
result={"schema":"marici.strominger.rh_weibull_corrected_inverse_barrier_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"A corrected inverse profile meets both the positive defect-slack and n=9 initialization gates at kappa={chosen['kappa']}, c={chosen['c']}. Its minimum slack is {chosen['minimum_slack']:.3e} and initial ratio margin {chosen['initial_margin_at_9']:.3e}. This remains a finite fitted barrier, not an eventual theorem." if chosen else "No corrected profile meets both gates.","checks":checks,"chosen_model":chosen,"positive_slack_model_count":len(valid),"admitted_model_count":len(admitted),"tested_model_count":len(models),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_weibull_corrected_inverse_barrier_grid.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
