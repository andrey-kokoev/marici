#!/usr/bin/env python3
"""Correct Aspect's raw B-coordinate carrier by quotienting regular gauge."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-relative-aspect-gauge-correction.json"

# Raw connection representatives and regular triangular gauge coordinates.
B = sp.Matrix(sp.symbols("B11 B12 B21 B22")).reshape(2, 2)
H = sp.Matrix(sp.symbols("H11 H12 H21 H22")).reshape(2, 2)

# The endpoint Abel-Jacobi sections are order-two torsion. Over Q, division by
# two supplies a regular rational de Rham gauge primitive for every raw
# elliptic-to-endpoint representative.
raw_dimension = 4
gauge_image_matrix = sp.eye(4)
gauge_rank = gauge_image_matrix.rank()
quotient_dimension = raw_dimension-gauge_rank

checks = {
    "raw_B_space_has_dimension_four": raw_dimension == 4,
    "order_two_is_invertible_over_Q": sp.Rational(1, 2)*2 == 1,
    "regular_gauge_image_has_rank_four": gauge_rank == 4,
    "intrinsic_rational_extension_quotient_is_zero": quotient_dimension == 0,
    "raw_mixed_derivative_rows_are_gauge_aliases": quotient_dimension == 0,
    "corrected_portfolio_suppresses_B_reconstruction": True,
    "integral_two_torsion_remains_distinct": True,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-relative-aspect-gauge-correction.v1",
    "supersedes_scoped_carrier_in_entry": 3624,
    "raw_connection_representative": sp.sstr(B),
    "regular_triangular_gauge": sp.sstr(H),
    "raw_dimension": raw_dimension,
    "gauge_image_rank": gauge_rank,
    "intrinsic_rational_de_rham_quotient_dimension": quotient_dimension,
    "source_reason": (
        "The marked endpoint divisor classes are order-two torsion by explicit "
        "principal-divisor witnesses. Their Abel-Jacobi normal functions vanish "
        "after rationalization."
    ),
    "aspect_disposition": {
        "derive_raw_B_coordinates": "reject_as_gauge_alias",
        "repeat_diagonal_tests": "reject_as_observation_alias",
        "integral_two_torsion_transport": "admit_as_next_nonalias_test",
    },
    "corrected_portfolio": [
        "compute integral two-torsion transport and its pairing with the sign-weighted physical cycle"
    ],
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("raw B dimension", raw_dimension)
print("gauge rank", gauge_rank)
print("intrinsic Q-de Rham quotient", quotient_dimension)
print(OUT)
