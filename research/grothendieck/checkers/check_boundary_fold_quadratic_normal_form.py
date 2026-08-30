#!/usr/bin/env python3
"""Audit the quadratic boundary-fold normal form at a simple seam zero."""

import cmath
import math


# One positive atom gives Y(z)=sinh(z), X(z)=2cosh(z), with a simple seam
# zero at z0=i*pi/2. It is the minimal exact local model.
z0 = 0.5j * math.pi
y0 = cmath.sinh(z0)
x0 = 2.0 * cmath.cosh(z0)
x_prime_0 = 2.0 * cmath.sinh(z0)
quadratic_coefficient = 0.25 * x_prime_0

epsilon = 1.0e-4
delta = complex(epsilon, 0.7 * epsilon)
exact_increment = cmath.sinh(z0 + delta) - y0
quadratic_increment = quadratic_coefficient * delta * delta
scaled_remainder = abs(exact_increment - quadratic_increment) / abs(delta) ** 3

# The leading real part -2*kappa*a*tau vanishes on the seam and normal rays.
kappa = quadratic_coefficient.imag
seam_real = (quadratic_coefficient * complex(0.0, epsilon) ** 2).real
normal_real = (quadratic_coefficient * complex(epsilon, 0.0) ** 2).real
quadrant_real = (quadratic_coefficient * complex(epsilon, epsilon) ** 2).real

checks = {
    "simple_seam_zero": abs(x0) < 1.0e-14 and abs(x_prime_0) > 1.0,
    "quadratic_coefficient_is_pure_imaginary": abs(quadratic_coefficient.real) < 1.0e-15 and abs(kappa) > 0.4,
    "taylor_remainder_is_cubic": scaled_remainder < 0.2,
    "seam_and_normal_are_zero_level_rays": abs(seam_real) < 1.0e-20 and abs(normal_real) < 1.0e-20,
    "mixed_quadrant_has_nonzero_potential": abs(quadrant_real) > 0.9e-8,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "quadratic_coefficient": quadratic_coefficient,
        "scaled_cubic_remainder": scaled_remainder,
        "quadrant_real": quadrant_real,
    }
)

if failed:
    raise SystemExit(1)

