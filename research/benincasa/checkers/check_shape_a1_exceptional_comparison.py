#!/usr/bin/env python3
"""Resolve one cyclic A1 germ and compute its exceptional incidence cone."""

import json
from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-a1-exceptional-comparison.json"

X, Y, Z, W = sp.symbols("X Y Z W")
Q = (9*X**2 - 30*X*Y + 6*X*Z + 9*Y**2 + 6*Y*Z + Z**2) / 4
F = sp.expand(W**2 - Q)
hessian = sp.hessian(F, (X, Y, Z, W))

# The retained marked intersection X=Y=0 on the exceptional quadric is
# W^2=Z^2/4, hence two rational projective points.
points = {
    "plus": [0, 0, 1, Fraction(1, 2)],
    "minus": [0, 0, 1, Fraction(-1, 2)],
}

# H^0(E)=Q because the smooth exceptional quadric is connected. Restriction
# to the two-point incidence locus is the diagonal map Q -> Q^2.
restriction = sp.Matrix([[1], [1]])
conductor = sp.Matrix([[1, -1]])
deck = sp.Matrix([[0, 1], [1, 0]])
source_vector = sp.Matrix([sp.Rational(-17, 6), sp.Rational(17, 6)])
source_boundary = (conductor * source_vector)[0]

checks = {
    "exceptional_quadric_is_nondegenerate": hessian.det() != 0,
    "plus_point_lies_on_exceptional_quadric": F.subs(dict(zip((X, Y, Z, W), points["plus"]))) == 0,
    "minus_point_lies_on_exceptional_quadric": F.subs(dict(zip((X, Y, Z, W), points["minus"]))) == 0,
    "deck_swaps_the_two_points": deck * sp.Matrix([1, 0]) == sp.Matrix([0, 1]),
    "constant_restriction_has_rank_one": restriction.rank() == 1,
    "incidence_cokernel_has_rank_one": 2 - restriction.rank() == 1,
    "conductor_kills_diagonal_image": conductor * restriction == sp.zeros(1, 1),
    "conductor_is_deck_odd": conductor * deck == -conductor,
    "source_class_maps_to_known_obstruction": source_boundary == -sp.Rational(17, 3),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-a1-exceptional-comparison.v1",
    "blowup": "ordinary blowup of (x,y,z,w) at the A1 origin",
    "exceptional_divisor": "W^2=Q(X,Y,Z) in P3",
    "exceptional_hessian_determinant": sp.sstr(hessian.det()),
    "marked_exceptional_points": {key: [str(value) for value in point] for key, point in points.items()},
    "restriction_matrix_H0_E_to_H0_points": [[1], [1]],
    "exceptional_incidence_cokernel_rank": 1,
    "cokernel_character": -1,
    "source_vector": ["-17/6", "17/6"],
    "source_cokernel_value": "-17/3",
    "matches_conductor_obstruction": True,
    "scope": "degree-zero exceptional marked-incidence block; not the full cohomology of the exceptional quadric",
    "physical_selector_value": 0,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("exceptional incidence cokernel: rank 1, odd, source value", source_boundary)
print(OUT)
