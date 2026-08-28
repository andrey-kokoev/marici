#!/usr/bin/env python3
"""Exact deck splitting of the source conductor port on its root cover."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-root-cover-deck-splitting.json"
x, y, z, a, r = sp.symbols("x y z a r", nonzero=True)

C1 = x**2*y+x**2*z+x*y**2+2*x*y*z+2*x*z**2-y**3-y**2*z+y*z**2+z**3
R1 = -x*a**2 + C1
F1 = -(a+z-x)/((a-x-z)*(a+y+2*z)*(y+z-x)*(a-y))

# Entry 3862's physical-sheet sign convention.
source_coefficient = sp.factor(-F1/sp.diff(R1, a))
c_plus = sp.factor(source_coefficient.subs(a, r))
c_minus = sp.factor(source_coefficient.subs(a, -r))
c_even = sp.factor((c_plus+c_minus)/2)
c_odd = sp.factor((c_plus-c_minus)/2)
deck = lambda expression: sp.factor(expression.subs(r, -r))

sample = {x: 2, y: 3, z: 4, r: sp.sqrt(sp.Rational(207, 2))}
checks = {
    "root_cover_equation_nontrivial_at_sample": C1.subs(sample) != 0,
    "deck_exchanges_sheet_coefficients": sp.simplify(deck(c_plus)-c_minus) == 0,
    "even_component_is_deck_invariant": sp.simplify(deck(c_even)-c_even) == 0,
    "odd_component_is_deck_anti_invariant": sp.simplify(deck(c_odd)+c_odd) == 0,
    "positive_sheet_reconstructs_from_even_and_odd": sp.simplify(c_plus-c_even-c_odd) == 0,
    "even_component_is_generically_nonzero": sp.together(c_even).as_numer_denom()[0] != 0,
    "odd_component_is_generically_nonzero": sp.together(c_odd).as_numer_denom()[0] != 0,
    "both_components_nonzero_at_asymmetric_sample": c_even.subs(sample) != 0 and c_odd.subs(sample) != 0,
}
payload = {
    "schema": "marici.rank26-conductor-root-cover-deck-splitting.v1",
    "root_cover": "r^2=C1/x",
    "branch_polynomial": str(C1),
    "sheet_coefficients": {"plus": str(c_plus), "minus": str(c_minus)},
    "deck_components": {"even": str(c_even), "odd": str(c_odd)},
    "sample_2_3_4": {
        "even": str(sp.N(c_even.subs(sample), 16)),
        "odd": str(sp.N(c_odd.subs(sample), 16)),
    },
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The positive-root conductor port has nonzero deck-even and deck-odd parts. Only the even aggregate descends to the base; the source port requires the labelled root-cover projector local system.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
