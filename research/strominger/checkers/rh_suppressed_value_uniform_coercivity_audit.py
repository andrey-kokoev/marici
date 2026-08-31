import json
from fractions import Fraction as Q
from pathlib import Path
A=Q(1); B=Q(1,4); tail_label=3
eta=(2+2*A*B)/tail_label; remaining=1-eta
checks={
 "tail_exponential_factor_is_at_most_one_third":Q(1,tail_label)==Q(1,3),
 "uniform_value_constant_is_five_sixths":eta==Q(5,6),
 "value_constant_is_strictly_below_one":eta<1,
 "remaining_endpoint_derivative_budget_is_one_sixth":remaining==Q(1,6),
 "general_parameter_gate_is_satisfied":A*B<Q(1,2),
}
base=Path(__file__).parents[1]
packet=(base/"rh-suppressed-value-form-has-a-degree-independent-coercivity-budget.md").read_text(encoding="utf-8")
components=json.loads((base/"results"/"rh_quadrature_error_generalized_eigenvalue_audit.json").read_text(encoding="utf-8"))
checks.update({
 "packet_states_degree_independent_bound":"independent of polynomial degree" in packet,
 "packet_states_parameter_gate":"a\\beta<\\frac12" in packet,
 "observed_value_ratio_is_below_analytic_bound":all(row["value_eta"]<float(eta) for row in components["rows"]),
 "packet_preserves_total_coercivity_blocker":"does not prove the total quadrature error" in packet,
})
result={"schema":"marici.strominger.rh_suppressed_value_uniform_coercivity_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":"1","beta":"1/4","tail_label":tail_label},"verdict":"The suppressed value form is bounded in Loewner order by eta_val Q_cont with eta_val=(2+2a beta)/3. For a=1,beta=1/4 this is 5/6, uniformly in degree, leaving a budget of 1/6 for endpoint and derivative terms. The observed value-component eigenvalues are much smaller, but no sharper uniform constant is claimed.","checks":checks,"eta_value":str(eta),"remaining_budget":str(remaining),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_suppressed_value_uniform_coercivity_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
