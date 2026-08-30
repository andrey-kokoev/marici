"""Exact hostile test: bare exterior Carrier does not fix a positive lens."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/carrier-positive-lens-nonuniqueness.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]


def determinant(g: Matrix) -> F:
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def swap_invariant(g: Matrix) -> bool:
    return g[0][0] == g[1][1] and g[0][1] == g[1][0]


def positive_definite(g: Matrix) -> bool:
    return g[0][0] > 0 and determinant(g) > 0


def overlap_squared(g: Matrix) -> F:
    return g[0][1] ** 2 / (g[0][0] * g[1][1])


g_flat: Matrix = ((F(1), F(0)), (F(0), F(1)))
g_squeezed: Matrix = ((F(5, 3), F(4, 3)), (F(4, 3), F(5, 3)))

# Rational one-parameter family with a^2-b^2=1.
parameters = (F(0), F(1, 4), F(1, 3), F(1, 2), F(2, 3))
family: list[Matrix] = []
for t in parameters:
    a = (1 + t * t) / (1 - t * t)
    b = 2 * t / (1 - t * t)
    family.append(((a, b), (b, a)))

gates = {
    "both_lenses_are_positive": positive_definite(g_flat) and positive_definite(g_squeezed),
    "both_preserve_swap": swap_invariant(g_flat) and swap_invariant(g_squeezed),
    "both_have_same_exterior_volume": determinant(g_flat) == determinant(g_squeezed) == 1,
    "readouts_differ": overlap_squared(g_flat) == 0 and overlap_squared(g_squeezed) == F(16, 25),
    "rational_family_preserves_carrier_data": all(
        positive_definite(g) and swap_invariant(g) and determinant(g) == 1 for g in family
    ),
    "family_contains_distinct_readouts": len({overlap_squared(g) for g in family}) == len(family),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.carrier-positive-lens-nonuniqueness.v1",
    "fixed_carrier_data": ["two labels", "label swap", "oriented exterior volume one"],
    "flat_overlap_squared": str(overlap_squared(g_flat)),
    "squeezed_overlap_squared": str(overlap_squared(g_squeezed)),
    "family_overlap_squared": [str(overlap_squared(g)) for g in family],
    "gates": gates,
    "conclusion": (
        "The same labelled exterior Carrier admits a rational family of "
        "swap-invariant positive determinant-one pairings with different "
        "observable overlaps. Carrier data constrains but does not select "
        "the positive coefficient lens."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
