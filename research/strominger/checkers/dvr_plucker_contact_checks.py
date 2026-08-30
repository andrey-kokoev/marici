#!/usr/bin/env python3
"""Exact checks for the DVR Pluecker-contact lemma and magnetic fixture."""

from __future__ import annotations

import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
LOCALIZATION = ROOT / "research/strominger/checkers/period_729_layer_localization.py"
with contextlib.redirect_stdout(io.StringIO()):
    local = runpy.run_path(str(LOCALIZATION))

layers = local["layers"]
det = local["det"]
P = 3
LEFT, RIGHT = 152, 881
ENTRY_DEPTH, PERTURBATION_DEPTH = 2, 7
JET_DEPTH = 2 * ENTRY_DEPTH + PERTURBATION_DEPTH


def row_minors(a):
    return [
        [[a[i][j] for j in range(3)] for i in rows]
        for rows in itertools.combinations(range(4), 3)
    ]


def replace_columns(base, delta, chosen):
    return [
        [delta[i][j] if j in chosen else base[i][j] for j in range(3)]
        for i in range(3)
    ]


left = layers(LEFT)["full"]
right = layers(RIGHT)["full"]
base = [[x // P**ENTRY_DEPTH for x in row] for row in left]
direction = [
    [(y - x) // P**PERTURBATION_DEPTH for x, y in zip(lrow, rrow)]
    for lrow, rrow in zip(left, right)
]

coordinates = []
for b, h, m, mp in zip(
    row_minors(base), row_minors(direction), row_minors(left), row_minors(right)
):
    one = sum(det(replace_columns(b, h, {j})) for j in range(3))
    two = sum(
        det(replace_columns(b, h, set(js)))
        for js in itertools.combinations(range(3), 2)
    )
    three = det(h)
    exact_difference = det(mp) - det(m)
    reconstructed = (
        P**JET_DEPTH * one
        + P**(ENTRY_DEPTH + 2 * PERTURBATION_DEPTH) * two
        + P**(3 * PERTURBATION_DEPTH) * three
    )
    leading_left = det(m) // P**JET_DEPTH
    coordinates.append({
        "leading_left_mod3": leading_left % P,
        "first_variation_mod3": one % P,
        "leading_sum_mod3": (leading_left + one) % P,
        "exact_multilinear_identity": exact_difference == reconstructed,
        "two_direction_terms_are_higher":
            ENTRY_DEPTH + 2 * PERTURBATION_DEPTH > JET_DEPTH,
        "three_direction_terms_are_higher":
            3 * PERTURBATION_DEPTH > JET_DEPTH,
    })

benincasa_path = ROOT / "research/benincasa/gauge-fitting-conic-transverse-jet.json"
benincasa = json.loads(benincasa_path.read_text(encoding="utf-8"))

gates = {
    "multilinear_expansion_exact_in_every_chart": all(
        x["exact_multilinear_identity"] for x in coordinates
    ),
    "higher_direction_terms_cannot_affect_leading_jet": all(
        x["two_direction_terms_are_higher"]
        and x["three_direction_terms_are_higher"]
        for x in coordinates
    ),
    "magnetic_leading_section_is_nonzero": any(
        x["leading_left_mod3"] for x in coordinates
    ),
    "magnetic_first_variation_is_nonzero": any(
        x["first_variation_mod3"] for x in coordinates
    ),
    "magnetic_first_variation_cancels_complete_section": all(
        x["leading_sum_mod3"] == 0 for x in coordinates
    ),
    "benincasa_fixture_is_reduced_rank_drop_one":
        benincasa["rank_drop_one_count"] == benincasa["tested_fibers"],
    "benincasa_fixture_has_nonzero_normal_pairing":
        benincasa["nonzero_pairing_count"] == benincasa["tested_fibers"],
}
payload = {
    "schema": "marici.strominger.dvr_plucker_contact_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "magnetic_fixture": {
        "prime": P,
        "grades": [LEFT, RIGHT],
        "entry_depth": ENTRY_DEPTH,
        "perturbation_depth": PERTURBATION_DEPTH,
        "first_variation_depth": JET_DEPTH,
        "coordinates": coordinates,
    },
    "benincasa_comparison": {
        "source_schema": benincasa["schema"],
        "tested_fibers": benincasa["tested_fibers"],
        "rank_drop_one_count": benincasa["rank_drop_one_count"],
        "nonzero_pairing_count": benincasa["nonzero_pairing_count"],
        "typed_relation": "analogy_only_no_source_functor",
    },
    "classification": {
        "benincasa": "reduced_rank_locus_crossing",
        "magnetic": "nonreduced_arithmetic_fitting_contact",
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
}
print(json.dumps(payload, indent=2))
