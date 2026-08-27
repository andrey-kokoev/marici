from fractions import Fraction
import json
from pathlib import Path


def identity():
    return [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def product(*matrices):
    out = identity()
    for matrix in matrices:
        out = matmul(out, matrix)
    return out


def x1(value):
    out = identity()
    out[0][1] = value
    return out


def x2(value):
    out = identity()
    out[1][2] = value
    return out


def alternate_parameters(a, b, c):
    return b * c / (a + c), a + c, a * b / (a + c)


def braid_holds(a, b, c):
    u, v, w = alternate_parameters(a, b, c)
    return product(x1(a), x2(b), x1(c)) == product(x2(u), x1(v), x2(w))


positive = (Fraction(2), Fraction(3), Fraction(5))
assert braid_holds(*positive)
positive_alternate = alternate_parameters(*positive)
assert all(value > 0 for value in positive)
assert all(value > 0 for value in positive_alternate)

hostile = (Fraction(-2), Fraction(3), Fraction(5))
assert braid_holds(*hostile)
hostile_alternate = alternate_parameters(*hostile)
assert not all(value > 0 for value in hostile)
assert not all(value > 0 for value in hostile_alternate)

hostile_endpoint = product(x1(hostile[0]), x2(hostile[1]), x1(hostile[2]))
assert hostile_endpoint[0][2] == hostile[0] * hostile[1]
assert hostile_endpoint[0][2] < 0

result = {
    "positive_sample": [str(value) for value in positive],
    "positive_alternate_chart": [str(value) for value in positive_alternate],
    "hostile_sample": [str(value) for value in hostile],
    "hostile_alternate_chart": [str(value) for value in hostile_alternate],
    "braid_holds_for_positive_sample": True,
    "braid_holds_for_hostile_sample": True,
    "hostile_negative_generalized_minor": str(hostile_endpoint[0][2]),
    "coherence_implies_positive_chamber": False,
    "verdict": "A2 braid coherence organizes transport presentations but supplies no RH orientation",
}

out = Path(__file__).parents[1] / "results" / "rh-a2-braid-vs-positive-chamber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
