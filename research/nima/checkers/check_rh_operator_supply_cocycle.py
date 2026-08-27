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


j = [
    [Fraction(2), Fraction(0)],
    [Fraction(0), Fraction(1, 2)],
]
assert j[0][0] * j[1][1] == 1
r_j = residual(j)
assert r_j == [
    [Fraction(-3), Fraction(0)],
    [Fraction(0), Fraction(3, 4)],
]

r_positive = [
    [Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(3, 4)],
]
r_negative = [
    [Fraction(3), Fraction(0)],
    [Fraction(0), Fraction(0)],
]
assert subtract(r_positive, r_negative) == r_j
assert add(matmul(transpose(j), j), r_positive) == add(identity(2), r_negative)

pairs = [
    (
        [[Fraction(1), Fraction(1)], [Fraction(0), Fraction(1)]],
        [[Fraction(2), Fraction(0)], [Fraction(1), Fraction(1)]],
    ),
    (
        [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(0)]],
        [[Fraction(3, 2), Fraction(0)], [Fraction(0), Fraction(2, 3)]],
    ),
]

for left, right in pairs:
    product = matmul(left, right)
    cocycle_right = add(
        residual(right),
        matmul(matmul(transpose(right), residual(left)), right),
    )
    assert residual(product) == cocycle_right

result = {
    "determinant_one_hostile": True,
    "hostile_residual": [[str(value) for value in row] for row in r_j],
    "positive_and_negative_supply_required": True,
    "composition_pairs_verified": len(pairs),
    "supply_cocycle": "R(JK)=R(K)+K^*R(J)K",
    "scalar_residual_addition_is_valid_without_transport": False,
    "theta_typed_residual_constructed": False,
    "verdict": "renormalized sewing requires an operator-valued transported supply cocycle, not determinant-one or scalar modulus normalization",
}

out = Path(__file__).parents[1] / "results" / "rh-operator-supply-cocycle.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
