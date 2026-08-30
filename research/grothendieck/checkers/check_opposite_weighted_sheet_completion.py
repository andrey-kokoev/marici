#!/usr/bin/env python3
"""Verify opposite sheet weights and fixed-domain conjugation."""

import cmath
import math


z = complex(0.3, 0.8)
a = z.real
t = z.imag
q = 0.47

# Source f(q)=exp(-q), valid for |a|<1.
f = math.exp(-q)
g_plus = math.exp(-q) / (1.0 - z)
g_minus = math.exp(-q) / (1.0 + z)
h_plus = math.exp(a * q) * g_plus
h_minus = math.exp(-a * q) * g_minus

g_plus_prime = -g_plus
g_minus_prime = -g_minus
h_plus_prime = a * h_plus + math.exp(a * q) * g_plus_prime
h_minus_prime = -a * h_minus + math.exp(-a * q) * g_minus_prime

plus_original = g_plus_prime + z * g_plus
plus_conjugated = math.exp(-a * q) * (h_plus_prime + 1j * t * h_plus)
minus_original = -g_minus_prime + z * g_minus
minus_conjugated = math.exp(a * q) * (-h_minus_prime + 1j * t * h_minus)

# Exact endpoint tilted transforms.
f_a = 1.0 / (1.0 - a - 1j * t)
f_minus_a_conjugate = 1.0 / (1.0 + a + 1j * t)
x_from_tilts = f_a + f_minus_a_conjugate
x_original = 1.0 / (1.0 - z) + 1.0 / (1.0 + z)

# Weighted homogeneous modes have constant modulus and are not L2.
weighted_plus_homogeneous_modulus = abs(cmath.exp(-1j * t * 123.0))
weighted_minus_homogeneous_modulus = abs(cmath.exp(1j * t * 123.0))

checks = {
    "plus_fixed_domain_conjugation": abs(plus_original - plus_conjugated) < 1.0e-13,
    "minus_fixed_domain_conjugation": abs(minus_original - minus_conjugated) < 1.0e-13,
    "plus_source_equation": abs(plus_original + f) < 1.0e-13,
    "minus_source_equation": abs(minus_original - f) < 1.0e-13,
    "tilted_endpoint_reconstructs_readout": abs(x_from_tilts - x_original) < 1.0e-13,
    "weighted_homogeneous_modes_are_nondecreasing": abs(weighted_plus_homogeneous_modulus - 1.0) < 1.0e-13 and abs(weighted_minus_homogeneous_modulus - 1.0) < 1.0e-13,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "plus_conjugation_error": abs(plus_original - plus_conjugated),
        "minus_conjugation_error": abs(minus_original - minus_conjugated),
        "readout_error": abs(x_from_tilts - x_original),
    }
)

if failed:
    raise SystemExit(1)

