from fractions import Fraction
import json
from pathlib import Path


def identity(size):
    return [
        [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]


def add(left, right):
    return [[a + b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def subtract(left, right):
    return [[a - b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def matmul(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def residual(matrix):
    return subtract(identity(len(matrix)), matmul(transpose(matrix), matrix))


j_plus = [
    [Fraction(2), Fraction(0)],
    [Fraction(0), Fraction(1, 2)],
]
j_minus = [
    [Fraction(1, 2), Fraction(0)],
    [Fraction(0), Fraction(2)],
]

assert matmul(j_plus, j_minus) == identity(2)
assert residual(j_plus) != [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
assert residual(j_minus) != [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]

transported_sum = add(
    residual(j_minus),
    matmul(matmul(transpose(j_minus), residual(j_plus)), j_minus),
)
assert transported_sum == [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]

# Determinant reciprocity does not imply operator inversion.
hostile_minus = [
    [Fraction(1), Fraction(1)],
    [Fraction(0), Fraction(1)],
]
hostile_det = hostile_minus[0][0] * hostile_minus[1][1] - hostile_minus[0][1] * hostile_minus[1][0]
assert hostile_det == 1
assert matmul(j_plus, hostile_minus) != identity(2)

result = {
    "local_plus_unitary": False,
    "local_minus_unitary": False,
    "operator_inverse_law": True,
    "round_trip_identity": True,
    "transported_supply_residual": [[str(value) for value in row] for row in transported_sum],
    "determinant_reciprocity_implies_operator_inverse": False,
    "theta_operator_inverse_lift_constructed": False,
    "verdict": "reciprocal inverse sector maps cancel their transported nonunitary supply exactly; scalar gamma reciprocity does not establish the operator law",
}

out = Path(__file__).parents[1] / "results" / "rh-reciprocal-supply-cancellation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
