"""Exact rank obstruction for scalar dagger lifts of Ward forms."""

from fractions import Fraction
import json


def matrix_rank(matrix):
    work = [list(row) for row in matrix]
    rows = len(work)
    cols = len(work[0])
    rank = 0
    for col in range(cols):
        pivot = next((row for row in range(rank, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][col]
        work[rank] = [entry / value for entry in work[rank]]
        for row in range(rows):
            if row != rank and work[row][col]:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[rank][j] for j in range(cols)]
        rank += 1
    return rank


rho = (Fraction(1), Fraction(2), Fraction(3))
dagger = tuple(tuple(rho[i] * rho[j] for j in range(3)) for i in range(3))
ward = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)

checks = {
    "scalar_dagger_has_rank_one": matrix_rank(dagger) == 1,
    "prime_two_exclusion_has_rank_two": matrix_rank(ward) == 2,
    "forms_cannot_be_equal": dagger != ward,
    "nonzero_scaling_preserves_dagger_rank": matrix_rank(
        tuple(tuple(Fraction(7, 3) * entry for entry in row) for row in dagger)
    ) == 1,
    "ward_retains_labels_one_and_three": ward[0][0] == ward[2][2] == 1,
}

result = {
    "schema": "marici.grothendieck.scalar-dagger-ward-rank-obstruction.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "labels": [1, 2, 3],
        "scalar_covector": [str(x) for x in rho],
        "dagger_rank": matrix_rank(dagger),
        "ward_rank": matrix_rank(ward),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
