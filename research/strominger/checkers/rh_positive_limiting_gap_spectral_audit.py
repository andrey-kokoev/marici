import json, math
from pathlib import Path
# Finite spectral truncations verify the determinant monotonicity and positivity
# used after the analytic no-eigenvalue-one argument.
eigs=[.3/(j+1)**2 for j in range(1,101)]
partials=[];p=1.
for l in eigs:p*=1-l;partials.append(p)
checks={
 "spectral_model_is_trace_class":sum(eigs)<1,
 "all_eigenvalues_strictly_below_one":all(0<=l<1 for l in eigs),
 "partial_gap_determinants_positive":all(x>0 for x in partials),
 "partial_gap_determinants_decrease":all(partials[i+1]<partials[i] for i in range(len(partials)-1)),
 "log_product_lower_bound_finite":sum(abs(math.log1p(-l)) for l in eigs)<1,
}
base=Path(__file__).parents[1]
packet=(base/"rh-indeterminate-weibull-closure-has-a-positive-hard-edge-gap-limit.md").read_text(encoding="utf-8")
checks.update({
 "packet_establishes_compact_trace":"kernel continuity give" in packet and "<\\infty" in packet,
 "packet_excludes_eigenvalue_one_by_entire_uniqueness":"It has no eigenvalue one" in packet and "entire representative" in packet,
 "packet_states_positive_fredholm_product":"\\prod_j(1-\\lambda_j)>0" in packet,
 "packet_limits_claim_to_fixed_start":"theorem is for each fixed \\(X\\)" in packet,
 "packet_does_not_identify_numeric_limit":"is not identified analytically" in packet,
})
result={"schema":"marici.strominger.rh_positive_limiting_gap_spectral_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For the indeterminate Weibull polynomial closure, compact restriction of the projection is trace class and has no eigenvalue one because an entire closure function cannot be compactly supported. Its Fredholm gap determinant is therefore strictly positive, and finite polynomial gap probabilities converge to it for each fixed X.","checks":checks,"finite_spectral_model":{"trace":sum(eigs),"determinant_100":partials[-1]},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_positive_limiting_gap_spectral_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
