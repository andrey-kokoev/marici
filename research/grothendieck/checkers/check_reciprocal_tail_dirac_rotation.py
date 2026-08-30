#!/usr/bin/env python3
"""Verify the parity rotation of the reciprocal tail system."""

import cmath
import math


z = complex(0.3, 0.8)
q = 0.41
f = math.exp(-q)

# Exact reciprocal tails for f(q)=exp(-q).
g_plus = math.exp(-q) / (1.0 - z)
g_minus = math.exp(-q) / (1.0 + z)
g_plus_prime = -g_plus
g_minus_prime = -g_minus

root_two = math.sqrt(2.0)
p = (g_plus + g_minus) / root_two
q_channel = (g_plus - g_minus) / root_two
p_prime = (g_plus_prime + g_minus_prime) / root_two
q_prime = (g_plus_prime - g_minus_prime) / root_two

dirac_p_residual = p_prime + z * q_channel + root_two * f
dirac_q_residual = q_prime + z * p

# For this source, f'=-f and P''=P. Check the eliminated equation.
p_second = p
sturm_residual = -p_second + z * z * p - root_two * (-f)

# The unitary locus is Re(z)=0: -z sigma_x is then skew-Hermitian.
seam_z = complex(0.0, 1.7)
off_z = complex(0.2, 1.7)
seam_hermitian_part = abs((-seam_z + (-seam_z).conjugate()) / 2.0)
off_hermitian_part = abs((-off_z + (-off_z).conjugate()) / 2.0)

sample_endpoint = complex(0.4, -0.9)
anti_endpoint = -sample_endpoint
p_endpoint = (sample_endpoint + anti_endpoint) / root_two

checks = {
    "first_dirac_equation": abs(dirac_p_residual) < 1.0e-13,
    "second_dirac_equation": abs(dirac_q_residual) < 1.0e-13,
    "sturm_elimination": abs(sturm_residual) < 1.0e-13,
    "zero_is_symmetric_dirichlet": abs(p_endpoint) < 1.0e-15,
    "critical_line_is_unitary_locus": seam_hermitian_part < 1.0e-15 and off_hermitian_part > 0.1,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "dirac_residuals": [abs(dirac_p_residual), abs(dirac_q_residual)],
        "sturm_residual": abs(sturm_residual),
        "off_seam_hermitian_part": off_hermitian_part,
    }
)

if failed:
    raise SystemExit(1)

