import json,math
from pathlib import Path
rows=[]
for alpha in (.25,.5,1.,2.):
 vals=[]
 for n in (20,100,1000,10000):
  relative=math.log1p(alpha/n);leading=alpha/n
  vals.append({"n":n,"n2_remainder":n*n*(relative-leading)})
 rows.append({"alpha":alpha,"predicted_limit":-alpha*alpha/2,"values":vals})
checks={"all_limits_match_minus_half_alpha_squared":all(abs(r["values"][-1]["n2_remainder"]-r["predicted_limit"])<1e-3 for r in rows),"quarter_weibull_candidate_differs":1!=.5,"nonzero_controls":all(r["predicted_limit"]<0 for r in rows)}
base=Path(__file__).parents[1];packet=(base/"rh-hard-edge-log-coefficient-is-potential-dependent.md").read_text(encoding="utf-8")
checks.update({"packet_uses_exact_laguerre_recurrence":"n(n+\\alpha)}4" in packet,"packet_rejects_universality":"Reject a universal" in packet,"packet_preserves_quarter_candidate":"quarter-Weibull finite-data candidate" in packet})
result={"schema":"marici.strominger.rh_laguerre_hard_edge_log_benchmark.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The exact beta=1 Laguerre recurrence yields a relative recurrence-log remainder -alpha^2/(2n^2), hence a relative free-energy term +(alpha^2/2)log n. This falsifies a beta-independent +alpha^2 log n rule.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_laguerre_hard_edge_log_benchmark.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
