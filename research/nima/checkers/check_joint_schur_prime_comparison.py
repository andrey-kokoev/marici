from fractions import Fraction
import json
from pathlib import Path


def identity(n):
    return [
        [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


def add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def subtract(left, right):
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def multiply(left, right):
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def determinant(matrix):
    work = [row[:] for row in matrix]
    value = Fraction(1)
    n = len(work)
    for column in range(n):
        pivot = next((r for r in range(column, n) if work[r][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for j in range(column, n):
            work[column][j] /= pivot_value
        for r in range(column + 1, n):
            factor = work[r][column]
            for j in range(column, n):
                work[r][j] -= factor * work[column][j]
    return value


def nilpotent_inverse_i_minus(a):
    n = len(a)
    result = identity(n)
    current = identity(n)
    for _ in range(1, n):
        current = multiply(current, a)
        result = add(result, current)
    assert multiply(subtract(identity(n), a), result) == identity(n)
    return result


def block_matrix(a, b, c, l):
    top = [a[i] + b[i] for i in range(len(a))]
    bottom = [c[i] + l[i] for i in range(len(c))]
    return top + bottom


records = []
for boundary_dimension in range(2, 7):
    prime_dimension = 2
    a = [
        [Fraction(1 if j == i + 1 else 0) for j in range(boundary_dimension)]
        for i in range(boundary_dimension)
    ]
    b = [
        [
            Fraction((i + 1) * (j + 2), boundary_dimension + 7)
            for j in range(prime_dimension)
        ]
        for i in range(boundary_dimension)
    ]
    c = [
        [
            Fraction((i + 2) * (j + 1), boundary_dimension + 11)
            for j in range(boundary_dimension)
        ]
        for i in range(prime_dimension)
    ]
    l = [
        [Fraction(1, 3) if i == j == 0 else Fraction(1, 5) if i == j else Fraction(0)
         for j in range(prime_dimension)]
        for i in range(prime_dimension)
    ]

    joint = block_matrix(a, b, c, l)
    i_minus_joint = subtract(identity(boundary_dimension + prime_dimension), joint)
    inverse_boundary = nilpotent_inverse_i_minus(a)
    r = multiply(multiply(c, inverse_boundary), b)
    schur = subtract(subtract(identity(prime_dimension), l), r)

    left = determinant(i_minus_joint)
    right = determinant(subtract(identity(boundary_dimension), a)) * determinant(schur)
    assert left == right

    diagonal_only = (1 - l[0][0] - r[0][0]) * (1 - l[1][1] - r[1][1])
    cross_correction = r[0][1] * r[1][0]
    assert cross_correction != 0
    assert determinant(schur) == diagonal_only - cross_correction
    assert determinant(schur) != diagonal_only

    records.append(
        {
            "boundary_dimension": boundary_dimension,
            "schur_identity_exact": True,
            "cross_prime_correction": str(cross_correction),
            "local_product_equals_joint_determinant": False,
        }
    )

result = {
    "schema": "marici.nima.joint-schur-prime-comparison.v1",
    "records": records,
    "verdict": "cross-prime comparison is one joint Schur determinant, not a product of local corrections",
}

out = Path(__file__).parents[1] / "results" / "joint-schur-prime-comparison.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
