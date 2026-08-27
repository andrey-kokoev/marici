"""Exact audit of the primitive lift in the doubled reciprocal flow."""

from fractions import Fraction
import json


z = Fraction(3)
c = Fraction(2)
f = Fraction(5)
u = Fraction(7)
v = Fraction(-11)
h = Fraction(13)

u_prime = -z * u - c * f
v_prime = z * v - c * f
h_prime = f

green_current_prime = 2 * u * u_prime - 2 * v * v_prime
relative = u - v
common = u + v
relative_prime = u_prime - v_prime
primitive_current_prime = 2 * h_prime * c * relative + 2 * h * c * relative_prime

positive_bulk = 2 * z * (u * u + v * v)
forcing = 2 * c * f * relative
common_residual = 2 * z * h * c * common

checks = {
    "relative_flow": relative_prime == -z * common,
    "doubled_green_identity": positive_bulk == -green_current_prime - forcing,
    "primitive_current_identity": primitive_current_prime == forcing - common_residual,
    "transferred_identity": positive_bulk == -(green_current_prime + primitive_current_prime) - common_residual,
    "positive_bulk_nonzero": positive_bulk > 0,
    "common_residual_nonzero_in_hostile": common_residual != 0,
    "pointwise_common_zero_would_remove_residual": 2 * z * h * c * Fraction(0) == 0,
}

result = {
    "schema": "marici.grothendieck.primitive-lift-common-path-residual.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "values": {
        "positive_bulk": str(positive_bulk),
        "forcing": str(forcing),
        "primitive_current_prime": str(primitive_current_prime),
        "common_residual": str(common_residual),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
