"""Exact regime checks for the reciprocal three-cell square-current split."""

from fractions import Fraction
import json


def square_current(c):
    return 1 - c * c / 2


witnesses = {
    "on_seam": Fraction(3, 2),
    "collision": Fraction(2),
    "off_seam": Fraction(5, 2),
}

checks = {
    "on_seam_discriminant_negative": witnesses["on_seam"] ** 2 - 4 < 0,
    "collision_discriminant_zero": witnesses["collision"] ** 2 - 4 == 0,
    "off_seam_discriminant_positive": witnesses["off_seam"] ** 2 - 4 > 0,
    "on_seam_square_above_threshold": square_current(witnesses["on_seam"]) > -1,
    "collision_square_at_threshold": square_current(witnesses["collision"]) == -1,
    "off_seam_square_below_threshold": square_current(witnesses["off_seam"]) < -1,
    "discriminant_identity": all(
        c * c - 4 == -2 * (square_current(c) + 1) for c in witnesses.values()
    ),
    "primitive_remains_positive": all(c > 0 for c in witnesses.values()),
}

result = {
    "schema": "marici.grothendieck.square-current-reciprocal-zero-split.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        name: {
            "c": str(c),
            "a_1": str(c),
            "a_2": str(square_current(c)),
            "discriminant": str(c * c - 4),
        }
        for name, c in witnesses.items()
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
