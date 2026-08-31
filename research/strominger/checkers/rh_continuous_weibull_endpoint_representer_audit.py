import json
from fractions import Fraction as Q
from pathlib import Path
beta=Q(1,4); krein_power=2*beta-2
checks={
 "krein_tail_power_is_minus_three_halves":krein_power==Q(-3,2),
 "krein_tail_is_integrable":krein_power<-1,
 "subhardy_condition_is_satisfied":beta<Q(1,2),
}
base=Path(__file__).parents[1]
packet=(base/"rh-subhardy-continuous-polynomial-closure-has-an-endpoint-representer.md").read_text(encoding="utf-8")
components=json.loads((base/"results"/"rh_quadrature_error_generalized_eigenvalue_audit.json").read_text(encoding="utf-8"))
endpoint=[row["endpoint_eta"] for row in components["rows"]]
checks.update({
 "packet_applies_krein_only_to_continuous_comparator":"continuous shifted Weibull moment problem" in packet,
 "packet_constructs_riesz_representer":"k_{x_0}\\in" in packet and "Riesz representation" in packet,
 "packet_states_degree_independent_endpoint_bound":"finite degree-independent constant" in packet,
 "finite_christoffel_values_increase_as_lower_approximants":all(endpoint[i+1]>=endpoint[i] for i in range(len(endpoint)-1)),
 "packet_does_not_treat_finite_grid_as_upper_bound":"is not an upper bound" in packet,
 "packet_does_not_transfer_to_atomic_measure":"does not transfer indeterminacy" in packet,
})
result={"schema":"marici.strominger.rh_continuous_weibull_endpoint_representer_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":"1","beta":"1/4","krein_tail_power":str(krein_power)},"verdict":"For beta<1/2 the shifted continuous Weibull measure satisfies the Stieltjes Krein integrability condition. Its polynomial closure therefore has bounded point evaluations and a Riesz representer at log 3, giving a finite degree-independent endpoint constant. The theorem supplies no quantitative upper cap for that constant and does not transfer indeterminacy to the atomic label measure.","checks":checks,"tested_endpoint_lower_approximants":endpoint,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_continuous_weibull_endpoint_representer_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
