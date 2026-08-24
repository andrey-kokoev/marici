"""Exact audit: a degenerate pullback lens canonically descends to a quotient."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/degenerate-lens-quotient.json"
Vector = tuple[F, F]
Matrix = tuple[tuple[F, F], tuple[F, F]]


record_map: Matrix = ((1, 1), (0, 0))
gram: Matrix = ((1, 1), (1, 1))
kernel_generator: Vector = (1, -1)


def apply(a: Matrix, v: Vector) -> Vector:
    return (
        a[0][0] * v[0] + a[0][1] * v[1],
        a[1][0] * v[0] + a[1][1] * v[1],
    )


def determinant(a: Matrix) -> F:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def quotient_coordinate(v: Vector) -> F:
    return v[0] + v[1]


representatives = tuple((F(1) + t, -t) for t in range(-4, 5))
image_values = tuple(apply(record_map, v) for v in representatives)
quotient_values = tuple(quotient_coordinate(v) for v in representatives)

gates = {
    "pullback_is_degenerate": determinant(gram) == 0,
    "record_kernel_equals_lens_kernel": (
        apply(record_map, kernel_generator) == (0, 0)
        and apply(gram, kernel_generator) == (0, 0)
    ),
    "quotient_coordinate_kills_kernel": quotient_coordinate(kernel_generator) == 0,
    "representative_independence_is_exact": len(set(image_values)) == 1,
    "quotient_metric_is_positive": len(set(quotient_values)) == 1 and quotient_values[0] ** 2 > 0,
    "boundary_readout_is_full_visibility_zero_distinguishability": (
        gram[0][1] == 1 and determinant(gram) == 0
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.degenerate-lens-quotient.v1",
    "record_map": [[str(x) for x in row] for row in record_map],
    "pullback_gram": [[str(x) for x in row] for row in gram],
    "kernel_generator": [str(x) for x in kernel_generator],
    "quotient_dimension": 1,
    "gates": gates,
    "conclusion": (
        "At coincident records the full occurrence pullback is semidefinite, "
        "not inconsistent. Its radical is the source record kernel, and the "
        "metric descends canonically to a positive one-dimensional quotient."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
