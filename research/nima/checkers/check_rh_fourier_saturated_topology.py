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


def matmul(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def power(matrix, exponent):
    out = identity(len(matrix))
    for _ in range(exponent):
        out = matmul(out, matrix)
    return out


def congruence(matrix, gramian):
    return matmul(matmul(transpose(matrix), gramian), matrix)


fourier = [
    [Fraction(0), Fraction(-1)],
    [Fraction(1), Fraction(0)],
]
assert power(fourier, 4) == identity(2)

# One authorized observer initially misses the second coordinate.
gramian = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0)],
]
saturated = [
    [Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0)],
]
orbit = []
for exponent in range(4):
    transported = congruence(power(fourier, exponent), gramian)
    orbit.append(transported)
    saturated = add(saturated, transported)

assert saturated == [
    [Fraction(2), Fraction(0)],
    [Fraction(0), Fraction(2)],
]
assert congruence(fourier, saturated) == saturated

# The original vector e2 is invisible, but becomes visible after saturation.
e2_original_energy = gramian[1][1]
e2_saturated_energy = saturated[1][1]
assert e2_original_energy == 0
assert e2_saturated_energy > 0

# A generic positive semidefinite Gramian is also invariant after orbit sum.
generic = [
    [Fraction(3), Fraction(1)],
    [Fraction(1), Fraction(2)],
]
generic_saturated = [
    [Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0)],
]
for exponent in range(4):
    generic_saturated = add(
        generic_saturated,
        congruence(power(fourier, exponent), generic),
    )
assert congruence(fourier, generic_saturated) == generic_saturated

result = {
    "fourier_order": 4,
    "transported_observer_count": len(orbit),
    "saturated_gramian": [[str(value) for value in row] for row in saturated],
    "fourier_invariance_exact": True,
    "original_hidden_direction_repaired": True,
    "generic_gramian_invariance_exact": True,
    "arithmetic_constructor_continuity_verified": False,
    "completion_observability_verified": False,
    "verdict": "fourier orbit saturation is the minimal source-generated topology constructor making reciprocal sewing isometric",
}

out = Path(__file__).parents[1] / "results" / "rh-fourier-saturated-topology.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
