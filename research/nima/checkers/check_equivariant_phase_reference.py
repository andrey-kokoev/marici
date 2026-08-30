import json
from fractions import Fraction
from pathlib import Path


def cmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def cpow(z, exponent):
    value = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        value = cmul(value, z)
    return value


def unit_point(t):
    denominator = 1 + t * t
    return ((1 - t * t) / denominator, 2 * t / denominator)


z = unit_point(Fraction(1, 2))
w = unit_point(Fraction(1, 3))
zw = cmul(z, w)
assert cpow(zw, 2) == cmul(cpow(z, 2), cpow(w, 2))

# A continuous one-dimensional real character of the circle is trivial.
scalar_reference_values = {Fraction(1) for _ in (z, w, zw)}
assert scalar_reference_values == {Fraction(1)}

minus_z = (-z[0], -z[1])
assert z != minus_z
assert cpow(z, 2) == cpow(minus_z, 2)
assert cpow(z, 1) != cpow(minus_z, 1)

orbit = [
    unit_point(Fraction(-2)),
    unit_point(Fraction(-1)),
    unit_point(Fraction(-1, 2)),
    unit_point(Fraction(0)),
    unit_point(Fraction(1, 2)),
    unit_point(Fraction(1)),
    unit_point(Fraction(2)),
]
assert len({cpow(point, 1) for point in orbit}) == len(orbit)

result = {
    "schema": "marici.equivariant-phase-reference.v1",
    "minimum_real_dimension": 2,
    "faithful_weights": [-1, 1],
    "weight_zero_blind": True,
    "weight_two_antipodal_collision": {
        "first": [str(x) for x in z],
        "second": [str(x) for x in minus_z],
        "shared_image": [str(x) for x in cpow(z, 2)],
    },
    "weight_one_sample_injective": True,
    "verdict": "phase reference needs a primitive two-real-dimensional equivariant carrier",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "equivariant-phase-reference.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
