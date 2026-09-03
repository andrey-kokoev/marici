import json, math
from pathlib import Path
a=1.;beta=.25
Xs=(1e2,1e4,1e6,1e8,1e10,1e12)
rows=[]
for X in Xs:
 L=X**(1-beta)/(2*a*beta);z=X**(beta/4);phi=2*a*((X+L*z)**beta-X**beta);err=abs(phi-z)
 rows.append({"X":X,"z_star":z,"y_star":L*z,"exponent_error":err,"scaled_error":err*X**(beta/2)})
checks={
 "matching_cut_grows":all(rows[i+1]["z_star"]>rows[i]["z_star"] for i in range(len(rows)-1)),
 "relative_cut_y_over_X_shrinks":all(rows[i+1]["y_star"]/rows[i+1]["X"]<rows[i]["y_star"]/rows[i]["X"] for i in range(len(rows)-1)),
 "exponent_error_decreases":all(rows[i+1]["exponent_error"]<rows[i]["exponent_error"] for i in range(len(rows)-1)),
 "scaled_error_is_bounded":max(r["scaled_error"] for r in rows)<2,
}
base=Path(__file__).parents[1]
packet=(base/"rh-moving-weibull-weight-has-a-growing-laguerre-overlap-window.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_overlap_range":"0<\\theta<\\beta/2" in packet,
 "packet_gives_beta_quarter_original_scale":"X^{13/16}" in packet,
 "packet_does_not_promote_scalar_to_determinant":"not a Hankel-determinant asymptotic" in packet,
})
result={"schema":"marici.strominger.rh_laguerre_weibull_overlap_window_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The cut z_*=X^(beta/4) grows while the Laguerre exponent error decays as O(X^(-beta/2)). It gives a nonempty local-global overlap and retains the far Weibull region. This constructs the scalar matching scale but not a determinant factorization.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_laguerre_weibull_overlap_window_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
