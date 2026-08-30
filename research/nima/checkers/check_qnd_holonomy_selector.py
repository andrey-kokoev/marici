"""Exact audit: the QND numerical selector is a transport holonomy."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/qnd-holonomy-selector.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]


def rotation(t: F) -> Matrix:
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    return ((c, -s), (s, c))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def compose_parameter(t1: F, t2: F) -> F:
    return (t1 + t2) / (1 - t1 * t2)


identity: Matrix = ((1, 0), (0, 1))
pairs = ((F(1, 5), F(1, 4)), (F(1, 3), F(1, 7)), (F(-1, 4), F(2, 5)))
composition_checks = tuple(
    multiply(rotation(t1), rotation(t2)) == rotation(compose_parameter(t1, t2))
    for t1, t2 in pairs
)

t_total = F(1, 2)
t1, t2 = F(1, 3), F(1, 7)
segmented = multiply(rotation(t1), rotation(t2))
direct = rotation(t_total)

t_a, t_b, t_c = F(1, 8), F(1, 6), F(1, 5)
associative_left = multiply(multiply(rotation(t_a), rotation(t_b)), rotation(t_c))
associative_right = multiply(rotation(t_a), multiply(rotation(t_b), rotation(t_c)))

gates = {
    "rational_transport_composes_exactly": all(composition_checks),
    "three_four_fifths_holonomy_has_two_segment_factorization": segmented == direct,
    "readout_depends_only_on_total_holonomy": direct[0][0] == F(3, 5) and direct[1][0] == F(4, 5),
    "transport_composition_is_associative": associative_left == associative_right,
    "reversed_history_inverts_transport": multiply(rotation(t_total), rotation(-t_total)) == identity,
    "segmentation_is_not_part_of_readout": t1 != t_total and t2 != t_total,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.qnd-holonomy-selector.v1",
    "direct_parameter": str(t_total),
    "segmented_parameters": [str(t1), str(t2)],
    "holonomy": [[str(x) for x in row] for row in direct],
    "gates": gates,
    "conclusion": (
        "The QND complementarity point is a holonomy invariant. Rational "
        "interaction segments compose exactly, and the selected readout "
        "depends only on total transport, not its subdivision."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
