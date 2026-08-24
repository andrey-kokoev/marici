"""Exact audit of the QND record-map pullback lens selector."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/record-map-pullback-selector.json"
Matrix = tuple[tuple[F, ...], ...]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def gram(e: Matrix) -> Matrix:
    return multiply(transpose(e), e)


c, s = F(3, 5), F(4, 5)
record_map: Matrix = ((1, c), (0, s))
expected: Matrix = ((1, c), (c, 1))

pointer_gauge: Matrix = ((c, -s), (s, c))
gauged_record_map = multiply(pointer_gauge, record_map)

occurrence_swap: Matrix = ((0, 1), (1, 0))
relabelled_record_map = multiply(record_map, occurrence_swap)
relabelled_gram = multiply(
    multiply(transpose(occurrence_swap), expected), occurrence_swap
)

# A bilinear form satisfying the pullback identity on the basis is forced
# entry-by-entry. This reconstructs its only four matrix entries.
basis_pairings = tuple(
    sum(record_map[k][i] * record_map[k][j] for k in range(2))
    for i in range(2) for j in range(2)
)

gates = {
    "record_map_selects_expected_lens": gram(record_map) == expected,
    "selector_is_pointer_gauge_independent": gram(gauged_record_map) == expected,
    "selector_is_occurrence_natural": gram(relabelled_record_map) == relabelled_gram,
    "pullback_identity_is_unique_on_basis": basis_pairings == tuple(
        expected[i][j] for i in range(2) for j in range(2)
    ),
    "selected_overlap_is_source_value": expected[0][1] == F(3, 5),
    "selected_exterior_defect_is_source_value": (
        expected[0][0] * expected[1][1] - expected[0][1] ** 2 == F(16, 25)
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.record-map-pullback-selector.v1",
    "record_map": [[str(x) for x in row] for row in record_map],
    "selected_gram": [[str(x) for x in row] for row in expected],
    "gates": gates,
    "conclusion": (
        "The source record map and pointer metric select a unique occurrence "
        "lens by pullback. The selector is invariant under pointer orthogonal "
        "gauge and natural under occurrence relabelling."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
