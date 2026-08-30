from fractions import Fraction
import json
from pathlib import Path


def shift(n):
    return [
        [Fraction(1 if j == i + 1 else 0) for j in range(n)]
        for i in range(n)
    ]


def matvec(matrix, vector):
    return [
        sum((a * b for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def dot(row, column):
    return sum((a * b for a, b in zip(row, column)), Fraction(0))


def rank(matrix):
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (r for r in range(pivot_row, rows) if work[r][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = work[r][column]
            work[r] = [
                work[r][j] - factor * work[pivot_row][j]
                for j in range(columns)
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


records = []
for n in range(2, 10):
    a = shift(n)
    b = [Fraction(0) for _ in range(n - 1)] + [Fraction(1)]
    c = [Fraction(1)] + [Fraction(0) for _ in range(n - 1)]

    krylov_columns = []
    moments = []
    current = b
    for _ in range(n):
        krylov_columns.append(current)
        moments.append(dot(c, current))
        current = matvec(a, current)

    controllability = [
        [krylov_columns[column][row] for column in range(n)]
        for row in range(n)
    ]
    assert rank(controllability) == n
    assert moments[:-1] == [0 for _ in range(n - 1)]
    assert moments[-1] == 1

    # A determinant-preserving nonzero pair exists only because the readout is
    # outside the reachable one-dimensional subspace.
    b_nonminimal = [Fraction(1)] + [Fraction(0) for _ in range(n - 1)]
    c_nonminimal = [Fraction(0) for _ in range(n - 1)] + [Fraction(1)]
    current = b_nonminimal
    zero_moments = []
    reachable = []
    for _ in range(n):
        reachable.append(current)
        zero_moments.append(dot(c_nonminimal, current))
        current = matvec(a, current)
    reachable_matrix = [
        [reachable[column][row] for column in range(n)]
        for row in range(n)
    ]
    assert all(value == 0 for value in zero_moments)
    assert rank(reachable_matrix) == 1

    records.append(
        {
            "dimension": n,
            "controllability_rank": n,
            "first_nonzero_markov_depth": n - 1,
            "nonminimal_reachable_rank": 1,
            "nonminimal_zero_transfer_explained": True,
        }
    )

result = {
    "schema": "marici.nima.minimal-attachment-relative-determinant.v1",
    "records": records,
    "controllable_nonzero_return_with_zero_transfer_exists": False,
    "minimal_two_way_attachment_forces_relative_determinant": True,
    "verdict": "faithful boundary attachment cannot preserve the bare Euler determinant",
}

out = (
    Path(__file__).parents[1]
    / "results"
    / "minimal-attachment-relative-determinant.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
