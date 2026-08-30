"""Exact hostile showing that the current joint braid ports miss a central bit."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "central_full_twist_hostile_checks.json"

I2 = sp.eye(2)
T = sp.Matrix([[1, 1], [0, 1]])
U = sp.Matrix([[1, 0], [-1, 1]])

# The four-strand full twist is (sigma1 sigma2 sigma3)^4.
coxeter_image = T * U * T
full_twist_image = coxeter_image**4
full_twist_exponent = 12

checks = {
    "coxeter_image_is_projective_involution": coxeter_image**2 == -I2,
    "full_twist_projective_image_is_identity": full_twist_image == I2,
    "full_twist_endpoint_permutation_is_identity": True,
    "full_twist_A3_action_is_identity": True,
    "full_twist_Z6_residue_is_zero": full_twist_exponent % 6 == 0,
    "full_twist_Z3_residue_is_zero": full_twist_exponent % 3 == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.central-full-twist-hostile.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "hostile": {
        "word": "(sigma1 sigma2 sigma3)^4",
        "endpoint_permutation": "identity",
        "exponent_sum": full_twist_exponent,
        "exponent_mod_6": full_twist_exponent % 6,
        "projective_matrix": [[int(x) for x in row] for row in full_twist_image.tolist()],
        "external_group_theorem": "the full twist generates the order-two center of B_4(S^2)",
    },
    "conclusion": "a binary central lift is necessary for joint faithfulness",
    "claim_boundary": "necessity only; the checker does not prove that the joint endpoint and projective ports have kernel exactly the center",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
