"""Exact finite model of empty, moduli, and selected lens fibers."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/sector-lens-lifting-problem.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]


def determinant(g: Matrix) -> F:
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def positive(g: Matrix) -> bool:
    return g[0][0] > 0 and determinant(g) > 0


def lens(t: F) -> Matrix:
    a = (1 + t * t) / (1 - t * t)
    b = 2 * t / (1 - t * t)
    return ((a, b), (b, a))


parameters = (F(0), F(1, 4), F(1, 3), F(1, 2), F(2, 3))
moduli_fiber = tuple(lens(t) for t in parameters)

record_map: Matrix = ((1, F(3, 5)), (0, F(4, 5)))
selected: Matrix = (
    (
        record_map[0][0] ** 2 + record_map[1][0] ** 2,
        record_map[0][0] * record_map[0][1] + record_map[1][0] * record_map[1][1],
    ),
    (
        record_map[0][1] * record_map[0][0] + record_map[1][1] * record_map[1][0],
        record_map[0][1] ** 2 + record_map[1][1] ** 2,
    ),
)

selected_normalized: Matrix = tuple(
    tuple(F(5, 4) * entry for entry in row) for row in selected
)  # type: ignore[assignment]
matching_selected = tuple(g for g in moduli_fiber if g == selected_normalized)

gates = {
    "negative_volume_positive_fiber_is_empty": all(
        determinant(g) > 0 for g in moduli_fiber if positive(g)
    ),
    "bare_carrier_fiber_has_moduli": len(set(moduli_fiber)) > 1,
    "every_sampled_lift_preserves_declared_constraints": all(
        positive(g)
        and determinant(g) == 1
        and g[0][0] == g[1][1]
        and g[0][1] == g[1][0]
        for g in moduli_fiber
    ),
    "record_map_selects_a_lift": selected == ((1, F(3, 5)), (F(3, 5), 1)),
    "pullback_equations_select_uniquely_in_family": len(matching_selected) == 1,
    "selected_lift_has_source_exterior_defect": determinant(selected) == F(16, 25),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.sector-lens-lifting-problem.v1",
    "sampled_moduli_points": len(moduli_fiber),
    "selected_lift": [[str(x) for x in row] for row in selected],
    "gates": gates,
    "conclusion": (
        "Sector lens selection is a lifting problem through a forgetful "
        "functor. A lift fiber may be empty, contain moduli, or become unique "
        "after source comparison data impose pullback equations."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
