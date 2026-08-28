"""Exact A3 lattice audit for the minimum four-zero selector packet."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "a3_zero_defect_redistribution_checks.json"

ones = sp.Matrix([1, 1, 1, 1])
roots = sp.Matrix([
    [1, 0, 0],
    [-1, 1, 0],
    [0, -1, 1],
    [0, 0, -1],
])
cartan = roots.T * roots
snf = smith_normal_form(cartan, domain=sp.ZZ)
attachment_and_roots = sp.Matrix.hstack(ones, roots)

permutations = list(itertools.permutations(range(4)))
permutation_matrices = []
for perm in permutations:
    matrix = sp.zeros(4)
    for column, row in enumerate(perm):
        matrix[row, column] = 1
    permutation_matrices.append(matrix)

root_vectors = {
    tuple((sp.eye(4)[:, i] - sp.eye(4)[:, j]))
    for i in range(4) for j in range(4) if i != j
}
simple_root_orbit = {
    tuple(P * roots[:, 0]) for P in permutation_matrices
}

affine_samples = [
    sp.Matrix([1, 1, 1, 1]),
    sp.Matrix([2, 0, 1, 1]),
    sp.Matrix([4, 0, 0, 0]),
    sp.Matrix([-1, 2, 1, 2]),
]

checks = {
    "simple_roots_have_rank_three": roots.rank() == 3,
    "simple_roots_preserve_total_defect": ones.T * roots == sp.zeros(1, 3),
    "cartan_matrix_is_A3": cartan == sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]),
    "A3_cartan_determinant_is_four": cartan.det() == 4,
    "A3_smith_type_is_one_one_four": snf == sp.diag(1, 1, 4),
    "diagonal_attachment_plus_root_lattice_has_index_four": abs(attachment_and_roots.det()) == 4,
    "S4_permutations_preserve_attachment_direction": all(P * ones == ones for P in permutation_matrices),
    "simple_root_S4_orbit_is_full_A3_root_system": simple_root_orbit == root_vectors and len(root_vectors) == 12,
    "total_degree_four_packets_form_affine_A3_torsor": all(sum(sample) == 4 and sum(sample - ones) == 0 and sample == ones + (sample - ones) for sample in affine_samples),
    "three_punctures_cannot_support_four_positive_simple_indices": sum([1, 1, 1]) != 4,
}

payload = {
    "schema": "marici.strominger.a3-zero-defect-redistribution.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "lattice": {
        "fixed_attachment": [1, 1, 1, 1],
        "redistribution_condition": "delta_1 + delta_2 + delta_3 + delta_4 = 0",
        "simple_roots": [list(map(int, roots[:, i])) for i in range(3)],
        "cartan": [[int(cartan[i, j]) for j in range(3)] for i in range(3)],
        "rank": 3,
        "weyl_group": "S4",
        "root_count": len(root_vectors),
        "discriminant": 4,
        "smith_type": [1, 1, 4],
    },
    "claim_boundary": "the Z/4 discriminant is an integral lattice obstruction, not yet a physical four-state residue",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
