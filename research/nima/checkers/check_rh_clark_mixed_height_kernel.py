from fractions import Fraction
import json
from pathlib import Path


def conjugate(value):
    return value.conjugate() if hasattr(value, "conjugate") else value


def inner(left, right):
    return sum(conjugate(a) * b for a, b in zip(left, right))


def add(left, right):
    return [a + b for a, b in zip(left, right)]


def scale(value, vector):
    return [value * entry for entry in vector]


# Rational real features are sufficient for an exact polarization check; the
# sheet coefficient is represented symbolically by the pair (X,Y).
features = [
    ([Fraction(1), Fraction(2)], [Fraction(3), Fraction(-1)]),
    ([Fraction(-2), Fraction(1)], [Fraction(0), Fraction(4)]),
    ([Fraction(3), Fraction(0)], [Fraction(-1), Fraction(2)]),
]


def clark_kernel(left, right):
    x_left, y_left = left
    x_right, y_right = right
    return 2 * inner(x_left, x_right) + 2 * inner(y_left, y_right)


gram = [
    [clark_kernel(left, right) for right in features]
    for left in features
]

# Test Gram positivity through its defining sum-of-squares identity for exact
# rational coefficient packets.
coefficient_packets = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(-2), Fraction(3)],
    [Fraction(-1), Fraction(4), Fraction(2)],
]

energies = []
for coefficients in coefficient_packets:
    quadratic = sum(
        coefficients[j] * gram[j][k] * coefficients[k]
        for j in range(3)
        for k in range(3)
    )
    x_sum = [Fraction(0), Fraction(0)]
    y_sum = [Fraction(0), Fraction(0)]
    for coefficient, (x_feature, y_feature) in zip(coefficients, features):
        x_sum = add(x_sum, scale(coefficient, x_feature))
        y_sum = add(y_sum, scale(coefficient, y_feature))
    sum_of_squares = 2 * inner(x_sum, x_sum) + 2 * inner(y_sum, y_sum)
    assert quadratic == sum_of_squares
    assert quadratic >= 0
    energies.append(str(quadratic))

result = {
    "height_count": len(features),
    "gram_matrix": [[str(value) for value in row] for row in gram],
    "coefficient_packets_verified": len(coefficient_packets),
    "packet_energies": energies,
    "mixed_height_polarization_exact": True,
    "clark_kernel_positive": True,
    "full_transfer_defect_identity_constructed": False,
    "remaining_kernel": "typed seam, primitive, square, archimedean, and mixed boundary features",
    "verdict": "the Clark block is already a genuine positive mixed-height kernel; the missing object is the full boundary conservation identity",
}

out = Path(__file__).parents[1] / "results" / "rh-clark-mixed-height-kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
