from fractions import Fraction
import json
from pathlib import Path


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    total = Fraction(0)
    for column, value in enumerate(matrix[0]):
        minor = [
            row[:column] + row[column + 1 :]
            for row in matrix[1:]
        ]
        total += (-1 if column % 2 else 1) * value * determinant(minor)
    return total


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def transporter(a, b, c):
    return [
        [Fraction(1), a + c, a * b],
        [Fraction(0), Fraction(1), b],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]


def bordered(u, y):
    return [
        [Fraction(1), Fraction(0), Fraction(0), u[0]],
        [Fraction(0), Fraction(1), Fraction(0), u[1]],
        [Fraction(0), Fraction(0), Fraction(1), u[2]],
        [y[0], y[1], y[2], Fraction(0)],
    ]


samples = [
    (
        Fraction(2),
        Fraction(3),
        Fraction(5),
        [Fraction(1), Fraction(2), Fraction(-1)],
        [Fraction(3), Fraction(-2), Fraction(4)],
    ),
    (
        Fraction(-2),
        Fraction(7),
        Fraction(5),
        [Fraction(0), Fraction(3), Fraction(2)],
        [Fraction(5), Fraction(1), Fraction(-3)],
    ),
]

for a, b, c, x, y in samples:
    u = matvec(transporter(a, b, c), x)
    readout = dot(y, u)
    operator = bordered(u, y)
    assert determinant(operator) == -readout

# Exact zero witness: e2 transported into the R=a+c coordinate and observed
# by e1 dual.
a = Fraction(2)
b = Fraction(3)
c = Fraction(-2)
x = [Fraction(0), Fraction(1), Fraction(0)]
y = [Fraction(1), Fraction(0), Fraction(0)]
u = matvec(transporter(a, b, c), x)
readout = dot(y, u)
operator = bordered(u, y)
kernel_vector = [-value for value in u] + [Fraction(1)]

assert u != [Fraction(0), Fraction(0), Fraction(0)]
assert readout == 0
assert determinant(operator) == 0
assert matvec(operator, kernel_vector) == [Fraction(0)] * 4

# Nearby nonzero witness.
c_nearby = Fraction(-1)
u_nearby = matvec(transporter(a, b, c_nearby), x)
readout_nearby = dot(y, u_nearby)
operator_nearby = bordered(u_nearby, y)
assert readout_nearby == 1
assert determinant(operator_nearby) == -1

result = {
    "carrier_dimension": 3,
    "evaluation_wall_dimension": 1,
    "bordered_operator_dimension": 4,
    "determinant_identity_verified_samples": len(samples) + 2,
    "determinant_identity": "det(D)=-y(Mx)",
    "zero_kernel_generator": [str(value) for value in kernel_vector],
    "zero_to_state_bridge": True,
    "open_sector_contraction_constructed": False,
    "verdict": "the ordered scalar zero is exactly cohomology of a canonical bordered source-forward operator",
}

out = Path(__file__).parents[1] / "results" / "rh-bordered-zero-to-state-lift.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
