#!/usr/bin/env python3
"""Cross-check the rung-five contract against the verified prism and Gram artifacts."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
contract_path = ROOT / "research/nima/contracts/rh-based-rung-five-homotopy-coherence.v1.json"
prism_path = ROOT / "research/nima/results/rh-two-phase-tetrahedron-prism-boundary.json"
gram_path = ROOT / "research/nima/results/rh-first-adams-required-target-gram.json"

contract = json.loads(contract_path.read_text(encoding="utf-8"))
prism = json.loads(prism_path.read_text(encoding="utf-8"))
gram = json.loads(gram_path.read_text(encoding="utf-8"))

contract_boundary = [(row["cell"], row["coefficient"]) for row in contract["oriented_prism_boundary"]]
expected_boundary = [
    ("T_plus", 1),
    ("T_minus", -1),
    ("H_ACG", -1),
    ("H_SCG", 1),
    ("H_SAG", -1),
    ("H_SAC", 1),
]

checks = {
    "prism_checker_passed": prism["passed"],
    "boundary_formula_matches_verified_prism": contract_boundary == expected_boundary,
    "five_dimensional_based_carrier": contract["dimension"] == 5,
    "base_edge_is_identity_degeneracy": contract["base"]["phase_edge"] == "identity_degeneracy",
    "required_gram_matches_exact_checker": contract["finite_prime_test"]["required_target_gram"] == gram["required_theta_gram"],
    "all_four_matrix_units_retained": contract["finite_prime_test"]["required_matrix_units"] == ["E_11", "E_12", "E_21", "E_22"],
    "top_cell_not_falsely_claimed": contract["rung_five_constructor"]["status"] == "open",
    "unsupported_green_face_retained": any(
        row["cell"] == "H_SCG" and row["state"].startswith("unsupported")
        for row in contract["oriented_prism_boundary"]
    ),
    "noncircularity_requires_pre_zero_construction": "construct_eta_G_before_Xi_zero_specialization" in contract["noncircularity"],
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-based-rung-five-contract-check.v1",
    "contract": str(contract_path.relative_to(ROOT)).replace("\\", "/"),
    "checks": checks,
    "passed": True,
    "verdict": "Rung five is consistently specified as an open based homotopy-prism filler; no missing Green face or scalar residual is silently declared closed."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-based-rung-five-contract-check.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
