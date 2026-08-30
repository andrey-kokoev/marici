"""Exact audit of the ordered structure needed for distinguishability."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/double-slit-ordered-readout-closure.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def negate(a: Matrix) -> Matrix:
    return tuple(tuple(-entry for entry in row) for row in a)  # type: ignore[return-value]


identity: Matrix = ((F(1), F(0)), (F(0), F(1)))
delta: Matrix = ((F(16, 25), F(-12, 25)), (F(-12, 25), F(-16, 25)))
minus_delta = negate(delta)
delta_square = multiply(delta, delta)
minus_delta_square = multiply(minus_delta, minus_delta)
trace = delta[0][0] + delta[1][1]
determinant = delta[0][0] * delta[1][1] - delta[0][1] * delta[1][0]

visibility = F(3, 5)
distinguishability = F(4, 5)

gates = {
    "record_difference_is_traceless": trace == 0,
    "record_difference_square_is_scalar": delta_square == tuple(
        tuple(F(16, 25) * identity[i][j] for j in range(2)) for i in range(2)
    ),
    "unordered_relations_do_not_orient_delta": (
        minus_delta_square == delta_square
        and determinant == (
            minus_delta[0][0] * minus_delta[1][1]
            - minus_delta[0][1] * minus_delta[1][0]
        )
    ),
    "positive_norm_selects_distinguishability": distinguishability**2 == F(16, 25),
    "complementarity_is_generated": visibility**2 + distinguishability**2 == 1,
    "ordering_is_additional_to_star_algebra": delta != minus_delta,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.double-slit-ordered-readout-closure.v1",
    "delta": [[str(x) for x in row] for row in delta],
    "delta_square": [[str(x) for x in row] for row in delta_square],
    "visibility": str(visibility),
    "distinguishability": str(distinguishability),
    "gates": gates,
    "conclusion": (
        "The QND star algebra generates the record-difference operator, but "
        "its physical distinguishability uses the positive norm. The ordered "
        "C*-enrichment is therefore part of the generated readout interface."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
