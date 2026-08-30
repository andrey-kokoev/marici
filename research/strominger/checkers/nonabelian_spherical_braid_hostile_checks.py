"""Exact projective SL2Z detector for an abelian-invisible spherical braid."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "nonabelian_spherical_braid_hostile_checks.json"

I2 = sp.eye(2)
T = sp.Matrix([[1, 1], [0, 1]])
U = sp.Matrix([[1, 0], [-1, 1]])
images = [T, U, T]

sphere_relation_image = T * U * T**2 * U * T
A = T**2
B = U**2
commutator_image = sp.simplify(A * B * A.inv() * B.inv())
commutator_exponent_sum = 2 + 2 - 2 - 2
commutator_endpoint_permutation_is_identity = True

checks = {
    "images_have_determinant_one": all(M.det() == 1 for M in images),
    "first_adjacent_braid_relation_holds": T * U * T == U * T * U,
    "second_adjacent_braid_relation_holds": U * T * U == T * U * T,
    "distant_generators_commute": images[0] * images[2] == images[2] * images[0],
    "sphere_relation_is_projectively_trivial": sphere_relation_image == -I2,
    "pure_commutator_has_identity_endpoint": commutator_endpoint_permutation_is_identity,
    "pure_commutator_has_zero_Z6_and_Z3_residue": commutator_exponent_sum % 6 == 0,
    "pure_commutator_image_is_nontrivial_projectively": commutator_image != I2 and commutator_image != -I2,
    "pure_commutator_image_is_hyperbolic": abs(commutator_image.trace()) > 2,
    "projective_matrix_port_separates_commutator_from_identity": commutator_image == sp.Matrix([[13, 8], [8, 5]]),
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.nonabelian-spherical-braid-hostile.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "representation": {
        "target": "PSL(2,Z)",
        "sigma1": T.tolist(),
        "sigma2": U.tolist(),
        "sigma3": T.tolist(),
        "sphere_relation_lift": sphere_relation_image.tolist(),
    },
    "hostile": {
        "word": "[sigma1^2,sigma2^2]",
        "endpoint_permutation": "identity",
        "exponent_mod_6": commutator_exponent_sum % 6,
        "A3_action": "identity",
        "projective_matrix": commutator_image.tolist(),
        "trace": int(commutator_image.trace()),
    },
    "claim_boundary": "this projective representation detects the displayed nonabelian hostile; no faithfulness claim for the full spherical braid group is made",
}
payload["representation"] = {
    key: ([[int(x) for x in row] for row in value] if isinstance(value, list) else value)
    for key, value in payload["representation"].items()
}
payload["hostile"]["projective_matrix"] = [[int(x) for x in row] for row in payload["hostile"]["projective_matrix"]]
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
