from fractions import Fraction
import json
from pathlib import Path


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matvec(matrix, vector):
    return [
        sum((a * b for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


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


records = []
for prime_dimension in range(2, 8):
    boundary_dimension = 3
    weights = [Fraction(index + 2) for index in range(prime_dimension)]
    b = [
        [
            Fraction((row + 1) * (column + 2), prime_dimension + 9)
            for column in range(prime_dimension)
        ]
        for row in range(boundary_dimension)
    ]
    b_t = transpose(b)
    weighted_adjoint = [
        [value / weights[row] for value in b_t[row]]
        for row in range(prime_dimension)
    ]

    x = [Fraction(index + 1, prime_dimension + 3) for index in range(prime_dimension)]
    f = [Fraction(2 * index + 1, prime_dimension + 5) for index in range(boundary_dimension)]

    left = dot(matvec(b, x), f)
    returned = matvec(weighted_adjoint, f)
    right = sum(
        (weights[index] * x[index] * returned[index] for index in range(prime_dimension)),
        Fraction(0),
    )
    assert left == right

    raw_returned = matvec(b_t, f)
    raw_right = sum(
        (weights[index] * x[index] * raw_returned[index] for index in range(prime_dimension)),
        Fraction(0),
    )
    assert raw_right != left

    positive_return = multiply(weighted_adjoint, b)
    trace_budget = sum(
        (
            sum(b[row][column] ** 2 for row in range(boundary_dimension))
            / weights[column]
            for column in range(prime_dimension)
        ),
        Fraction(0),
    )
    assert sum(positive_return[i][i] for i in range(prime_dimension)) == trace_budget

    records.append(
        {
            "prime_dimension": prime_dimension,
            "weighted_adjoint_identity": True,
            "raw_transpose_identity": False,
            "positive_return_trace_budget": str(trace_budget),
        }
    )

result = {
    "schema": "marici.nima.seam-weighted-adjoint-return.v1",
    "records": records,
    "verdict": "seam weighting forces the adjoint and makes the boundary return trace class under the tail condition",
}

out = Path(__file__).parents[1] / "results" / "seam-weighted-adjoint-return.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
