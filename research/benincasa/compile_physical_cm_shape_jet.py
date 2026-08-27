#!/usr/bin/env python3
"""Exact physical second-shape jet of the labelled Cayley--Menger twist."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/benincasa/results/physical-cm-shape-jet.json"

a, b, c, t = sp.symbols("a b c t")
P1, P2, P3 = 1 + t, 1 - t, sp.Integer(1)
cm = sp.Matrix([
    [0, 1, 1, 1, 1],
    [1, 0, c**2, a**2, b**2],
    [1, c**2, 0, P2**2, P1**2],
    [1, a**2, P2**2, 0, P3**2],
    [1, b**2, P1**2, P3**2, 0],
])
K = sp.expand(-cm.det() / 2)
K0 = sp.factor(K.subs(t, 0))
K1 = sp.factor(sp.diff(K, t).subs(t, 0))
K2 = sp.factor(sp.diff(K, t, 2).subs(t, 0))

swap = {a: b, b: a}
checks = {
    "K0_is_exchange_even": sp.expand(K0.xreplace(swap) - K0) == 0,
    "K1_is_exchange_odd": sp.expand(K1.xreplace(swap) + K1) == 0,
    "K2_is_exchange_even": sp.expand(K2.xreplace(swap) - K2) == 0,
    "K1_has_antisymmetric_edge_factor": sp.rem(K1, a**2 - b**2, a) == 0,
    "K2_is_nonzero": K2 != 0,
    "determinant_degree_is_six": sp.Poly(K, a, b, c, t).total_degree() == 6,
}
assert all(checks.values()), checks

packet = {
    "schema": "marici.physical-cm-shape-jet.v1",
    "cayley_menger_order": ["loop", "vertex3", "vertex1", "vertex2"],
    "shape_family": ["P1=1+t", "P2=1-t", "P3=1"],
    "K0": sp.sstr(K0),
    "K1": sp.sstr(K1),
    "K2": sp.sstr(K2),
    "k1": sp.sstr(sp.factor(K1 / K0)),
    "k2": sp.sstr(sp.factor(K2 / K0)),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("K1 =", K1)
print("K2 =", K2)

