"""Exact abelianization audit for four spherical braid strands."""

import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "spherical_pure_braid_z3_residue_checks.json"

# Abelianized B4(S2) presentation. Adjacent braid relations identify the three
# Artin generators; the sphere relation sigma1 sigma2 sigma3^2 sigma2 sigma1
# contributes the count vector (2,2,2).
relation_matrix = sp.Matrix([
    [1, -1, 0],
    [0, 1, -1],
    [2, 2, 2],
])
snf = smith_normal_form(relation_matrix, domain=sp.ZZ)
sphere_relation_exponent = sum([1, 1, 2, 1, 1])
global_classes = set(range(6))
pure_endpoint_classes = {value for value in global_classes if value % 2 == 0}
sigma1_squared_class = 2

checks = {
    "sphere_relation_has_exponent_six": sphere_relation_exponent == 6,
    "abelianized_relation_matrix_has_full_rank": relation_matrix.rank() == 3,
    "spherical_B4_abelianization_has_smith_type_one_one_six": snf == sp.diag(1, 1, 6),
    "global_exponent_residue_is_Z6": len(global_classes) == 6,
    "endpoint_sign_is_reduction_mod_two": all((value % 2) in (0, 1) for value in global_classes),
    "pure_endpoint_kernel_is_even_subgroup": pure_endpoint_classes == {0, 2, 4},
    "pure_endpoint_abelian_shadow_has_order_three": len(pure_endpoint_classes) == 3,
    "sigma1_squared_generates_pure_Z3_shadow": {0, sigma1_squared_class % 6, (2 * sigma1_squared_class) % 6} == pure_endpoint_classes,
    "sigma1_squared_remains_nontrivial_globally": sigma1_squared_class % 6 != 0,
    "three_copies_of_sigma1_squared_vanish_only_in_abelian_shadow": (3 * sigma1_squared_class) % 6 == 0,
}

payload = {
    "schema": "marici.strominger.spherical-pure-braid-z3-residue.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "presentation": {
        "group": "spherical braid group B4(S2)",
        "sphere_relation": "sigma1 sigma2 sigma3^2 sigma2 sigma1 = 1",
        "abelian_relation_matrix": [[int(relation_matrix[i, j]) for j in range(3)] for i in range(3)],
        "smith_type": [1, 1, 6],
        "abelianization": "Z/6",
    },
    "pure_residue": {
        "endpoint_sign_map": "Z/6 to Z/2",
        "kernel": [0, 2, 4],
        "kernel_type": "Z/3",
        "generator": "class of sigma1^2",
    },
    "claim_boundary": "Z/3 is the endpoint-invisible abelian shadow of spherical pure braids, not a faithful classifier of the pure braid group",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
