#!/usr/bin/env python3
"""Restrict the four ambient external-soft A3 germs to the source CM contour."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-a3-physical-diagonal.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K
P1, P2 = 1 + t, 1 - t


def triangle_cm(x, y, p):
    matrix = sp.Matrix([
        [0, 1, 1, 1],
        [1, 0, x**2, y**2],
        [1, x**2, 0, p**2],
        [1, y**2, p**2, 0],
    ])
    return sp.factor(-matrix.det())


minor_p2 = sp.factor(triangle_cm(c, a, P2).subs(t, 1))
minor_p1 = sp.factor(triangle_cm(c, b, P1).subs(t, -1))

x = sp.symbols("x")
points = [
    ("t=1:b=1", {t: 1, b: 1, a: x, c: x}, "a=c"),
    ("t=1:b=2", {t: 1, b: 2, a: x, c: x}, "a=c"),
    ("t=-1:a=1", {t: -1, a: 1, b: x, c: x}, "b=c"),
    ("t=-1:a=2", {t: -1, a: 2, b: x, c: x}, "b=c"),
]

records = {}
checks = {
    "P2_zero_triangle_minor_is_square": sp.factor(minor_p2 / (a**2-c**2)**2).is_number,
    "P1_zero_triangle_minor_is_square": sp.factor(minor_p1 / (b**2-c**2)**2).is_number,
}
for label, substitution, diagonal in points:
    restricted = sp.factor(K.subs(substitution))
    derivative = sp.factor(sp.diff(restricted, x))
    records[label] = {
        "source_forced_diagonal": diagonal,
        "restricted_polynomial": sp.sstr(restricted),
        "restricted_jacobian_generator": sp.sstr(derivative),
        "restricted_local_algebra": "Q[x]/(x)",
        "restricted_milnor_rank": 1,
        "ambient_milnor_rank": 3,
        "physical_excess_rank": 0,
    }
    checks[f"{label}:restricted_germ_is_exactly_9x2"] = sp.factor(restricted - 9*x**2) == 0
    checks[f"{label}:restricted_jacobian_is_linear"] = sp.factor(derivative - 18*x) == 0

assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-external-soft-a3-physical-diagonal.v1",
    "triangle_minor_at_P2_zero": sp.sstr(minor_p2),
    "triangle_minor_at_P1_zero": sp.sstr(minor_p1),
    "nonnegative_length_consequence": {
        "P2=0": "a=c",
        "P1=0": "b=c",
    },
    "records": records,
    "classification": (
        "The A3 enhancements are ambient coefficient germs. The source CM contour "
        "meets each along a forced diagonal on which the germ is Morse of rank one."
    ),
    "physical_odd_A3_activation": False,
    "new_carrier_component": False,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
for label, record in records.items():
    print(label, record["source_forced_diagonal"], record["restricted_polynomial"])
print(OUT)
