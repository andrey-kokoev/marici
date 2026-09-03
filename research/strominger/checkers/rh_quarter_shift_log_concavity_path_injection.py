import json
from fractions import Fraction as F
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4));states=("LL","LR","RL","RR");rows=[]
for a in range(4):
 for t in range(4):
  for s in ss:
   u=s+a+t
   outer={"LL":u*(u+2),"LR":u,"RL":u+2,"RR":F(1)}
   middle={"LL":(u+1)**2,"LR":u+1,"RL":u+1,"RR":F(1)}
   for state in states:rows.append({"shift":a,"layer":t,"s":str(s),"state":state,"middle_minus_outer":str(middle[state]-outer[state]),"nonnegative":middle[state]>=outer[state]})
negative=[r for r in rows if not r["nonnegative"]];zero=[r for r in rows if r["middle_minus_outer"]=="0"]
checks={"naive_state_preserving_domination_fails":bool(negative),"right_level_left_rise_is_counterexample":all(any(r["state"]=="RL" and r["shift"]==a and r["layer"]==t and r["s"]==str(s) and r["middle_minus_outer"]=="-1" for r in negative) for a in range(4) for t in range(4) for s in ss),"both_level_state_strictly_improves":all(r["nonnegative"] and r["middle_minus_outer"]=="1" for r in rows if r["state"]=="LL"),"both_rise_state_preserves_weight":all(r["middle_minus_outer"]=="0" for r in rows if r["state"]=="RR"),"all_256_local_cases_tested":len(rows)==256}
result={"schema":"marici.strominger.rh_quarter_shift_log_concavity_path_injection.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The naive state-preserving injection from networks at shifts a and a+2 to two networks at a+1 is not weight-dominating. At every tested layer, the outer RL state has weight u+2 while the middle state has u+1, giving residual -1. A valid proof needs a global path switch that changes mixed edge states, not pointwise layer matching.","first_negative":negative[0] if negative else None,"negative_case_count":len(negative),"zero_case_count":len(zero),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_shift_log_concavity_path_injection.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
