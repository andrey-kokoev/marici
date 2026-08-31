import json
from pathlib import Path
base=Path(__file__).parents[1]
packet=(base/"rh-existing-weibull-data-do-not-cap-the-endpoint-kernel.md").read_text(encoding="utf-8")
representer=(base/"results"/"rh_continuous_weibull_endpoint_representer_audit.json").read_text(encoding="utf-8")
gamma=(base/"results"/"rh_atomic_log_moment_gamma_comparator_audit.json").read_text(encoding="utf-8")
eigs=json.loads((base/"results"/"rh_quadrature_error_generalized_eigenvalue_audit.json").read_text(encoding="utf-8"))
endpoint=[r["endpoint_eta"] for r in eigs["rows"]]
checks={
 "krein_artifact_claims_finiteness_not_numeric_cap":"no quantitative upper cap" in representer,
 "finite_christoffel_sequence_is_monotone_increasing":all(endpoint[i+1]>=endpoint[i] for i in range(len(endpoint)-1)),
 "gamma_artifact_preserves_loewner_blocker":"do not preserve Hankel Loewner order" in gamma,
 "packet_identifies_positive_uncomputed_kernel_tail":"K(x_0,x_0)-K_K(x_0,x_0)" in packet,
 "packet_lists_required_quantitative_constructors":"explicit Nevanlinna matrix" in packet and "trial representer" in packet,
 "packet_rejects_finite_value_as_upper_bound":"cannot be promoted to an upper bound" in packet,
 "packet_does_not_claim_impossibility":"does not prove that no endpoint cap exists" in packet,
}
result={"schema":"marici.strominger.rh_endpoint_kernel_cap_source_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-existing-weibull-data-do-not-cap-the-endpoint-kernel.md","research/strominger/results/rh_continuous_weibull_endpoint_representer_audit.json","research/strominger/results/rh_atomic_log_moment_gamma_comparator_audit.json","research/strominger/results/rh_quadrature_error_generalized_eigenvalue_audit.json"],"verdict":"Current artifacts prove endpoint-kernel finiteness and provide monotone finite lower approximants, but no quantitative upper cap. Krein integrability is qualitative; finite Christoffel values approach from below; independent moment intervals cannot be inverted in Loewner order. The present 1/6 coercivity-budget proof is therefore blocked pending an explicit representer norm, Nevanlinna/recurrence tail bound, or a sharper quadrature decomposition.","checks":checks,"endpoint_lower_approximants":endpoint,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_endpoint_kernel_cap_source_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
