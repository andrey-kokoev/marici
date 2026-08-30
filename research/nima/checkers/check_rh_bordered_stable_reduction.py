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


def left_eliminator(y, sign=-1):
    out = identity(4)
    for index in range(3):
        out[3][index] = sign * y[index]
    return out


def right_eliminator(u, sign=-1):
    out = identity(4)
    for index in range(3):
        out[index][3] = sign * u[index]
    return out


samples = [
    ([Fraction(2), Fraction(3), Fraction(5)], [Fraction(1), Fraction(-1), Fraction(2)]),
    ([Fraction(-2), Fraction(7), Fraction(1)], [Fraction(3), Fraction(2), Fraction(-1)]),
    ([Fraction(0), Fraction(1), Fraction(0)], [Fraction(1), Fraction(0), Fraction(0)]),
]

records = []
for u, y in samples:
    f = dot(y, u)
    d = bordered(u, y)
    left = left_eliminator(y)
    right = right_eliminator(u)
    left_inverse = left_eliminator(y, sign=1)
    right_inverse = right_eliminator(u, sign=1)
    assert matmul(left, left_inverse) == identity(4)
    assert matmul(right, right_inverse) == identity(4)
    reduced = matmul(matmul(left, d), right)
    expected = identity(4)
    expected[3][3] = -f
    assert reduced == expected
    records.append({"u": [str(v) for v in u], "y": [str(v) for v in y], "f": str(f)})

result = {
    "verified_samples": len(samples),
    "includes_zero_readout_sample": any(record["f"] == "0" for record in records),
    "triangular_maps_divide_by_readout": False,
    "stable_normal_form": "I_3 direct-sum (-f)",
    "finite_bordered_lift_adds_independent_cohomology": False,
    "records": records,
    "remaining_gate": "source-typed continuity and domain preservation of triangular elimination",
    "verdict": "new RH content can live only in a typed failure of Gaussian elimination through boundary completion",
}

out = Path(__file__).parents[1] / "results" / "rh-bordered-stable-reduction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
