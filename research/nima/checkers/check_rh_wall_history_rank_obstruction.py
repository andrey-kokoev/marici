"""Exact correction: coefficient rank is not analytic multiplication rank."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


# The constant wall is one coefficient feature.
coefficient_gram = [[Fraction(1)]]
assert rank(coefficient_gram) == 1

records = []
for n in range(2, 7):
    # Mult(-1) acts as -I on an n-dimensional analytic truncation.
    multiplication_operator = [
        [Fraction(-1 if i == j else 0) for j in range(n)] for i in range(n)
    ]
    represented_gram = identity(n)  # Mult(-1)^* Mult(-1)
    assert rank(multiplication_operator) == n
    assert represented_gram == identity(n)
    assert rank(represented_gram) == n
    records.append(
        {
            "analytic_dimension": n,
            "coefficient_feature_count": 1,
            "coefficient_gram_rank": 1,
            "multiplication_operator_rank": n,
            "represented_gram_rank": n,
            "represented_gram_is_identity": True,
        }
    )

payload = {
    "schema": "marici.research.check.v1",
    "claim": "a one-feature constant wall represents as the full analytic identity under multiplication",
    "exact_arithmetic": "fractions.Fraction",
    "records": records,
    "retracted_model": "conjugating a rank-one state-space projector",
    "correct_functor": "scalar coefficient to multiplication operator",
    "relative_completion_identity_proved": False,
    "g1_1_closed": False,
    "verdict": "the rank obstruction is rejected; relative Green extension remains open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-wall-history-rank-obstruction.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
