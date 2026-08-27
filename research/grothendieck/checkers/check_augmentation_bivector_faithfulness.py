"""Exact augmentation-bivector identity on a finite label port."""

from fractions import Fraction
import json


def dot(left, right):
    return sum((left[i] * right[i] for i in range(len(left))), Fraction(0))


def norm_squared(vector):
    return dot(vector, vector)


def wedge_coordinates(left, right):
    return tuple(
        left[i] * right[j] - left[j] * right[i]
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )


omega = (Fraction(1), Fraction(1), Fraction(1))
fiber = (Fraction(1), Fraction(-2), Fraction(1))
q = Fraction(1, 2)
defect = tuple((1 - q * q) * value for value in fiber)
wedge_fiber = wedge_coordinates(omega, fiber)
wedge_defect = wedge_coordinates(omega, defect)

checks = {
    "scalar_output_vanishes": dot(omega, fiber) == 0,
    "fiber_is_nonzero": norm_squared(fiber) > 0,
    "gram_identity": norm_squared(wedge_fiber)
    == norm_squared(omega) * norm_squared(fiber) - dot(omega, fiber) ** 2,
    "faithful_zero_space_recovery": norm_squared(wedge_fiber)
    == len(omega) * norm_squared(fiber),
    "defect_wedge_scales_correctly": norm_squared(wedge_defect)
    == (1 - q * q) ** 2 * norm_squared(wedge_fiber),
    "bivector_is_nonzero": norm_squared(wedge_fiber) > 0,
}

result = {
    "schema": "marici.grothendieck.augmentation-bivector-faithfulness.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "omega": [str(x) for x in omega],
        "fiber": [str(x) for x in fiber],
        "wedge_coordinates": [str(x) for x in wedge_fiber],
        "fiber_norm_squared": str(norm_squared(fiber)),
        "wedge_norm_squared": str(norm_squared(wedge_fiber)),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
