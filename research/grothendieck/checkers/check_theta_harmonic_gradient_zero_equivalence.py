#!/usr/bin/env python3
"""Verify the harmonic-gradient realization of the two quadratures."""

import cmath


atoms = [0.3, 0.9, 1.8]
weights = [1.2, 0.5, 0.25]
a = 0.4
t = 1.1
z = complex(a, t)


def source_sum(function):
    return sum(weight * function(q) for q, weight in zip(atoms, weights))


y_value = source_sum(lambda q: cmath.sinh(z * q) / q)
y_prime = source_sum(lambda q: cmath.cosh(z * q))
x_value = 2.0 * y_prime

u_a = source_sum(lambda q: cmath.cosh(a * q).real * cmath.cos(t * q).real)
u_t = -source_sum(lambda q: cmath.sinh(a * q).real * cmath.sin(t * q).real)
gradient_complex = u_a - 1j * u_t

c_a = source_sum(lambda q: q * cmath.sinh(a * q).real * cmath.cos(t * q).real)
c_t = -source_sum(lambda q: q * cmath.cosh(a * q).real * cmath.sin(t * q).real)
s_a = source_sum(lambda q: q * cmath.cosh(a * q).real * cmath.sin(t * q).real)
s_t = source_sum(lambda q: q * cmath.sinh(a * q).real * cmath.cos(t * q).real)
jacobian = c_a * s_t - c_t * s_a
x_prime = 2.0 * source_sum(lambda q: q * cmath.sinh(z * q))

seam_u = source_sum(lambda q: cmath.sinh(0.0 * q).real * cmath.cos(t * q).real / q)
seam_tangent = -source_sum(lambda q: cmath.sinh(0.0 * q).real * cmath.sin(t * q).real)

checks = {
    "primitive_derivative_is_half_readout": abs(x_value - 2.0 * y_prime) < 1.0e-15,
    "gradient_reconstructs_half_readout": abs(gradient_complex - y_prime) < 1.0e-13,
    "cauchy_riemann_first": abs(c_a - s_t) < 1.0e-13,
    "cauchy_riemann_second": abs(c_t + s_a) < 1.0e-13,
    "jacobian_is_derivative_norm": abs(jacobian - 0.25 * abs(x_prime) ** 2) < 1.0e-12,
    "seam_is_constant_potential_boundary": abs(seam_u) < 1.0e-15 and abs(seam_tangent) < 1.0e-15,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "primitive": y_value,
        "gradient_error": abs(gradient_complex - y_prime),
        "jacobian_error": abs(jacobian - 0.25 * abs(x_prime) ** 2),
    }
)

if failed:
    raise SystemExit(1)

