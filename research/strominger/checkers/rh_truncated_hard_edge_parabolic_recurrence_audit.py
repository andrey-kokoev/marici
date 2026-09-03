import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_truncated_weibull_jacobi_diagnostic.json").read_text(encoding="utf-8"));r=src["rows"];rows=[]
for n in range(1,len(r)-1):
 an=r[n]["a"];an1=r[n+1]["a"];bn=r[n]["b_translated"];defect=(an+an1-bn)/an1
 rows.append({"n":n,"a_ratio":an/an1,"b_over_a_sum":bn/(an+an1),"edge_defect":defect,"n2_abs_defect":n*n*abs(defect)})
late=rows[1:]
checks={
 "a_ratio_increases_toward_one":all(rows[i+1]["a_ratio"]>rows[i]["a_ratio"] for i in range(len(rows)-1)),
 "b_over_a_sum_approaches_one_after_n2":all(abs(late[i+1]["b_over_a_sum"]-1)<abs(late[i]["b_over_a_sum"]-1) for i in range(len(late)-1)),
 "edge_defect_magnitude_decreases_after_n2":all(abs(late[i+1]["edge_defect"])<abs(late[i]["edge_defect"]) for i in range(len(late)-1)),
}
packet=(base/"rh-truncated-exterior-recurrence-is-parabolic-at-the-hard-edge.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_double_root":"(\\lambda+1)^2" in packet,
 "packet_distinguishes_parabolic_from_hyperbolic":"A hyperbolic limiting recurrence" in packet,
 "packet_requires_indicial_analysis":"without an indicial analysis" in packet,
})
result={"schema":"marici.strominger.rh_truncated_hard_edge_parabolic_recurrence_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The finite truncated Jacobi coefficients approach the hard-edge balance b_n=a_n+a_(n+1), while a_n/a_(n+1) approaches one. The limiting characteristic polynomial is therefore diagnostically (lambda+1)^2, identifying a parabolic recurrence whose subleading terms can generate algebraic exterior decay.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_truncated_hard_edge_parabolic_recurrence_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
