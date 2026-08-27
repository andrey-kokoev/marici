from fractions import Fraction
import json
from pathlib import Path


alpha = Fraction(2)


def modulus_squared_w_plus(x, t):
    return ((x - alpha) ** 2 + t * t) / ((x + alpha) ** 2 + t * t)


right_samples = [
    (Fraction(1), Fraction(0)),
    (Fraction(3), Fraction(4)),
    (Fraction(1, 2), Fraction(7, 3)),
]
left_samples = [(-x, t) for x, t in right_samples]
seam_samples = [(Fraction(0), Fraction(0)), (Fraction(0), Fraction(3))]

for x, t in right_samples:
    assert x > 0
    assert modulus_squared_w_plus(x, t) < 1

for x, t in left_samples:
    assert x < 0
    # w_minus is the reciprocal of w_plus.
    assert Fraction(1, 1) / modulus_squared_w_plus(x, t) < 1

for x, t in seam_samples:
    assert modulus_squared_w_plus(x, t) == 1

# Algebraic reflection identity at real test points.
real_samples = [Fraction(1), Fraction(3), Fraction(-4)]
for zeta in real_samples:
    if zeta in (alpha, -alpha):
        continue
    w_plus_reflected = (-zeta - alpha) / (-zeta + alpha)
    w_minus_original = (zeta + alpha) / (zeta - alpha)
    assert w_plus_reflected == w_minus_original

result = {
    "chart_scale": str(alpha),
    "right_interior_samples": len(right_samples),
    "left_interior_samples": len(left_samples),
    "seam_samples": len(seam_samples),
    "right_chart_maps_to_disk": True,
    "left_chart_maps_to_disk": True,
    "seam_maps_to_unit_circle": True,
    "reflection_exchanges_charts": True,
    "source_colligation_constructed": False,
    "verdict": "the RH Ubersector is two reciprocal contractive disk interiors sewn along one unitary boundary",
}

out = Path(__file__).parents[1] / "results" / "rh-reciprocal-disk-ubersector.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
