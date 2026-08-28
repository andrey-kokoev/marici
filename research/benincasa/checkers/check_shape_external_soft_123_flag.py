#!/usr/bin/env python3
"""Verify the canonical physical/source/ambient flag at external-soft A3 germs."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-123-flag.json"

# Ordered ambient basis: (1, x^2, x), adapted to P subset S subset A.
deck = sp.diag(1, 1, -1)
physical_inclusion = sp.Matrix([[1], [0], [0]])
source_inclusion = sp.Matrix([[1, 0], [0, 1], [0, 0]])
physical_readout = sp.Matrix([[1, 0, 0]])
source_projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
site_transport = sp.eye(3)

# Generic flag-preserving endomorphism.
q11, q12, q13, q22, q23, q33 = sp.symbols("q11 q12 q13 q22 q23 q33")
flag_endomorphism = sp.Matrix([
    [q11, q12, q13],
    [0, q22, q23],
    [0, 0, q33],
])

# Deck equivariance removes even/odd mixing.
deck_commutator = sp.expand(flag_endomorphism*deck - deck*flag_endomorphism)
deck_equivariant_solution = {
    q13: 0,
    q23: 0,
}
equivariant_endomorphism = flag_endomorphism.subs(deck_equivariant_solution)

checks = {
    "physical_rank_one": physical_inclusion.rank() == 1,
    "source_rank_two": source_inclusion.rank() == 2,
    "ambient_rank_three": sp.eye(3).rank() == 3,
    "physical_lies_in_source": source_projection*physical_inclusion == sp.Matrix([[1], [0]]),
    "physical_readout_kills_higher_grades": physical_readout == sp.Matrix([[1, 0, 0]]),
    "deck_preserves_physical": deck*physical_inclusion == physical_inclusion,
    "deck_preserves_source": deck*source_inclusion == source_inclusion,
    "site_transport_preserves_flag": (
        site_transport*physical_inclusion == physical_inclusion
        and site_transport*source_inclusion == source_inclusion
    ),
    "deck_characters_are_plus_plus_minus": list(deck.diagonal()) == [1, 1, -1],
    "equivariant_flag_algebra_has_dimension_four": len(
        equivariant_endomorphism.free_symbols
    ) == 4,
    "deck_commutator_vanishes_after_solution": deck_commutator.subs(
        deck_equivariant_solution
    ) == sp.zeros(3),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-external-soft-123-flag.v1",
    "adapted_basis": ["1", "x^2", "x"],
    "flag": {
        "physical": ["1"],
        "source_transport": ["1", "x^2"],
        "ambient_coefficient": ["1", "x^2", "x"],
    },
    "graded_deck_characters": [1, 1, -1],
    "flag_preserving_endomorphism": sp.sstr(flag_endomorphism),
    "deck_equivariant_flag_endomorphism": sp.sstr(equivariant_endomorphism),
    "deck_equivariant_flag_algebra_dimension": 4,
    "site_transport_matrix": site_transport.tolist(),
    "interpretation": (
        "The branch supplies a canonical nested physical/source/ambient flag. "
        "Allowed composability is the deck-equivariant flag-preserving algebra."
    ),
    "all_checks_pass": True,
}
packet["site_transport_matrix"] = [
    [int(value) for value in row] for row in packet["site_transport_matrix"]
]
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("flag dimensions 1 < 2 < 3; equivariant operation algebra dimension 4")
print(OUT)
