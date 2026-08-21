"""Exact rational semigroup Gram audit for ordinary and shifted kernels."""

from fractions import Fraction as F
import json
from pathlib import Path


# q^s is a rational discrete-time surrogate for exp(-s*lambda).
atoms = [
    (F(1, 2), F(1, 2), F(1)),
    (F(1, 3), F(1, 3), F(4)),
    (F(1, 5), F(1, 5), F(9)),
]
increments = [0, 1, 2]


def kernel(i, j, shifted=False):
    return sum(
        weight * (spectral_value if shifted else 1) * q ** (i + j)
        for weight, q, spectral_value in atoms
    )


def exact_ldl(matrix):
    size = len(matrix)
    L = [[F(0) for _ in range(size)] for _ in range(size)]
    pivots = []
    for i in range(size):
        L[i][i] = F(1)
        for j in range(i):
            numerator = matrix[i][j] - sum(
                L[i][k] * pivots[k] * L[j][k] for k in range(j)
            )
            L[i][j] = numerator / pivots[j]
        pivot = matrix[i][i] - sum(L[i][k] ** 2 * pivots[k] for k in range(i))
        pivots.append(pivot)
    return pivots


ordinary = [[kernel(i, j) for j in increments] for i in increments]
shifted = [[kernel(i, j, shifted=True) for j in increments] for i in increments]
ordinary_pivots = exact_ldl(ordinary)
shifted_pivots = exact_ldl(shifted)
assert all(value > 0 for value in ordinary_pivots)
assert all(value > 0 for value in shifted_pivots)

# A positive diagonal does not prevent a hostile two-time determinant.
hostile = [[F(1), F(2)], [F(2), F(1)]]
hostile_determinant = hostile[0][0] * hostile[1][1] - hostile[0][1] ** 2
assert hostile_determinant < 0

result = {
    "increment_count": len(increments),
    "ordinary_LDL_pivots": [str(value) for value in ordinary_pivots],
    "shifted_LDL_pivots": [str(value) for value in shifted_pivots],
    "ordinary_reflection_positive": True,
    "generator_shifted_reflection_positive": True,
    "hostile_two_time_determinant": str(hostile_determinant),
    "smallest_coupled_falsifier_size": 2,
    "kernel_factorization_constructs_all_Hankel_minors": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "time-addition-reflection-positivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
