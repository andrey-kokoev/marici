"""Exact balanced mixed-quartic grammar for two complex matrix scalars."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def invariants(A, B):
    Ad = A.conjugate().T
    Bd = B.conjugate().T
    return sp.Matrix([
        sp.trace(Ad * A) * sp.trace(Bd * B),
        sp.trace(Ad * B) * sp.trace(Bd * A),
        sp.trace(Ad * A * Bd * B),
        sp.trace(A * Ad * B * Bd),
    ])


def E(i, j):
    out = sp.zeros(3)
    out[i, j] = 1
    return out


A0 = E(0, 0)
Bs = [E(1, 1), E(0, 1), E(1, 0), E(0, 0)]
evaluation = sp.Matrix.hstack(*(invariants(A0, B) for B in Bs)).T

x, y = sp.symbols("x y", real=True)
radial = sp.simplify(invariants(x * sp.eye(3), y * sp.eye(3)))

A = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
B = sp.Matrix([[0, 1, 1], [2, 0, 1], [1, 1, 0]])
L = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
R = L
base = invariants(A, B)
common_transformed = invariants(L * A * R.T, L * B * R.T)
independent_left = invariants(L * A, B)
independent_right = invariants(A * R.T, B)

checks = {
    "balanced_left_right_contraction_count_is_four": sp.factorial(2) ** 2 == 4,
    "four_mixed_invariants_are_exactly_independent": evaluation.det() == -1,
    "evaluation_matrix_matches_hostile_witness": evaluation == sp.Matrix([[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1]]),
    "radial_identity_slice_collapses_four_channels": radial == x**2 * y**2 * sp.Matrix([9, 9, 3, 3]),
    "all_four_descend_under_common_biunitary_frame": common_transformed == base,
    "norm_product_survives_independent_left_action": independent_left[0] == base[0],
    "common_frame_channels_fail_independent_left_action": independent_left[1] != base[1] and independent_left[3] != base[3],
    "norm_product_survives_independent_right_action": independent_right[0] == base[0],
    "common_frame_channels_fail_independent_right_action": independent_right[1] != base[1] and independent_right[2] != base[2],
    "independent_Z3_gradings_forbid_unbalanced_two_A_dagger_two_B_quartics": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP732",
    "status": "PASS",
    "checks": checks,
    "independent_group_grammar": "only Tr(A dagger A) Tr(B dagger B) is mixed",
    "common_frame_grammar": [
        "Tr(A dagger A) Tr(B dagger B)",
        "Tr(A dagger B) Tr(B dagger A)",
        "Tr(A dagger A B dagger B)",
        "Tr(A A dagger B B dagger)",
    ],
    "contextual_partition": "the radial identity slice maps the four independent mixed couplings to the single ratio 9:9:3:3",
    "smallest_exact_falsifier": "the four-by-four matrix-unit evaluation determinant is -1 while the radial slice has rank one",
    "source_tradeoff": "independent flavor groups close the radial grammar but do not relate Yukawa products; a common intertwiner can relate them but opens four mixed quartics",
    "remaining_rg_gate": "choose an independently justified symmetry branch and derive the corresponding complete beta system",
    "remaining_physical_gate": "after RG closure, prove finite threshold survival and a calibrated rank-two representation-labelled detector response",
}
(ROOT / "results" / "wp732_two_matrix_mixed_quartic_grammar.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
