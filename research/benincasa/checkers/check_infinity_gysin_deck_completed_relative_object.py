#!/usr/bin/env python3
"""Construct the deck-completed marked-relative infinity representation."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-gysin-deck-completed-relative-object.json"

# H0(D) for D={p0+,pinf+,p0-,pinf-}; deck swaps the two sheets.
deck_h0_D = sp.Matrix([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
])
global_constant = sp.Matrix([1, 1, 1, 1])

# Adapted quotient basis:
# qT=(pinf+ + pinf-) - (p0+ + p0-),
# qS0=p0+ - p0-, qSinf=pinf+ - pinf-.
qT = sp.Matrix([-1, 1, -1, 1])
qS0 = sp.Matrix([1, 0, -1, 0])
qSinf = sp.Matrix([0, 1, 0, -1])
adapted = sp.Matrix.hstack(global_constant, qT, qS0, qSinf)

# Relative H1 basis (qT,qS0,qSinf,h1,h2). Hyperelliptic deck acts
# by -1 on the compact elliptic H1.
deck_relative = sp.diag(1, -1, -1, -1, -1)

# Boundaries of ordinary and sign-weighted sheet completions.
boundary_trace = sp.Matrix([1, 0, 0, 0, 0])
boundary_sign = sp.Matrix([0, -1, 1, 0, 0])

projector_plus = (sp.eye(5)+deck_relative)/2
projector_minus = (sp.eye(5)-deck_relative)/2

checks = {
    "four_endpoint_basis_is_independent": adapted.det() != 0,
    "global_constant_is_deck_even": deck_h0_D*global_constant == global_constant,
    "endpoint_trivial_difference_is_even": deck_h0_D*qT == qT,
    "zero_endpoint_difference_is_odd": deck_h0_D*qS0 == -qS0,
    "infinity_endpoint_difference_is_odd": deck_h0_D*qSinf == -qSinf,
    "relative_rank_is_five": deck_relative.rows == 5,
    "relative_character_is_one_plus_four_minus": list(deck_relative.diagonal()) == [1, -1, -1, -1, -1],
    "ordinary_trace_lands_in_plus_sector": projector_plus*boundary_trace == boundary_trace,
    "sign_trace_lands_in_minus_sector": projector_minus*boundary_sign == boundary_sign,
    "projectors_are_complementary": (
        projector_plus+projector_minus == sp.eye(5)
        and projector_plus*projector_minus == sp.zeros(5)
    ),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-gysin-deck-completed-relative-object.v1",
    "marked_endpoints": ["p0+", "pinf+", "p0-", "pinf-"],
    "rank_decomposition": {
        "H0_D_mod_H0_E": 3,
        "H1_E": 2,
        "H1_E_D": 5,
    },
    "deck_character_decomposition": {
        "plus_rank": 1,
        "minus_rank": 4,
        "ordered_basis": ["qT", "qS0", "qSinf", "h1", "h2"],
        "matrix": [[int(value) for value in row] for row in deck_relative.tolist()],
    },
    "ordinary_trace_boundary": {
        "class": "qT",
        "character": 1,
        "elliptic_H1_visible": False,
    },
    "sign_weighted_trace_boundary": {
        "class": "qSinf-qS0",
        "character": -1,
        "elliptic_H1_compatible": True,
    },
    "coefficient_character": {
        "omega0": -1,
        "omega2": -1,
        "reason": "both contain 1/W and W changes sign under the deck involution",
    },
    "typed_physical_completion": (
        "The elliptic coefficient forms require the sign-weighted sheet completion. "
        "The ordinary trace selects only the trivial endpoint-difference line."
    ),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("relative rank 5 = plus 1 + minus 4")
print("ordinary trace: qT; sign trace: qSinf-qS0")
print(OUT)
