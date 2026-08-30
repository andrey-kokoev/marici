from fractions import Fraction
import json
from pathlib import Path


def amplitude(a: Fraction, b: Fraction, theta: Fraction) -> Fraction:
    return a + theta * b


def weight(a: Fraction, b: Fraction, theta: Fraction) -> Fraction:
    value = amplitude(a, b, theta)
    return value * value


def derivative(a: Fraction, b: Fraction, theta: Fraction) -> Fraction:
    return 2 * amplitude(a, b, theta) * b


def symmetric_difference(
    a: Fraction, b: Fraction, theta: Fraction, h: Fraction
) -> Fraction:
    return (weight(a, b, theta + h) - weight(a, b, theta - h)) / (2 * h)


fixtures = [
    (Fraction(2), Fraction(3), Fraction(1), Fraction(1, 7)),
    (Fraction(-4, 3), Fraction(5, 2), Fraction(2, 5), Fraction(3, 11)),
    (Fraction(7, 5), Fraction(-9, 4), Fraction(-2, 3), Fraction(1, 13)),
]

for fixture in fixtures:
    assert symmetric_difference(*fixture) == derivative(*fixture[:3])

# Exact support-zero hostile: the central ratio is undefined, the first
# derivative vanishes, and the second-order support entry is nonzero.
a = Fraction(1)
b = Fraction(-1)
theta = Fraction(1)
h = Fraction(1, 4)
w_minus = weight(a, b, theta - h)
w_zero = weight(a, b, theta)
w_plus = weight(a, b, theta + h)
d1 = symmetric_difference(a, b, theta, h)
d2 = (w_plus - 2 * w_zero + w_minus) / (h * h)

assert w_zero == 0
assert w_minus == w_plus == Fraction(1, 16)
assert d1 == derivative(a, b, theta) == 0
assert d2 == 2

# The symmetric proposal mixture dominates all three samples without using a
# central-weight denominator.
proposal = w_minus + w_zero + w_plus
r_minus = w_minus / proposal
r_zero = w_zero / proposal
r_plus = w_plus / proposal
proposal_derivative_density = (r_plus - r_minus) / (2 * h)

assert proposal == Fraction(1, 8)
assert (r_minus, r_zero, r_plus) == (Fraction(1, 2), 0, Fraction(1, 2))
assert proposal_derivative_density == 0

result = {
    "schema": "marici.nima.source-response-signed-measure.v1",
    "status": "pass",
    "exact_symmetric_fixtures": len(fixtures),
    "support_zero_hostile": {
        "central_weight": str(w_zero),
        "neighbor_weights": [str(w_minus), str(w_plus)],
        "first_derivative": str(d1),
        "second_derivative": str(d2),
        "central_ratio_defined": False,
    },
    "support_cover": {
        "proposal_mass": str(proposal),
        "densities": [str(r_minus), str(r_zero), str(r_plus)],
        "derivative_density": str(proposal_derivative_density),
    },
}

output = Path(__file__).parents[1] / "results" / "source-response-signed-measure.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
