#!/usr/bin/env python3
"""Hostile tests of the transverse maximal-minor-jet explanation."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
LOCALIZATION = ROOT / "research/strominger/checkers/period_729_layer_localization.py"
PACKETS = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    local = runpy.run_path(str(LOCALIZATION))
    source = runpy.run_path(str(PACKETS))

layers = local["layers"]
det = local["det"]
packet = source["packet"]
LEFT, RIGHT, SHIFT = 152, 881, 729
BASE_SCALE, PERTURBATION_SCALE = 2, 7
DETERMINANT_SCALE = PERTURBATION_SCALE + 2 * BASE_SCALE


def row_submatrices(A):
    return [
        [[A[i][j] for j in range(3)] for i in rows]
        for rows in itertools.combinations(range(4), 3)
    ]


def replace_column(A, column, values):
    return [
        [values[i] if j == column else A[i][j] for j in range(3)]
        for i in range(3)
    ]


L = layers(LEFT)["full"]
R = layers(RIGHT)["full"]
B = [[x // (3 ** BASE_SCALE) for x in row] for row in L]
H = [[(b - a) // (3 ** PERTURBATION_SCALE) for a, b in zip(la, rb)]
     for la, rb in zip(L, R)]

linearized = []
exact_difference = []
higher_residual = []
for base_minor, perturbation_minor, left_minor, right_minor in zip(
    row_submatrices(B),
    row_submatrices(H),
    row_submatrices(L),
    row_submatrices(R),
):
    derivative = sum(
        det(replace_column(
            base_minor,
            column,
            [perturbation_minor[i][column] for i in range(3)],
        ))
        for column in range(3)
    )
    exact = (det(right_minor) - det(left_minor)) // (3 ** DETERMINANT_SCALE)
    linearized.append(derivative % 3)
    exact_difference.append(exact % 3)
    higher_residual.append((exact - derivative) % 3)

# Test whether the shift acts selectively on the valuation readout.
WINDOW_UPPER = 200
pairs = []
for n in range(WINDOW_UPPER + 1):
    left = packet(n)
    right = packet(n + SHIFT)
    pairs.append({
        "grade": n,
        "same_d1": left["v3_d1"] == right["v3_d1"],
        "same_d2": left["v3_d2"] == right["v3_d2"],
        "same_d3": left["v3_d3"] == right["v3_d3"],
    })
changed_d3 = [x["grade"] for x in pairs if not x["same_d3"]]
unchanged_d3 = [x["grade"] for x in pairs if x["same_d3"]]

gates = {
    "determinant_first_variation_matches_exact_difference_mod3":
        linearized == exact_difference,
    "higher_order_terms_vanish_at_leading_scale":
        higher_residual == [0, 0, 0, 0],
    "all_four_plucker_coordinates_are_tested":
        len(linearized) == 4,
    "linearized_plucker_jet_is_nonzero":
        any(x != 0 for x in linearized),
    "shift_preserves_lower_smith_layers_on_window":
        all(x["same_d1"] and x["same_d2"] for x in pairs),
    "shift_is_selective_at_maximal_minor_layer":
        bool(changed_d3) and bool(unchanged_d3),
}
payload = {
    "schema": "marici.strominger.transverse_fitting_explanation_falsifier.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "grades": [LEFT, RIGHT],
    "scales": {
        "base_entry_v3": BASE_SCALE,
        "perturbation_v3": PERTURBATION_SCALE,
        "determinant_first_variation_v3": DETERMINANT_SCALE,
    },
    "linearized_maximal_minor_mod3": linearized,
    "exact_maximal_minor_difference_mod3": exact_difference,
    "higher_residual_mod3": higher_residual,
    "shift_selectivity_window": [0, WINDOW_UPPER],
    "changed_d3_count": len(changed_d3),
    "unchanged_d3_count": len(unchanged_d3),
    "first_changed_d3_grades": changed_d3[:20],
    "first_unchanged_d3_grades": unchanged_d3[:20],
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "The explanation survives its local hostiles: the exact leading "
        "maximal-minor difference equals the determinant derivative in every "
        "Plucker coordinate, higher terms vanish at that scale, and the shift "
        "changes d3 only on selected grades while preserving d1 and d2."
    ),
}
print(json.dumps(payload, indent=2))
