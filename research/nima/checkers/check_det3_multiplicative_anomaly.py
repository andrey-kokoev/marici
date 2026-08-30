from fractions import Fraction
import json
from pathlib import Path


def add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def subtract(left, right):
    return [
        [left[i][j] - right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def multiply(left, right):
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right))
        ]
        for i in range(len(left))
    ]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def scale(matrix, scalar):
    return [[scalar * value for value in row] for row in matrix]


def star(left, right):
    return subtract(add(left, right), multiply(left, right))


def regularizer(matrix):
    return trace(matrix) + Fraction(1, 2) * trace(multiply(matrix, matrix))


def anomaly_from_regularizer(left, right):
    return regularizer(star(left, right)) - regularizer(left) - regularizer(right)


def anomaly_formula(left, right):
    left2 = multiply(left, left)
    right2 = multiply(right, right)
    left_right = multiply(left, right)
    return (
        -trace(multiply(left2, right))
        - trace(multiply(left, right2))
        + Fraction(1, 2) * trace(multiply(left_right, left_right))
    )


fixtures = [
    (
        [[Fraction(1, 3), Fraction(1, 5)], [Fraction(2, 7), Fraction(1, 4)]],
        [[Fraction(1, 6), Fraction(3, 8)], [Fraction(1, 9), Fraction(2, 5)]],
        [[Fraction(2, 9), Fraction(1, 7)], [Fraction(3, 10), Fraction(1, 8)]],
    ),
    (
        [[Fraction(0), Fraction(1, 2)], [Fraction(1, 3), Fraction(0)]],
        [[Fraction(1, 5), Fraction(0)], [Fraction(2, 7), Fraction(1, 6)]],
        [[Fraction(1, 4), Fraction(1, 9)], [Fraction(0), Fraction(2, 11)]],
    ),
]

records = []
for index, (a, b, c) in enumerate(fixtures):
    observed = anomaly_from_regularizer(a, b)
    assert observed == anomaly_formula(a, b)
    assert observed != 0

    left_cocycle = observed + anomaly_from_regularizer(star(a, b), c)
    right_cocycle = anomaly_from_regularizer(b, c) + anomaly_from_regularizer(
        a, star(b, c)
    )
    assert left_cocycle == right_cocycle

    assert anomaly_formula(transpose(b), transpose(a)) == observed

    records.append(
        {
            "fixture": index + 1,
            "anomaly": str(observed),
            "strict_multiplicativity": False,
            "two_cocycle_identity": True,
            "dagger_order_reversal": True,
        }
    )

result = {
    "schema": "marici.nima.det3-multiplicative-anomaly.v1",
    "records": records,
    "anomaly_begins_at_total_degree": 3,
    "verdict": "the det3 product residue is a trace-class reciprocal 2-cocycle",
}

out = Path(__file__).parents[1] / "results" / "det3-multiplicative-anomaly.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
