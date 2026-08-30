from fractions import Fraction
import json
from pathlib import Path


def identity(size):
    return [
        [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def bordered(u, y):
    return [
        [Fraction(1), Fraction(0), Fraction(0), u[0]],
        [Fraction(0), Fraction(1), Fraction(0), u[1]],
        [Fraction(0), Fraction(0), Fraction(1), u[2]],
        [y[0], y[1], y[2], Fraction(0)],
    ]


def proposed_inverse(u, y):
    f = dot(y, u)
    assert f != 0
    top_left = [
        [Fraction(int(i == j)) - u[i] * y[j] / f for j in range(3)]
        for i in range(3)
    ]
    return [
        top_left[0] + [u[0] / f],
        top_left[1] + [u[1] / f],
        top_left[2] + [u[2] / f],
        [y[0] / f, y[1] / f, y[2] / f, -Fraction(1) / f],
    ]


samples = [
    ([Fraction(2), Fraction(3), Fraction(5)], [Fraction(1), Fraction(-1), Fraction(2)]),
    ([Fraction(-2), Fraction(7), Fraction(1)], [Fraction(3), Fraction(2), Fraction(-1)]),
]

denominators = []
for u, y in samples:
    f = dot(y, u)
    assert f != 0
    d = bordered(u, y)
    d_inverse = proposed_inverse(u, y)
    assert matmul(d, d_inverse) == identity(4)
    assert matmul(d_inverse, d) == identity(4)
    denominators.append(str(f))

zero_u = [Fraction(0), Fraction(1), Fraction(0)]
zero_y = [Fraction(1), Fraction(0), Fraction(0)]
assert dot(zero_y, zero_u) == 0

result = {
    "inverse_formula_verified_samples": len(samples),
    "sample_readout_denominators": denominators,
    "inverse_common_denominator": "f=y(u)",
    "inverse_defined_at_zero_witness": False,
    "algebraic_inverse_is_noncircular_rh_explanation": False,
    "required_next_object": "source-local parametrix with independently controlled residual",
    "verdict": "the bordered complex gives a forward zero-to-state bridge, but its tautological contraction divides by the RH-bearing readout",
}

out = Path(__file__).parents[1] / "results" / "rh-bordered-inverse-circularity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
