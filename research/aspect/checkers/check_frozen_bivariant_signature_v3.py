import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v2 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v2.json").read_text(encoding="utf-8"))
v3 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v3.json").read_text(encoding="utf-8"))


def matrix_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


# Positive repair packet: the same Ising cell in a nonorthonormal domain frame.
F0 = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S = sp.diag(2, 1)
F_positive = F0 * S
G_positive_domain = S.T * S
G_positive_codomain = sp.eye(2)

# Unused local packet: a rational Lorentz isometry in independent GL frames.
J = sp.diag(1, -1)
L = sp.Matrix([[sp.Rational(5, 4), sp.Rational(3, 4)], [sp.Rational(3, 4), sp.Rational(5, 4)]])
S_domain = sp.Matrix([[2, 1], [0, 1]])
S_codomain = sp.Matrix([[1, 0], [1, 2]])
F_indefinite = sp.simplify(S_codomain.inv() * L * S_domain)
G_domain = S_domain.T * J * S_domain
G_codomain = S_codomain.T * J * S_codomain
F_sharp = sp.simplify(G_domain.inv() * F_indefinite.T * G_codomain)

required_laws = set(v3["metric_matrix_route_associator"]["required_laws"])
checks = {
    "v2_preserved_as_failed_predecessor": "domain_gram" not in v2["matrix_route_associator"]["required_fields"],
    "v3_is_new_frozen_candidate": v3["status"] == "candidate_frozen" and v3["cell_creation_during_replay"] is False,
    "route_metrics_are_required": "gram_matrix" in v3["labelled_metric_route_space"]["required_fields"],
    "signatures_are_required": "signature" in v3["labelled_metric_route_space"]["required_fields"],
    "GL_covariance_is_required": "GL_covariance_under_independent_invertible_route_frame_changes" in required_laws,
    "positive_repair_packet_is_metric_isometry": matrix_zero(F_positive.T * G_positive_codomain * F_positive - G_positive_domain),
    "lorentz_seed_preserves_J": matrix_zero(L.T * J * L - J),
    "unused_GL_frames_are_invertible": S_domain.det() != 0 and S_codomain.det() != 0,
    "unused_indefinite_packet_is_metric_isometry": matrix_zero(F_indefinite.T * G_codomain * F_indefinite - G_domain),
    "metric_dagger_is_inverse": matrix_zero(F_sharp * F_indefinite - sp.eye(2)),
    "domain_signature_is_indefinite": G_domain.det() < 0,
    "codomain_signature_is_indefinite": G_codomain.det() < 0,
    "raw_unitarity_is_not_required": not matrix_zero(F_indefinite.T * F_indefinite - sp.eye(2)),
    "local_packet_not_global_admission": v3["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v3-check.v1",
    "status": "candidate_v3_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "v2_disposition": "preserved as falsified",
    "v3_disposition": "candidate frozen; positive repair and unused indefinite local gates pass; global admission not earned",
    "next_decisive_test": "complete unused metric fusion packet with every metric pentagon and hexagon, cell creation disabled",
}

out = root / "results" / "frozen_bivariant_signature_v3.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v3_frozen_local_schema_pass" else 1)
