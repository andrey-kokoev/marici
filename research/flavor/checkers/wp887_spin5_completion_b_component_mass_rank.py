import json
from pathlib import Path

import sympy as sp


I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.diag(1, -1)
eye2 = sp.eye(2)
kron = sp.kronecker_product
gammas = [
    kron(s1, s1),
    kron(s2, s1),
    kron(s3, s1),
    kron(eye2, s2),
    kron(eye2, s3),
]
C = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])

phi = sp.Matrix([1, 2, 3, 5])
phi_tilde = C * phi.conjugate()


def B(x):
    return sp.Matrix.hstack(*[C * gamma * x for gamma in gammas])


def q(x):
    return C * x


mass = sp.zeros(16)


def symmetric_block(row, col, block, coefficient):
    weighted = coefficient * block
    mass[row : row + block.rows, col : col + block.cols] = weighted
    mass[col : col + block.cols, row : row + block.rows] = weighted.T


# Component order: S[0:4], V[4:9], X[9:13], n0[13], n1[14], n2[15].
symmetric_block(0, 4, B(phi), 2)
symmetric_block(9, 4, B(phi_tilde), 3)
symmetric_block(0, 13, q(phi_tilde), 5)
symmetric_block(0, 14, q(phi), 7)
symmetric_block(9, 14, q(phi_tilde), 11)
symmetric_block(9, 15, q(phi), 13)

determinant = sp.simplify(mass.det())
tests = {
    "five_gamma_matrices_present": len(gammas) == 5,
    "clifford_relations_hold": all(
        gammas[a] * gammas[b] + gammas[b] * gammas[a]
        == (2 if a == b else 0) * sp.eye(4)
        for a in range(5)
        for b in range(5)
    ),
    "C_is_antisymmetric": C.T == -C,
    "C_is_invertible": C.det() != 0,
    "charge_conjugation_intertwines_all_gammas": all(gamma.T * C == C * gamma for gamma in gammas),
    "spinor_vector_intertwiner_has_rank_three": B(phi).rank() == 3,
    "mass_matrix_is_symmetric": mass.T == mass,
    "mass_matrix_dimension_is_sixteen": mass.shape == (16, 16),
    "exact_witness_determinant_matches": determinant == sp.Integer(468887390507036217600),
    "exact_witness_has_full_rank": mass.rank() == 16,
    "zero_yukawa_hostile_has_rank_zero": sp.zeros(16).rank() == 0,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP887",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "generic_full_rank_not_selector: Completion B is massable with declared scalars but its spectrum remains parameter dependent",
    "component_dimension": 16,
    "witness_phi": [1, 2, 3, 5],
    "witness_yukawas": [2, 3, 5, 7, 11, 13],
    "witness_determinant": str(determinant),
    "witness_rank": mass.rank(),
    "generic_statement": "nonzero polynomial witness implies full rank on a nonempty Zariski-open parameter set",
    "smallest_hostile": "all six Yukawa coefficients vanish, giving rank zero",
    "remaining_gate": "source selection of Yukawa matrices and spinor-Higgs vacuum, followed by RG, widths, and calibrated pole readout",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp887_spin5_completion_b_component_mass_rank.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
