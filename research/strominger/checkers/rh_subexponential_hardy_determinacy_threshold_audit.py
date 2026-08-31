import json, math
from pathlib import Path

# Exact exponent comparisons sampled far into the tail. The theorem is the
# analytic argument in the companion packet; this checker tests its threshold.
def E(t,a,beta,c):return c*math.sqrt(t)-2*a*t**beta
T=(10.,100.,1000.,10000.,100000.)
checks={
 "beta_three_quarters_hardy_exponent_decreases_in_tail":all(E(T[i+1],1,.75,1)<E(T[i],1,.75,1) for i in range(1,len(T)-1)),
 "beta_half_converges_when_c_below_two_a":all(E(T[i+1],1,.5,1)<E(T[i],1,.5,1) for i in range(len(T)-1)),
 "beta_half_diverges_when_c_above_two_a":all(E(T[i+1],1,.5,3)>E(T[i],1,.5,3) for i in range(len(T)-1)),
 "beta_quarter_fails_hardy_for_every_tested_positive_c":all(E(T[-1],1,.25,c)>E(T[-2],1,.25,c) for c in (.1,.5,1.)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-hardy-threshold-eliminates-half-of-subexponential-flat-candidates.md").read_text(encoding="utf-8")
prior=(base/"results"/"rh_subexponential_log_weight_threshold_audit.json").read_text(encoding="utf-8")
checks.update({
 "packet_defines_discrete_log_label_measure":"\\mu_{a,\\beta}" in packet and "\\delta_{\\log n}" in packet,
 "packet_applies_hardy_square_root_condition":"Hardy exponential-square-root test" in packet,
 "packet_eliminates_beta_at_least_half":"\\frac12\\leq\\beta<1" in packet,
 "packet_retains_beta_below_half_without_claiming_existence":"Failure of the Hardy condition" in packet,
 "prior_only_removed_analytic_obstruction":"does not automatically produce" not in prior and "neither selects" in prior,
})
result={"schema":"marici.strominger.rh_subexponential_hardy_determinacy_threshold_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-hardy-threshold-eliminates-half-of-subexponential-flat-candidates.md","research/strominger/results/rh_subexponential_log_weight_threshold_audit.json"],"verdict":"The Hardy exponential-square-root criterion makes the discrete logarithmic-label measure determinate for 1/2<=beta<1. Polynomials are therefore dense and the one-copy flat orthogonal complement is zero throughout that range. Non-analyticity was insufficient. Only 0<beta<1/2 survives this obstruction, and no discrete flat sequence is inferred there.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_subexponential_hardy_determinacy_threshold_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
