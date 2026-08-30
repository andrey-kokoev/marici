from fractions import Fraction
import json
from pathlib import Path


def matrix(a, b, c):
    return [
        [Fraction(1), a + c, a * b],
        [Fraction(0), Fraction(1), b],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]


def matvec(a, x):
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def dot(y, x):
    return sum(v * w for v, w in zip(y, x))


def readout(a, b, c, x, y):
    return dot(y, matvec(matrix(a, b, c), x))


def expanded_readout(a, b, c, x, y):
    constant = y[0] * x[0] + y[1] * x[1] + y[2] * x[2]
    return (
        constant
        + y[0] * x[1] * (a + c)
        + y[0] * x[2] * a * b
        + y[1] * x[2] * b
    )


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
    assert readout(a, b, c, x, y) == expanded_readout(a, b, c, x, y)

e2 = [Fraction(0), Fraction(1), Fraction(0)]
e3 = [Fraction(0), Fraction(0), Fraction(1)]
e1_dual = [Fraction(1), Fraction(0), Fraction(0)]

a = Fraction(2)
b = Fraction(3)
c = Fraction(-2)
assert readout(a, b, c, e2, e1_dual) == a + c == 0
assert readout(a, b, c, e3, e1_dual) == a * b == 6
assert b * (a + c) == a * b + b * c

result = {
    "generic_expansion_verified_samples": len(samples),
    "readout_type": "ordered source-to-endpoint matrix coefficient",
    "basis_readout_e1star_M_e2": "R=a+c",
    "basis_readout_e1star_M_e3": "P=a*b",
    "zero_witness": {"a": "2", "b": "3", "c": "-2", "R": "0", "det_M": "1"},
    "relative_flag_regular_at_zero_witness": True,
    "theta_port_flag_identified": False,
    "verdict": "the theta divisor cannot be assigned to an A2 minor before the ordered source and observer ports are derived",
}

out = Path(__file__).parents[1] / "results" / "rh-ordered-flag-matrix-coefficient.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
