import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v1 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v1.json").read_text(encoding="utf-8"))
v2 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v2.json").read_text(encoding="utf-8"))

F_ising = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
theta, psi = sp.symbols("theta psi", real=True)
U_domain = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
U_codomain = sp.Matrix([[sp.cos(psi), -sp.sin(psi)], [sp.sin(psi), sp.cos(psi)]])
F_gauge = sp.simplify(U_codomain * F_ising * U_domain.T)


def matrix_zero(matrix):
    return all(sp.simplify(sp.expand_trig(entry)) == 0 for entry in matrix)


required_laws = set(v2["matrix_route_associator"]["required_laws"])
checks = {
    "v1_remains_unchanged_and_failed": "matrix_route_associator" not in v1["cell_types"],
    "v2_is_separate_candidate": v2["status"] == "candidate_frozen" and v2["predecessor"].endswith("v1.json"),
    "replay_cell_creation_disabled": v2["cell_creation_during_replay"] is False,
    "matrix_associator_is_explicit_type": "matrix_route_associator" in v2["cell_types"],
    "pentagon_is_mandatory": "pentagon_on_every_admissible_quadruple" in required_laws,
    "hexagon_is_conditional_mandatory": "hexagon_when_braided_exchange_is_present" in required_laws,
    "gauge_covariance_is_mandatory": "gauge_covariance_under_independent_route_basis_changes" in required_laws,
    "local_to_global_promotion_forbidden": "local unitarity promoted to full packet admission" in v2["forbidden_promotions"],
    "unused_ising_local_associator_is_unitary": matrix_zero(F_ising.T * F_ising - sp.eye(2)),
    "unused_ising_associator_mixes_routes": all(entry != 0 for entry in F_ising),
    "gauge_transformed_associator_remains_unitary": matrix_zero(F_gauge.T * F_gauge - sp.eye(2)),
    "local_ising_test_not_global_admission": v2["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v2-check.v1",
    "status": "candidate_v2_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "v1_disposition": "preserved as falsified",
    "v2_disposition": "candidate frozen; local Ising schema gate passes; global packet admission not yet earned",
    "next_decisive_test": "complete unused fusion packet with every required pentagon and hexagon, cell creation disabled",
}

out = root / "results" / "frozen_bivariant_signature_v2.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v2_frozen_local_schema_pass" else 1)
