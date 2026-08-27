#!/usr/bin/env python3
"""Verify the two-quadrature decomposition and the scope distinction."""

import cmath


# Finite positive atomic source for an exact algebraic audit.
atoms = [0.4, 1.1, 2.0]
weights = [1.0, 0.7, 0.2]
a = 0.3
t = 1.4

f_a = sum(weight * cmath.exp((a + 1j * t) * q) for q, weight in zip(atoms, weights))
f_minus_a = sum(weight * cmath.exp((-a + 1j * t) * q) for q, weight in zip(atoms, weights))
x_value = f_a + f_minus_a.conjugate()

c_quadrature = sum(
    weight * cmath.cosh(a * q).real * cmath.cos(t * q).real
    for q, weight in zip(atoms, weights)
)
s_quadrature = sum(
    weight * cmath.sinh(a * q).real * cmath.sin(t * q).real
    for q, weight in zip(atoms, weights)
)
x_from_quadratures = 2.0 * c_quadrature + 2.0j * s_quadrature

# Equal modulus is weaker than antipodal cancellation.
equal_modulus_pair_left = 1.0 + 0.0j
equal_modulus_pair_right = 0.0 + 1.0j

# An antipodal pair cancels and has equal modulus.
antipode_left = 0.6 - 0.8j
antipode_right = -antipode_left

checks = {
    "quadratures_reconstruct_readout": abs(x_value - x_from_quadratures) < 1.0e-13,
    "seam_antisymmetric_quadrature_vanishes": all(abs(cmath.sinh(0.0 * q)) < 1.0e-15 for q in atoms),
    "equal_modulus_need_not_cancel": abs(abs(equal_modulus_pair_left) - abs(equal_modulus_pair_right)) < 1.0e-15 and abs(equal_modulus_pair_left + equal_modulus_pair_right) > 1.0,
    "antipode_implies_equal_modulus": abs(abs(antipode_left) - abs(antipode_right)) < 1.0e-15,
    "antipode_is_exact_zero_condition": abs(antipode_left + antipode_right) < 1.0e-15,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "readout_error": abs(x_value - x_from_quadratures),
        "equal_modulus_nonzero_sum": equal_modulus_pair_left + equal_modulus_pair_right,
    }
)

if failed:
    raise SystemExit(1)

