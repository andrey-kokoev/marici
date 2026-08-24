"""Exact audit: planar QND overlap is independent of pointer preparation."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/qnd-preparation-independence.json"

c, s = F(3, 5), F(4, 5)
parameters = (F(-3, 4), F(-1, 2), F(0), F(1, 3), F(1, 2), F(4, 5))


def pointer(t: F) -> tuple[F, F]:
    return (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)


def rotate(p: tuple[F, F]) -> tuple[F, F]:
    return c * p[0] - s * p[1], s * p[0] + c * p[1]


def dot(p: tuple[F, F], q: tuple[F, F]) -> F:
    return p[0] * q[0] + p[1] * q[1]


states = tuple(pointer(t) for t in parameters)
overlaps = tuple(dot(p, rotate(p)) for p in states)
areas = tuple(p[0] * rotate(p)[1] - p[1] * rotate(p)[0] for p in states)

gates = {
    "all_preparations_are_normalized": all(dot(p, p) == 1 for p in states),
    "all_overlaps_equal_rotation_cosine": all(value == c for value in overlaps),
    "all_oriented_areas_equal_rotation_sine": all(value == s for value in areas),
    "all_selected_grams_are_identical": len(set(overlaps)) == 1,
    "complementarity_is_preparation_independent": all(
        overlap * overlap + area * area == 1
        for overlap, area in zip(overlaps, areas)
    ),
    "multiple_distinct_preparations_were_tested": len(set(states)) == len(states) > 1,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.qnd-preparation-independence.v1",
    "preparations_tested": len(states),
    "common_overlap": str(overlaps[0]),
    "common_oriented_area": str(areas[0]),
    "gates": gates,
    "conclusion": (
        "For the planar controlled rotation, every normalized pointer "
        "preparation yields the same Gram lens. The numerical point is "
        "selected by the interaction rotation, not the prepared pointer ray."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
