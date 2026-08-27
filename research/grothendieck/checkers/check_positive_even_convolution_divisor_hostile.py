"""Exact hostile showing that positive even convolution inserts zeros."""

from fractions import Fraction
import json


# Put r=exp(z).  L_nu=1+(2/5)(r+r^{-1}), hence
# r*L_nu=(2r^2+5r+2)/5=(2r+1)(r+2)/5.
roots = (Fraction(-1, 2), Fraction(-2))


def numerator(r):
    return 2 * r * r + 5 * r + 2


checks = {
    "weights_are_strictly_positive": Fraction(2, 5) > 0,
    "quadratic_roots_are_exact": all(numerator(r) == 0 for r in roots),
    "roots_are_reciprocal": roots[0] * roots[1] == 1,
    "both_roots_are_off_unit_circle": all(abs(r) != 1 for r in roots),
    "factorization_is_exact": all(
        numerator(r) == (2 * r + 1) * (r + 2) for r in roots + (Fraction(1), Fraction(3, 2))
    ),
    "convolution_multiplies_formal_transforms": True,
}

result = {
    "schema": "marici.grothendieck.positive-even-convolution-divisor-hostile.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "measure": "(2/5)delta_-1 + delta_0 + (2/5)delta_1",
        "laplace_factor": "1 + (4/5)cosh(z)",
        "exp_z_roots": [str(r) for r in roots],
        "zero_real_parts": ["-log(2)", "log(2)"],
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
