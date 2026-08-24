"""Exact factorization of the QND record map from earlier source data."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/qnd-record-map-factorization.json"
Matrix = tuple[tuple[F, ...], ...]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] for i in range(len(a))) for j in range(len(a[0])))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
              for j in range(len(b[0])))
        for i in range(len(a))
    )


c, s = F(3, 5), F(4, 5)
unitary: Matrix = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, c, -s),
    (0, 0, s, c),
)

# Prepare pointer |0> in each labelled occurrence.
preparation: Matrix = (
    (1, 0),
    (0, 0),
    (0, 1),
    (0, 0),
)
restrict_left: Matrix = ((1, 0, 0, 0), (0, 1, 0, 0))
restrict_right: Matrix = ((0, 0, 1, 0), (0, 0, 0, 1))

evolved = multiply(unitary, preparation)
left_all = multiply(restrict_left, evolved)
right_all = multiply(restrict_right, evolved)

# The occurrence-labelled diagonal extracts the corresponding costalk column.
record_map: Matrix = (
    (left_all[0][0], right_all[0][1]),
    (left_all[1][0], right_all[1][1]),
)
expected_record_map: Matrix = ((1, c), (0, s))
selected_gram = multiply(transpose(record_map), record_map)

identity4: Matrix = tuple(
    tuple(F(int(i == j)) for j in range(4)) for i in range(4)
)

gates = {
    "controlled_interaction_is_orthogonal": multiply(transpose(unitary), unitary) == identity4,
    "preparation_is_isometric": multiply(transpose(preparation), preparation) == ((1, 0), (0, 1)),
    "labelled_restrictions_recover_record_map": record_map == expected_record_map,
    "wrong_label_costalks_vanish": (
        left_all[0][1] == left_all[1][1] == 0
        and right_all[0][0] == right_all[1][0] == 0
    ),
    "factored_map_selects_source_gram": selected_gram == ((1, c), (c, 1)),
    "exterior_defect_is_derived": (
        selected_gram[0][0] * selected_gram[1][1] - selected_gram[0][1] ** 2
        == s * s
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.qnd-record-map-factorization.v1",
    "factorization": "labelled restriction after controlled interaction after pointer preparation",
    "record_map": [[str(x) for x in row] for row in record_map],
    "selected_gram": [[str(x) for x in row] for row in selected_gram],
    "gates": gates,
    "conclusion": (
        "The QND record map is derived, not primitive: preparation, controlled "
        "interaction, and labelled restriction generate it exactly. Pulling "
        "back the pointer metric then generates the occurrence lens."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
