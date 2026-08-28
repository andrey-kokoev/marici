import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
contract = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v2.json").read_text(encoding="utf-8"))

F_orthonormal = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S_domain = sp.diag(2, 1)
F_nonorthogonal = sp.simplify(F_orthonormal * S_domain)
G_domain = S_domain.T * S_domain
G_codomain = sp.eye(2)


def matrix_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


raw_unitarity_residual = sp.simplify(F_nonorthogonal.T * F_nonorthogonal - sp.eye(2))
metric_isometry_residual = sp.simplify(F_nonorthogonal.T * G_codomain * F_nonorthogonal - G_domain)

checks = {
    "v2_is_frozen": contract["cell_creation_during_replay"] is False,
    "v2_requires_raw_dagger_unitarity": "dagger_unitarity" in contract["matrix_route_associator"]["required_laws"],
    "v2_has_no_route_metric_field": "domain_gram" not in contract["matrix_route_associator"]["required_fields"],
    "coordinate_change_is_invertible": S_domain.det() != 0,
    "coordinate_change_is_not_unitary": S_domain.T * S_domain != sp.eye(2),
    "same_cell_fails_raw_unitarity": not matrix_zero(raw_unitarity_residual),
    "same_cell_preserves_transported_metric": matrix_zero(metric_isometry_residual),
    "physical_determinant_relation": sp.simplify(F_nonorthogonal.det() ** 2 - G_domain.det()) == 0,
}

result = {
    "schema": "marici.aspect.v2-nonorthonormal-route-frame-falsifier.v1",
    "status": "frozen_v2_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "hostile": "the unused Ising associator expressed in an invertible nonorthonormal domain route frame",
    "failure": "v2 tests F^*F=I without carrying domain and codomain Gram metrics",
    "required_future_repair": "metric-relative dagger law F^* G_R F=G_L and GL route-frame covariance",
}

out = root / "results" / "v2_nonorthonormal_route_frame_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v2_falsified" else 1)
