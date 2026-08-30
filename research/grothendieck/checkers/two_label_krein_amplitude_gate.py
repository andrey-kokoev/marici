import json
import math


u1, u2 = 1.0, 2.0
y = 0.2
x = math.pi / (u2 - u1)

a = math.sinh(2.0 * y * u1)
b = math.sinh(2.0 * y * u2)
c = math.sinh(y * (u1 + u2))
disc = c * c - a * b
r_minus = (c - math.sqrt(disc)) / b
r_plus = (c + math.sqrt(disc)) / b


def half_krein(r):
    return a + b * r * r - 2.0 * c * r


r_negative = c / b
r_positive = r_plus + 1.0

result = {
    "schema": "marici.grothendieck.two_label_krein_amplitude_gate.v1",
    "checks": {
        "two_label_krein_matrix_is_indefinite": disc > 0.0,
        "same_geometry_has_negative_orientation": half_krein(r_negative) < 0.0,
        "same_geometry_has_positive_orientation": half_krein(r_positive) > 0.0,
        "negative_ratios_form_exact_open_interval": r_minus < r_negative < r_plus,
    },
    "fixed_geometry": {"u1": u1, "u2": u2, "x": x, "y": y},
    "negative_ratio_interval": [r_minus, r_plus],
    "tested_ratios": {"negative": r_negative, "positive": r_positive},
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
