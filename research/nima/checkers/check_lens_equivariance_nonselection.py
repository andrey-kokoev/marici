"""Exact audit: source equivariance does not uniquely select a lens."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/lens-equivariance-nonselection.json"


def lens(t: F) -> tuple[tuple[F, F], tuple[F, F]]:
    a = (1 + t * t) / (1 - t * t)
    b = 2 * t / (1 - t * t)
    return ((a, b), (b, a))


parameters = tuple(F(n, 10) for n in range(-9, 10))
family = tuple(lens(t) for t in parameters)

gates = {
    "all_are_swap_equivariant": all(
        g[0][0] == g[1][1] and g[0][1] == g[1][0] for g in family
    ),
    "all_preserve_unit_exterior_volume": all(
        g[0][0] * g[1][1] - g[0][1] * g[1][0] == 1 for g in family
    ),
    "all_are_positive": all(
        g[0][0] + g[0][1] > 0 and g[0][0] - g[0][1] > 0 for g in family
    ),
    "equivariant_solution_is_not_unique": len(set(family)) == len(family) > 1,
    "readout_overlap_varies": len(
        {g[0][1] ** 2 / (g[0][0] * g[1][1]) for g in family}
    ) > 1,
    "identity_lens_is_only_one_member": family[parameters.index(F(0))] == ((1, 0), (0, 1)),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.lens-equivariance-nonselection.v1",
    "equations": ["G commutes with swap", "det(G)=1", "G positive"],
    "rational_points_checked": len(family),
    "distinct_overlap_squared": len(
        {g[0][1] ** 2 / (g[0][0] * g[1][1]) for g in family}
    ),
    "gates": gates,
    "conclusion": (
        "Naturality under the declared label swap, positivity, and exterior "
        "normalization leave a one-parameter family. Equivariance validates "
        "a proposed lens but cannot select one."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
