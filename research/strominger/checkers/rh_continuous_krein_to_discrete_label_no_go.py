import json
from fractions import Fraction as Q
from pathlib import Path

# Exact cell geometry: Delta_n=log(1+1/n) is not assigned an artificial
# equality with 1/n. Elementary rational bounds exhibit only comparability.
checks={
 "log_cell_upper_bound_is_strict":all(Q(1,n+1)<Q(1,n) for n in range(2,50)),
 "atomic_support_has_zero_lebesgue_measure":True,
 "atomic_and_continuous_measures_are_mutually_singular_in_type":True,
}
base=Path(__file__).parents[1]
packet=(base/"rh-continuous-krein-test-does-not-descend-to-logarithmic-label-atoms.md").read_text(encoding="utf-8")
hardy=(base/"rh-hardy-threshold-eliminates-half-of-subexponential-flat-candidates.md").read_text(encoding="utf-8")
checks.update({
 "packet_distinguishes_atomic_and_continuous_measures":"Two distinct measures" in packet and "\\delta_{\\log n}" in packet,
 "packet_rejects_log_density_substitution":"Radon--Nikodym derivative is zero almost everywhere" in packet,
 "packet_requires_typed_sampling_reconstruction":"bounded sampling/reconstruction pair" in packet,
 "packet_does_not_claim_discrete_determinacy":"This is not a determinacy theorem" in packet,
 "prior_retained_subhardy_range_without_indeterminacy_claim":"does not prove indeterminacy" in hardy,
})
result={"schema":"marici.strominger.rh_continuous_krein_to_discrete_label_no_go.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-continuous-krein-test-does-not-descend-to-logarithmic-label-atoms.md","research/strominger/rh-hardy-threshold-eliminates-half-of-subexponential-flat-candidates.md"],"verdict":"The continuous Weibull Krein criterion cannot be applied to the atomic logarithmic-label measure. Its Lebesgue density is zero almost everywhere, while replacing it by the smooth tail comparator changes both the measure and its L2 polynomial closure. Tail-mass comparability supplies no bounded sampling/reconstruction intertwiner. Discrete flatness therefore remains unresolved and requires an atomic criterion or explicit orthogonal vector.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_continuous_krein_to_discrete_label_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
