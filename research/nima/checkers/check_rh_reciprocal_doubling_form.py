from fractions import Fraction as F
import json
from pathlib import Path


def rank(matrix):
    a = [[F(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(rows):
            if i != pivot_row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
    return pivot_row


positive = [F(1), F(2), F(3)]
doubled = positive + [-x for x in positive]

single_allowed = [(i, j) for i, x in enumerate(positive) for j, y in enumerate(positive) if x + y == 0]
doubled_allowed = [(i, j) for i, x in enumerate(doubled) for j, y in enumerate(doubled) if x + y == 0]

Q = [[F(0) for _ in doubled] for _ in doubled]
for i in range(3):
    Q[i][i + 3] = 1
    Q[i + 3][i] = 1

for i, x in enumerate(doubled):
    for j, y in enumerate(doubled):
        assert (x + y) * Q[i][j] == 0

assert single_allowed == []
assert rank(Q) == 6
assert all(Q[i][i] == 0 for i in range(6))

result = {
    "schema": "marici.rh-reciprocal-doubling-form.v1",
    "positive_spectrum": ["1", "2", "3"],
    "single_sector_allowed_form_entries": 0,
    "doubled_spectrum": ["1", "2", "3", "-1", "-2", "-3"],
    "doubled_allowed_form_entries": len(doubled_allowed),
    "canonical_symmetric_cross_form_rank": rank(Q),
    "preservation_equation": "D^T Q+QD=0",
    "individual_sector_vectors_are_null": True,
    "form_is_positive_definite": False,
    "conclusion": "reciprocal_doubling_is_forced_but_does_not_orient_scalar_readout",
}

out = Path(__file__).parents[1] / "results" / "rh-reciprocal-doubling-form.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
