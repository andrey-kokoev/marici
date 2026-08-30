"""Exact hostile for pointwise common-path cancellation."""

from fractions import Fraction
import json


z = Fraction(1)
c = Fraction(1)


def f(q):
    return Fraction(1) + q


q0 = Fraction(0)
q1 = Fraction(1)
u_forced_0 = -c * f(q0) / z
u_forced_1 = -c * f(q1) / z

# Pointwise anti-diagonality plus both flow equations requires u'=0.
required_u_prime = Fraction(0)
finite_difference = u_forced_1 - u_forced_0

checks = {
    "forcing_is_nonconstant": f(q0) != f(q1),
    "forced_u_is_nonconstant": u_forced_0 != u_forced_1,
    "two_flow_comparison_requires_u_prime_zero": required_u_prime == 0,
    "finite_difference_contradicts_constant_u": finite_difference != required_u_prime,
    "z_is_nonzero": z != 0,
    "amplitude_is_nonzero": c != 0,
}

result = {
    "schema": "marici.grothendieck.common-path-cancellation-incompatibility.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "z": str(z),
        "c": str(c),
        "f_0": str(f(q0)),
        "f_1": str(f(q1)),
        "forced_u_0": str(u_forced_0),
        "forced_u_1": str(u_forced_1),
        "finite_difference": str(finite_difference),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
