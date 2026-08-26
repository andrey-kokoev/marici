import cmath
import json
import math


def minor(q1, q2, x1, x2):
    return cmath.exp(-1j * (x1 * q1 + x2 * q2)) - cmath.exp(-1j * (x2 * q1 + x1 * q2))


def centered(q1, q2, x1, x2):
    center = 0.5 * (x1 + x2) * (q1 + q2)
    return 1j * cmath.exp(1j * center) * minor(q1, q2, x1, x2)


q1, q2 = 0.4, 2.1
x1, x2 = -0.7, 3.2
L = 5.3
M = -2.4
area = (x2 - x1) * (q2 - q1)
base = centered(q1, q2, x1, x2)
translated_q = centered(q1 + L, q2 + L, x1, x2)
translated_x = centered(q1, q2, x1 + M, x2 + M)
expected = 2.0 * math.sin(area / 2.0)

large_area = 7.0 * math.pi
grade = math.floor(large_area / (2.0 * math.pi))
oriented = 2.0 * math.sin(large_area / 2.0)
lifted_positive = ((-1) ** grade) * oriented

result = {
    "schema": "marici.grothendieck.affine_origin_centers_fourier_minor.v1",
    "checks": {
        "centered_minor_equals_area_half_angle": abs(base.real - expected) < 1e-12 and abs(base.imag) < 1e-12,
        "common_q_translation_is_removed_by_center_frame": abs(base - translated_q) < 1e-12,
        "common_frequency_translation_is_removed_by_center_frame": abs(base - translated_x) < 1e-12,
        "maslov_grade_restores_lifted_positive_orientation": lifted_positive > 0.0,
    },
    "area": area,
    "large_area_grade": grade,
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
