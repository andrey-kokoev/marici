"""Exact audit: an open QND transport needs endpoint comparison data."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/qnd-framed-transport.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]
Vector = tuple[F, F]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def apply(a: Matrix, v: Vector) -> Vector:
    return tuple(sum((a[i][k] * v[k] for k in range(2)), F(0)) for i in range(2))  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def dot(v: Vector, w: Vector) -> F:
    return v[0] * w[0] + v[1] * w[1]


identity: Matrix = ((1, 0), (0, 1))
transport: Matrix = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
p: Vector = (1, 0)
q = apply(transport, p)
original_overlap = dot(p, q)

q_in: Matrix = identity
q_out: Matrix = ((0, -1), (1, 0))
transformed_transport = multiply(multiply(q_out, transport), transpose(q_in))
p_prime = apply(q_in, p)
q_prime = apply(q_out, q)
naive_overlap = dot(p_prime, q_prime)

# The endpoint comparison F transforms contragrediently.
comparison: Matrix = identity
comparison_prime = multiply(multiply(q_in, comparison), transpose(q_out))
framed_overlap = dot(p_prime, apply(comparison_prime, q_prime))

# A common gauge is conjugation and needs no extra endpoint mismatch repair.
common_gauge: Matrix = ((1, 0), (0, -1))
conjugated = multiply(multiply(common_gauge, transport), transpose(common_gauge))
common_p = apply(common_gauge, p)
common_q = apply(common_gauge, q)

gates = {
    "open_transport_obeys_endpoint_gauge_law": (
        apply(transformed_transport, p_prime) == q_prime
    ),
    "naive_open_overlap_is_not_independent_endpoint_gauge_invariant": (
        naive_overlap != original_overlap
    ),
    "framing_restores_overlap_invariance": framed_overlap == original_overlap,
    "common_gauge_preserves_metric_overlap": dot(common_p, common_q) == original_overlap,
    "raw_oriented_component_can_flip": conjugated[1][0] == -transport[1][0],
    "absolute_complementarity_readout_survives_common_gauge": (
        abs(conjugated[0][0]) == F(3, 5) and abs(conjugated[1][0]) == F(4, 5)
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.qnd-framed-transport.v1",
    "original_overlap": str(original_overlap),
    "naive_independent_endpoint_overlap": str(naive_overlap),
    "framed_overlap": str(framed_overlap),
    "gates": gates,
    "conclusion": (
        "The QND interaction is an open transport. Independent endpoint gauge "
        "changes alter a naive overlap; a source endpoint comparison restores "
        "invariance. The selector is a framed transport, not an unframed holonomy."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
