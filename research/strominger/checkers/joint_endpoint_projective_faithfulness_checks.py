"""Exact finite witness for joint endpoint/projective faithfulness modulo center."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "joint_endpoint_projective_faithfulness_checks.json"

I2 = sp.eye(2)
T = sp.Matrix([[1, 1], [0, 1]])
U = sp.Matrix([[1, 0], [-1, 1]])


def compose(p, q):
    """Return p after q for permutations represented by image tuples."""
    return tuple(p[q[i]] for i in range(4))


def inverse(p):
    out = [0] * 4
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


s1 = (1, 0, 2, 3)
s2 = (0, 2, 1, 3)
s3 = (0, 1, 3, 2)
identity = (0, 1, 2, 3)

# a=sigma1 sigma3^{-1}; b is its sigma2 conjugate.
a_perm = compose(s1, inverse(s3))
b_perm = compose(s2, compose(a_perm, inverse(s2)))
ab_perm = compose(a_perm, b_perm)

a_matrix = T * T.inv()
b_matrix = U * a_matrix * U.inv()
kernel_permutations = {identity, a_perm, b_perm, ab_perm}

checks = {
    "projective_kernel_generators_map_to_identity": a_matrix == I2 and b_matrix == I2,
    "kernel_endpoint_images_form_four_elements": len(kernel_permutations) == 4,
    "first_kernel_generator_is_double_transposition": a_perm == (1, 0, 3, 2),
    "second_kernel_generator_is_double_transposition": b_perm == (2, 3, 0, 1),
    "third_kernel_element_is_double_transposition": ab_perm == (3, 2, 1, 0),
    "endpoint_is_injective_on_projective_kernel": identity not in {a_perm, b_perm, ab_perm},
    "full_twist_remains_jointly_invisible": (T * U * T) ** 4 == I2,
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.joint-endpoint-projective-faithfulness.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "projective_kernel_on_M04": {
        "external_theorem": "Klein four group",
        "endpoint_images": [list(p) for p in sorted(kernel_permutations)],
        "endpoint_restriction": "injective",
    },
    "conclusion": "the joint endpoint and projective map is faithful on M(0,4); its pullback to B_4(S^2) has precisely the central full-twist kernel",
    "source_boundary": "kernel identification on M(0,4) and the central quotient B_4(S^2)->M(0,4) are external group theorems; this checker verifies their finite compatibility with the chosen generators",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
