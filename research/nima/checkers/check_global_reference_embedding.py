import json
from fractions import Fraction
from pathlib import Path


def unit_point(t):
    denominator = 1 + t * t
    return ((1 - t * t) / denominator, 2 * t / denominator)


points = [
    unit_point(Fraction(-2)),
    unit_point(Fraction(-1)),
    unit_point(Fraction(-1, 2)),
    unit_point(Fraction(0)),
    unit_point(Fraction(1, 2)),
    unit_point(Fraction(1)),
    unit_point(Fraction(2)),
]
assert len(set(points)) == len(points)

real_collision = (unit_point(Fraction(1, 2)), unit_point(Fraction(-1, 2)))
imag_collision = (unit_point(Fraction(2)), unit_point(Fraction(1, 2)))
assert real_collision[0] != real_collision[1]
assert real_collision[0][0] == real_collision[1][0]
assert imag_collision[0] != imag_collision[1]
assert imag_collision[0][1] == imag_collision[1][1]

assert len(set((x, y) for x, y in points)) == len(points)

orientation_fiber = [Fraction(-1), Fraction(1)]
assert len(set(orientation_fiber)) == 2

result = {
    "schema": "marici.global-reference-embedding.v1",
    "fiber": "unit_circle",
    "one_real_continuous_coordinate_globally_injective": False,
    "two_quadrature_sample_injective": True,
    "real_quadrature_collision": [
        [str(x) for x in point] for point in real_collision
    ],
    "imaginary_quadrature_collision": [
        [str(x) for x in point] for point in imag_collision
    ],
    "orientation_fiber_scalar_separated": True,
    "verdict": "reference minimization is an embedding problem, not dimension counting",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "global-reference-embedding.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
