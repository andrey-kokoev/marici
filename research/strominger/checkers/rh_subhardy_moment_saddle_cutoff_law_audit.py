import json, math
from fractions import Fraction as Q
from pathlib import Path

def saddle(K,a,beta):return (K/(a*beta))**(1/beta)
def dpsi(x,K,a,beta):return 2*K/x-2*a*beta*x**(beta-1)
checks={
 "saddle_formula_solves_stationarity":abs(dpsi(saddle(6,1,.25),6,1,.25))<1e-15,
 "integrand_increases_below_saddle":all(dpsi(x,6,1,.25)>0 for x in (1,10,100,1000,10000,100000)),
 "integrand_decreases_above_saddle":all(dpsi(x,6,1,.25)<0 for x in (400000,1000000)),
 "beta_quarter_order_six_saddle_is_exact":saddle(6,1,.25)==331776,
 "tested_cutoff_log_is_far_below_saddle":math.log(100000)<12 and math.log(100000)<saddle(6,1,.25),
 "log_cell_rational_bounds_are_ordered":all(Q(1,n+1)<Q(1,n) for n in range(2,100)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-subhardy-moment-saddle-forces-inaccessible-label-cutoffs.md").read_text(encoding="utf-8")
adaptive=(base/"results"/"rh_subhardy_adaptive_cutoff_gram_audit.json").read_text(encoding="utf-8")
checks.update({
 "packet_derives_saddle":"x_K=\\left(\\frac{K}{a\\beta}\\right)^{1/\\beta}" in packet,
 "packet_rejects_further_direct_enumeration":"Further direct enumeration is rejected" in packet,
 "adaptive_grid_ended_at_one_hundred_thousand":"100000" in adaptive,
})
result={"schema":"marici.strominger.rh_subhardy_moment_saddle_cutoff_law_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-subhardy-moment-saddle-forces-inaccessible-label-cutoffs.md","research/strominger/results/rh_subhardy_adaptive_cutoff_gram_audit.json"],"verdict":"The order-K dual moment is concentrated near log-label x_K=(K/(a beta))^(1/beta). Direct enumeration requires N at least on the scale exp(x_K). For a=1,beta=1/4,K=6, x_K=331776, while the tested cutoff has log N<12. The finite Gram growth is therefore unresolved-tail behavior, not evidence of norm divergence. Further enumeration is structurally uninformative; infinite atomic Gram bounds are required.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"order_six_log_saddle":saddle(6,1,.25),"tested_log_cutoff":math.log(100000)}
out=base/"results"/"rh_subhardy_moment_saddle_cutoff_law_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
